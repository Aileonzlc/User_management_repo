# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Adduser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_AddUser(object):
    def setupUi(self, Dialog_AddUser):
        Dialog_AddUser.setObjectName("Dialog_AddUser")
        Dialog_AddUser.resize(306, 254)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_AddUser.sizePolicy().hasHeightForWidth())
        Dialog_AddUser.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_AddUser)
        self.gridLayout.setObjectName("gridLayout")
        self.label_userID = QtWidgets.QLabel(Dialog_AddUser)
        self.label_userID.setMinimumSize(QtCore.QSize(80, 40))
        self.label_userID.setObjectName("label_userID")
        self.gridLayout.addWidget(self.label_userID, 0, 0, 1, 1)
        self.comboBox_userID = QtWidgets.QComboBox(Dialog_AddUser)
        self.comboBox_userID.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_userID.setCurrentText("")
        self.comboBox_userID.setObjectName("comboBox_userID")
        self.comboBox_userID.addItem("")
        self.comboBox_userID.addItem("")
        self.comboBox_userID.addItem("")
        self.gridLayout.addWidget(self.comboBox_userID, 0, 1, 1, 1)
        self.label_username = QtWidgets.QLabel(Dialog_AddUser)
        self.label_username.setMinimumSize(QtCore.QSize(80, 40))
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 1, 0, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(Dialog_AddUser)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 1, 1, 1, 1)
        self.label_pwd = QtWidgets.QLabel(Dialog_AddUser)
        self.label_pwd.setMinimumSize(QtCore.QSize(80, 40))
        self.label_pwd.setObjectName("label_pwd")
        self.gridLayout.addWidget(self.label_pwd, 2, 0, 1, 1)
        self.lineEdit_pwd = QtWidgets.QLineEdit(Dialog_AddUser)
        self.lineEdit_pwd.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.gridLayout.addWidget(self.lineEdit_pwd, 2, 1, 1, 1)
        self.label_pwdconfirm = QtWidgets.QLabel(Dialog_AddUser)
        self.label_pwdconfirm.setMinimumSize(QtCore.QSize(80, 40))
        self.label_pwdconfirm.setObjectName("label_pwdconfirm")
        self.gridLayout.addWidget(self.label_pwdconfirm, 3, 0, 1, 1)
        self.lineEdit_pwdconfirm = QtWidgets.QLineEdit(Dialog_AddUser)
        self.lineEdit_pwdconfirm.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_pwdconfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwdconfirm.setObjectName("lineEdit_pwdconfirm")
        self.gridLayout.addWidget(self.lineEdit_pwdconfirm, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_rewrite = QtWidgets.QPushButton(Dialog_AddUser)
        self.pushButton_rewrite.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_rewrite.setObjectName("pushButton_rewrite")
        self.horizontalLayout.addWidget(self.pushButton_rewrite)
        self.pushButton_adduser = QtWidgets.QPushButton(Dialog_AddUser)
        self.pushButton_adduser.setEnabled(False)
        self.pushButton_adduser.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_adduser.setObjectName("pushButton_adduser")
        self.horizontalLayout.addWidget(self.pushButton_adduser)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.retranslateUi(Dialog_AddUser)
        self.comboBox_userID.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_AddUser)

    def retranslateUi(self, Dialog_AddUser):
        _translate = QtCore.QCoreApplication.translate
        Dialog_AddUser.setWindowTitle(_translate("Dialog_AddUser", "新增用户"))
        self.label_userID.setText(_translate("Dialog_AddUser", "用 户 身 份"))
        self.comboBox_userID.setItemText(0, _translate("Dialog_AddUser", "安全工程师"))
        self.comboBox_userID.setItemText(1, _translate("Dialog_AddUser", "操纵员"))
        self.comboBox_userID.setItemText(2, _translate("Dialog_AddUser", "一般用户"))
        self.label_username.setText(_translate("Dialog_AddUser", "用 户 名"))
        self.label_pwd.setText(_translate("Dialog_AddUser", "密    码"))
        self.label_pwdconfirm.setText(_translate("Dialog_AddUser", "密 码 确 认"))
        self.pushButton_rewrite.setText(_translate("Dialog_AddUser", "重新输入"))
        self.pushButton_adduser.setText(_translate("Dialog_AddUser", "确认新增"))
