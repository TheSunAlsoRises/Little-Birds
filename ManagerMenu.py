# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\ManagerMenu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(891, 541)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -10, 921, 561))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter2.jpeg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 811, 471))
        self.label_2.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.headline_2 = QtGui.QLabel(Form)
        self.headline_2.setGeometry(QtCore.QRect(0, 40, 891, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.headline_2.setFont(font)
        self.headline_2.setAlignment(QtCore.Qt.AlignCenter)
        self.headline_2.setObjectName(_fromUtf8("headline_2"))
        self.upload_data_button = QtGui.QPushButton(Form)
        self.upload_data_button.setGeometry(QtCore.QRect(350, 190, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.upload_data_button.setFont(font)
        self.upload_data_button.setStyleSheet(_fromUtf8("QPushButton\n"
"{ \n"
"background-color: 000000;\n"
"  color: black;\n"
"  border: 6px solid #00aced;\n"
"margin: 3px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: #111111;\n"
"  color: white;\n"
"}\n"
"\n"
"\n"
""))
        self.upload_data_button.setObjectName(_fromUtf8("upload_data_button"))
        self.logout_button = QtGui.QPushButton(Form)
        self.logout_button.setGeometry(QtCore.QRect(350, 330, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet(_fromUtf8("QPushButton:hover\n"
"{\n"
"  background-color: #111111;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"background-color: 000000;\n"
"  color: black;\n"
"  border: 6px solid #00aced;\n"
"margin: 3px;\n"
"}"))
        self.logout_button.setObjectName(_fromUtf8("logout_button"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(80, 370, 102, 102))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,100);\n"
"\n"
""))
        self.back_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../buttons/icons8-reply-arrow-100.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QtCore.QSize(80, 80))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.help_button = QtGui.QPushButton(Form)
        self.help_button.setGeometry(QtCore.QRect(800, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.help_button.setFont(font)
        self.help_button.setStyleSheet(_fromUtf8("QPushButton\n"
"{ \n"
"background-color: 000000;\n"
"  color: black;\n"
"  border: 4px solid #00aced;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: #111111;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #111111;\n"
"  color: white;\n"
"  border: 2.666px solid #00aced;\n"
"}\n"
""))
        self.help_button.setObjectName(_fromUtf8("help_button"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.headline_2.setText(_translate("Form", "Choose an option", None))
        self.upload_data_button.setText(_translate("Form", "Upload Data \n"
"(override)", None))
        self.logout_button.setText(_translate("Form", "Logout", None))
        self.help_button.setText(_translate("Form", "?", None))

