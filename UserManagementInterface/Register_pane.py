# -*- coding: utf-8 -*-
__author__ = 'liangjh'
__helper__ = 'Aileon'

import sys
from PyQt5.Qt import *
from UserManagementInterface.register_save_as_txt import Ui_Form

from UserManagementBackend.UserRegister import Register
from UserManagementBackend.UserManagementError import RegisterPasswordError, UserExistError


class Regist(QWidget):
    exit_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit_auth_id.textChanged.connect(self.enable_regist)
        self.ui.lineEdit_username.textChanged.connect(self.enable_regist)
        self.ui.lineEdit_pwd.textChanged.connect(self.enable_regist)
        self.ui.lineEdit_pwd_confirm.textChanged.connect(self.enable_regist)
        self.ui.pushButton_regist.clicked.connect(self.save_as_txt)
        self.show()

    # -------------------修改的代码段------------------------
    # def save_as_txt(self):
    #     user_name = self.ui.lineEdit_username.text()
    #     pwd = self.ui.lineEdit_pwd.text()
    #     with open('user.txt', 'w') as f:
    #         f.writelines(user_name + '\n')
    #         f.writelines(pwd + '\n')
    #     self.exit_signal.emit()

    # 以上是原代码
    # 以下是为了使用后端逻辑而修改的代码

    def save_as_txt(self):
        user_name = self.ui.lineEdit_username.text()  # 注册用户名
        pwd = self.ui.lineEdit_pwd.text()  # 注册密码
        auth = self.ui.comboBox.currentText()  # 注册身份
        auth_id = int(self.ui.lineEdit_auth_id.text())  # 注册该身份的权限密钥,由于我在数据库里设置了整型，故int
        try:
            Register().register(user_name, pwd, auth, auth_id)
            QMessageBox.about(self, '提示', f'{user_name} 注册成功！')
        except RegisterPasswordError as e:
            print(e)
            QMessageBox.about(self, '提示', '注册口令错误！')
        except UserExistError as e:
            print(e)
            QMessageBox.about(self, '提示', '用户已存在！')
        except Exception as e:
            print(e)
            QMessageBox.about(self, '提示', '注册出现异常！')
        self.exit_signal.emit()
    # ---------------------------------------------------------

    def enable_regist(self):
        auth_id = self.ui.lineEdit_auth_id.text()
        user_name = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        pwd_confirm = self.ui.lineEdit_pwd_confirm.text()
        if len(user_name) > 0 and len(pwd) > 0 and pwd == pwd_confirm:
            self.ui.pushButton_regist.setEnabled(True)
        else:
            self.ui.pushButton_regist.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Regist()
    w.show()
    sys.exit(app.exec_())
