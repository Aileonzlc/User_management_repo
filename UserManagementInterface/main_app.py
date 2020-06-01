import sys
from PyQt5.Qt import *
from UserManagementInterface.Login_pane import Login
from UserManagementInterface.Register_pane import Regist

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login_pane = Login()
    Regist_pane = Regist()
    Regist_pane.hide()
    Login_pane.show()


    def show_register():
        Login_pane.hide()
        Regist_pane.show()


    Login_pane.show_register_signal.connect(show_register)


    def exit_regist():
        Regist_pane.hide()
        Login_pane.show()


    Regist_pane.exit_signal.connect(exit_regist)
    sys.exit(app.exec_())
