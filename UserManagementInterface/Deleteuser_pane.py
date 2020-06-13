# -*- coding: utf-8 -*-
__author__ = 'liangjh'
__helper__ = 'Aileon'

import sys
from PyQt5.Qt import QDialog, QApplication, QTableWidgetItem, QMessageBox
from UserManagementInterface.Deleteuser import Ui_Dialog_DeleteUser

from UserManagementBackend.UserQuery import Query
from UserManagementBackend.UserDelete import Delete
from UserManagementBackend.UserManagementError import *


class Deleteuser(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Dialog_DeleteUser()
        self.ui.setupUi(self)

        self.ui.tableWidget_userInfo.itemSelectionChanged.connect(self.enable_delete)
        self.ui.comboBox_userID.currentTextChanged.connect(self.enable_query)
        self.ui.lineEdit_username.textChanged.connect(self.enable_query)
        self.ui.pushButton_query.clicked.connect(self.query_user_info)
        self.ui.pushButton_viewall.clicked.connect(self.view_all_user_info)
        self.ui.pushButton_delete.clicked.connect(self.delete_user)

    """          1、这个函数我把and改成了or          """
    def enable_query(self):
        user_ID = self.ui.comboBox_userID.currentText()
        username = self.ui.lineEdit_username.text()
        if user_ID or username:
            self.ui.pushButton_query.setEnabled(True)
        else:
            self.ui.pushButton_query.setEnabled(False)
        pass

    def enable_delete(self):
        if self.ui.tableWidget_userInfo.selectedItems():
            seleted_column = self.ui.tableWidget_userInfo.selectedItems()[0].column()
            seleted_text = self.ui.tableWidget_userInfo.selectedItems()[0].text()
            if seleted_column == 0 and len(seleted_text) > 0:
                self.ui.pushButton_delete.setEnabled(True)
            else:
                self.ui.pushButton_delete.setEnabled(False)

    """           2、这是我新增的函数用来向表格里插入用户行              """
    def insert_users_into_table(self, users):
        # 把这句清理放到前面来
        self.ui.tableWidget_userInfo.clearContents()
        totalrow = self.ui.tableWidget_userInfo.rowCount()
        assert totalrow >= 10  # 这里的10是你之前在ui设置的10行
        for i in range(totalrow-1, 10, -1):  # 多出几行删几行，不然你的行数会一直增加
            self.ui.tableWidget_userInfo.removeRow(i)
        user_index = 0  # 记录第几个用户, 第几个用户就放在第几行
        for user in users:
            user_ID = user['remote_identity']
            username = user['name']
            pwd = user['password']
            auth = str(user['authority'])
            name_Item = QTableWidgetItem(username)
            name_Item.setTextAlignment(132)
            pwd_Item = QTableWidgetItem(pwd)
            pwd_Item.setTextAlignment(132)
            ID_Item = QTableWidgetItem(user_ID)
            ID_Item.setTextAlignment(132)
            auth_Item = QTableWidgetItem(auth)
            auth_Item.setTextAlignment(132)
            self.ui.tableWidget_userInfo.insertRow(user_index)
            self.ui.tableWidget_userInfo.setItem(user_index, 0, name_Item)
            self.ui.tableWidget_userInfo.setItem(user_index, 1, pwd_Item)
            self.ui.tableWidget_userInfo.setItem(user_index, 2, ID_Item)
            self.ui.tableWidget_userInfo.setItem(user_index, 3, auth_Item)

            user_index += 1

    """"               3、这是修改后的查询函数             """
    def query_user_info(self):
        # 查询之前先把表格清空，相当于刷新，不然即使下边找不到用户了，之前的记录依旧呈现再界面上
        self.insert_users_into_table([])
        user_ID = self.ui.comboBox_userID.currentText()
        # 因为输入表示的是用户名中包含的字符串，所以我帮你改了一下变量名
        string_in_username = self.ui.lineEdit_username.text()
        try:
            # 这里会返回一个列表，列表里包含多个用户
            users = Query().query(identity=user_ID, str_in_name=string_in_username)
            # 排除一下管理员
            users = [user for user in users if user['remote_identity'] != '管理员']
            self.insert_users_into_table(users)
        except UserDoesNotExistError as err:
            QMessageBox.about(self, '提示', '用户不存在')

    """"               4、这是修改后的查询函数             """
    def view_all_user_info(self):
        try:
            # 这里会返回一个列表，列表里包含多个用户
            users = Query().query()
            users = [user for user in users if user['remote_identity'] != '管理员']
            self.insert_users_into_table(users)
        except UserDoesNotExistError as err:
            # 至少会查询到当前登陆用户这一个用户
            QMessageBox.about(self, '提示', '不存在任何用户，数据库用户表出错！')

    def delete_user(self):
        seleted_user = self.ui.tableWidget_userInfo.selectedItems()[0].text()
        try:
            Delete().delete(seleted_user)
            QMessageBox.about(self, '提示', '删除成功')
        except UserDoesNotExistError as err:
            QMessageBox.about(self, '提示', '要删除的用户不存在')
        # 删除后刷新一下界面，并且要把按钮重新置为false，否则在第一次删除完，而第二次没有item被选择的情况下会报IndexError
        self.view_all_user_info()
        self.ui.pushButton_delete.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Deleteuser()
    w.show()
    sys.exit(app.exec_())