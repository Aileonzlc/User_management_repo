# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Login(object):
    def setupUi(self, Form_Login):
        Form_Login.setObjectName("Form_Login")
        Form_Login.resize(450, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_Login.sizePolicy().hasHeightForWidth())
        Form_Login.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form_Login)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_left = QtWidgets.QWidget(Form_Login)
        self.widget_left.setObjectName("widget_left")
        self.horizontalLayout.addWidget(self.widget_left)
        self.widget_center = QtWidgets.QWidget(Form_Login)
        self.widget_center.setObjectName("widget_center")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_center)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_center)
        self.label.setStyleSheet("background-image: url(:/label_image/智能运行支持系统.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_username = QtWidgets.QLabel(self.widget_center)
        self.label_username.setMinimumSize(QtCore.QSize(0, 40))
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 1, 0, 1, 1)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_center)
        self.lineEdit_username.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 1, 1, 1, 1)
        self.label_pwd = QtWidgets.QLabel(self.widget_center)
        self.label_pwd.setMinimumSize(QtCore.QSize(0, 40))
        self.label_pwd.setObjectName("label_pwd")
        self.gridLayout.addWidget(self.label_pwd, 2, 0, 1, 1)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget_center)
        self.lineEdit_pwd.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.gridLayout.addWidget(self.lineEdit_pwd, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 40)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_login = QtWidgets.QPushButton(self.widget_center)
        self.pushButton_login.setEnabled(False)
        self.pushButton_login.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout_2.addWidget(self.pushButton_login)
        self.pushButton_exit = QtWidgets.QPushButton(self.widget_center)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_2.addWidget(self.pushButton_exit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget_center)
        self.widget_right = QtWidgets.QWidget(Form_Login)
        self.widget_right.setObjectName("widget_right")
        self.horizontalLayout.addWidget(self.widget_right)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(Form_Login)
        QtCore.QMetaObject.connectSlotsByName(Form_Login)

    def retranslateUi(self, Form_Login):
        _translate = QtCore.QCoreApplication.translate
        Form_Login.setWindowTitle(_translate("Form_Login", "智能运行支持系统"))
        self.label_username.setText(_translate("Form_Login", "用户名"))
        self.label_pwd.setText(_translate("Form_Login", "密  码"))
        self.pushButton_login.setText(_translate("Form_Login", "登    录"))
        self.pushButton_exit.setText(_translate("Form_Login", "退  出"))
import Login_rc
