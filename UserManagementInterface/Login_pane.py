import sys
from PyQt5.Qt import *
from support_system.Login_read_txt import Ui_Form


class Login(QWidget):
    show_register_signal = pyqtSignal()
    check_login_signal = pyqtSignal()
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit_username.textChanged.connect(self.enable_login)
        self.ui.lineEdit_pwd.textChanged.connect(self.enable_login)
        self.ui.pushButton_login.clicked.connect(self.verify_user_data)
        self.ui.pushButton_regist.clicked.connect(self.show_register)
        self.show()

    def enable_login(self):
        user_name = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        if len(user_name)>0 and len(pwd)>0:
            self.ui.pushButton_login.setEnabled(True)
        else:
            self.ui.pushButton_login.setEnabled(False)

    def verify_user_data(self):
        user_name = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        with open('user.txt', 'r') as f:
            user_name_in_text = f.readline().strip()
            pwd_in_text = f.readline().strip()
            print(user_name_in_text, pwd_in_text)
        if user_name == user_name_in_text and pwd == pwd_in_text:
            QMessageBox.about(self, '提示', '登录成功！')
        else:
            QMessageBox.about(self, '提示', '登录失败！')

    def show_register(self):
        self.show_register_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec_())