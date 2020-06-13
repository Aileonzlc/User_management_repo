# -*- coding: utf-8 -*-
__author__ = 'liangjh'

import sys
from PyQt5.Qt import *
from UserManagementInterface.Login_pane import Login
from UserManagementInterface.Main_pane import Main_pane

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login_pane = Login()
    Main_pane = Main_pane()
    Login_pane.show()

    def show_main_pane():
        Login_pane.close()
        Main_pane.show()

    Login_pane.Login_signal.connect(show_main_pane)


    sys.exit(app.exec_())
