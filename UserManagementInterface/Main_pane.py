import sys
from UserManagementInterface.main_ui import Ui_MainWindow
from  PyQt5.Qt import QApplication, QMainWindow
from UserManagementInterface.Adduser_pane import Adduser
from UserManagementInterface.Alteruser_pane import Alteruser
from UserManagementInterface.Deleteuser_pane import Deleteuser

class Main_pane(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_adduser.triggered.connect(self.Add_user)
        self.ui.action_deleteuser.triggered.connect(self.Delete_user)
        self.ui.action_alteruser.triggered.connect(self.Alter_user)

    def Add_user(self):
        print('新增用户')
        Adduser_pane = Adduser(self)
        Adduser_pane.show()
        pass

    def Alter_user(self):
        print('修改用户信息')
        Alteruser_pane = Alteruser(self)
        Alteruser_pane.show()
        pass

    def Delete_user(self):
        print('删除用户')
        Deleteuser_pane = Deleteuser(self)
        Deleteuser_pane.show()
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_pane()
    w.show()
    sys.exit(app.exec_())
