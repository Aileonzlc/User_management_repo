# -*- coding: utf-8 -*-
__author__ = 'liangjh'
__helper__ = 'Aileon'

import sys
from PyQt5.Qt import QWidget, QApplication, pyqtSignal, QMessageBox
from UserManagementInterface.Login_ui import Ui_Form_Login

from UserManagementBackend.UserLogin import LoginFactoryEncrypt, LoginUser
from UserManagementBackend.UserManagementError import PasswordError, UserDoesNotExistError, IdentityDoesNotExistError


class Login(QWidget):
    Login_signal = pyqtSignal()
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Form_Login()
        self.ui.setupUi(self)
        self.ui.lineEdit_username.textChanged.connect(self.enable_login)
        self.ui.lineEdit_pwd.textChanged.connect(self.enable_login)
        self.ui.pushButton_login.clicked.connect(self.verify_user_data)
        self.ui.pushButton_exit.clicked.connect(self.close)
        self.show()

    def enable_login(self):
        user_name = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        if len(user_name) > 0 and len(pwd) > 0:
            self.ui.pushButton_login.setEnabled(True)
        else:
            self.ui.pushButton_login.setEnabled(False)

    # ------------------修改的代码段-----------------------------
    # def verify_user_data(self):
    #     user_name = self.ui.lineEdit_username.text()
    #     pwd = self.ui.lineEdit_pwd.text()
    #     with open('user.txt', 'r') as f:
    #         user_name_in_text = f.readline().strip()
    #         pwd_in_text = f.readline().strip()
    #         print(user_name_in_text, pwd_in_text)
    #     if user_name == user_name_in_text and pwd == pwd_in_text:
    #         QMessageBox.about(self, '提示', '登录成功！')
    #     else:
    #         QMessageBox.about(self, '提示', '登录失败！')

    # 以上为原代码
    # 以下为修改后的代码

    def verify_user_data(self):
        user_name = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        try:
            login_user = LoginUser(LoginFactoryEncrypt().create_user(user_name, pwd))
            QMessageBox.about(self, '提示', f'登录成功！您的权限为 {login_user.get_authority()}')
            self.Login_signal.emit()
        except PasswordError as e:
            print(e)
            QMessageBox.about(self, '提示', '密码错误！')
        except UserDoesNotExistError as e:
            print(e)
            QMessageBox.about(self, '提示', '用户不存在！')
        except IdentityDoesNotExistError as e:
            print(e)
            QMessageBox.about(self, '提示', '身份不存在！')
    # -------------------------------------------------------------------




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec_())
