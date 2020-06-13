# -*- coding: utf-8 -*-
__author__ = 'liangjh'
__helper__ = 'Aileon'

import sys
from PyQt5.Qt import QDialog, QApplication, QMessageBox, QTableWidgetItem
from UserManagementInterface.Alteruser import Ui_Dialog_Alteruser

from UserManagementBackend.UserQuery import Query
from UserManagementBackend.UserUpdate import Update
from UserManagementBackend.UserManagementError import *

class Alteruser(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Dialog_Alteruser()
        self.ui.setupUi(self)
        self.ui.tableWidget_userInfo.itemSelectionChanged.connect(self.enable_alter)
        self.ui.comboBox_userID.currentTextChanged.connect(self.enable_query)
        self.ui.lineEdit_username.textChanged.connect(self.enable_query)
        self.ui.pushButton_query.clicked.connect(self.query_user_info)
        self.ui.pushButton_viewall.clicked.connect(self.view_all_user_info)
        self.ui.pushButton_alter.clicked.connect(self.alter_user_info)

    def enable_alter(self):
        if self.ui.tableWidget_userInfo.selectedItems():
            seleted_column = self.ui.tableWidget_userInfo.selectedItems()[0].column()
            seleted_text = self.ui.tableWidget_userInfo.selectedItems()[0].text()
            if seleted_column == 0 and len(seleted_text) > 0:
                self.ui.pushButton_alter.setEnabled(True)
            else:
                self.ui.pushButton_alter.setEnabled(False)
        pass

    def enable_query(self):
        user_ID = self.ui.comboBox_userID.currentText()
        username = self.ui.lineEdit_username.text()
        if user_ID or username:
            self.ui.pushButton_query.setEnabled(True)
        else:
            self.ui.pushButton_query.setEnabled(False)
        pass

    def insert_users_into_table(self, users):
        self.ui.tableWidget_userInfo.clearContents()
        totalrow = self.ui.tableWidget_userInfo.rowCount()
        assert totalrow >= 10  # 这里的10是你之前在ui设置的10行
        for i in range(totalrow - 1, 10, -1):  # 多出几行删几行，不然你的行数会一直增加
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

    def query_user_info(self):
        # 1、查询之前先把表格清空，相当于刷新，不然即使下边找不到用户了，之前的记录依旧呈现再界面上
        self.insert_users_into_table([])
        user_ID = self.ui.comboBox_userID.currentText()
        string_in_username = self.ui.lineEdit_username.text()
        try:
            users = Query().query(identity=user_ID, str_in_name=string_in_username)
            # 1、这里是我之前忘了加的，要把管理员排除在外，我设定的是管理员只能自己删除，这个功能回头再加
            users = [user for user in users if user['remote_identity'] != '管理员']
            self.insert_users_into_table(users)
        except UserDoesNotExistError as err:
            QMessageBox.about(self, '提示', '用户不存在')

    def view_all_user_info(self):
        try:
            # 这里会返回一个列表，列表里包含多个用户
            users = Query().query()
            users = [user for user in users if user['remote_identity'] != '管理员']
            self.insert_users_into_table(users)
        except UserDoesNotExistError as err:
            # 至少会查询到当前登陆用户这一个用户
            QMessageBox.about(self, '提示', '不存在任何用户，数据库用户表出错！')
        pass

    def alter_user_info(self):
        old_name = self.ui.tableWidget_userInfo.selectedItems()[0].text()
        new_name = self.ui.lineEdit_newname.text()
        new_pwd = self.ui.lineEdit_newpwd.text()
        new_ID = self.ui.comboBox_newID.currentText()
        try:
            Update().update(old_name=old_name, new_name=new_name, new_password=new_pwd, new_identity=new_ID)
            QMessageBox.about(self, '提示', '更改成功！')
        except UserExistError as err:
            QMessageBox.about(self, '提示', '新的用户名已存在，不能进行更新')
        except IdentityDoesNotExistError as err:
            QMessageBox.about(self, '提示', '新的身份不存在')
        except UserDoesNotExistError as err:
            QMessageBox.about(self, '提示', '需要更新的用户不存在')
        # 2、更新完成后刷新一下界面，显示所有的记录，并且要把按钮重新置为False
        self.view_all_user_info()
        self.ui.pushButton_alter.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Alteruser()
    w.show()
    sys.exit(app.exec_())