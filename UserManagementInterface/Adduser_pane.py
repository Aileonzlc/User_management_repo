# -*- coding: utf-8 -*-
__author__ = 'liangjh'
__helper__ = 'Aileon'

import sys
from PyQt5.Qt import QDialog, QApplication, QMessageBox
from UserManagementInterface.Adduser import Ui_Dialog_AddUser

from UserManagementBackend.UserRegister import Register
from UserManagementBackend.UserManagementError import *


class Adduser(QDialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Dialog_AddUser()
        self.ui.setupUi(self)
        self.ui.comboBox_userID.currentTextChanged.connect(self.enable_add)
        self.ui.lineEdit_username.textChanged.connect(self.enable_add)
        self.ui.lineEdit_pwd.textChanged.connect(self.enable_add)
        self.ui.lineEdit_pwdconfirm.textChanged.connect(self.enable_add)
        self.ui.pushButton_adduser.clicked.connect(self.Add_user)
        self.ui.pushButton_rewrite.clicked.connect(self.Rewrite)

    def enable_add(self):
        user_ID = self.ui.comboBox_userID.currentText()
        username = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        pwdconfirm = self.ui.lineEdit_pwdconfirm.text()
        if len(user_ID)>0 and len(username)>0 and len(pwd)>0 and pwd == pwdconfirm:
            self.ui.pushButton_adduser.setEnabled(True)
        else:
            self.ui.pushButton_adduser.setEnabled(False)
        pass

    def Add_user(self):
        user_ID = self.ui.comboBox_userID.currentText()
        username = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        try:
            Register().register(username, pwd, user_ID)
            QMessageBox.about(self, '提示', '成功新增用户！')
            self.Rewrite()
        except IdentityDoesNotExistError as err:
            print(err)
            QMessageBox.about(self, '提示', '注册身份不存在，请重新输入')
        except UserExistError as err:
            print(err)
            QMessageBox.about(self, '提示', '用户名已存在,请重新输入')
        except InputIsNoneError as err:
            print(err)
            QMessageBox.about(self, '提示', '输入为空,请重新输入')
        pass

    def Rewrite(self):
        print('重新输入')
        self.ui.comboBox_userID.setCurrentIndex(-1)
        self.ui.lineEdit_username.clear()
        self.ui.lineEdit_pwd.clear()
        self.ui.lineEdit_pwdconfirm.clear()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Adduser()
    w.show()
    sys.exit(app.exec_())