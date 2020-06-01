import sys
from PyQt5.Qt import *
from UserManagementInterface.register_save_as_txt import Ui_Form


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

    def save_as_txt(self):
        user_name = self.ui.lineEdit_username.text()
        pwd = self.ui.lineEdit_pwd.text()
        with open('user.txt', 'w') as f:
            f.writelines(user_name + '\n')
            f.writelines(pwd + '\n')
        self.exit_signal.emit()

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