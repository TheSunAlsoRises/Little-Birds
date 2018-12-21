# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\UI\ManagerMenu.ui'
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
        Form.resize(400, 301)
        self.logout_button = QtGui.QPushButton(Form)
        self.logout_button.setGeometry(QtCore.QRect(120, 180, 151, 23))
        self.logout_button.setObjectName(_fromUtf8("logout_button"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(20, 260, 71, 23))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.upload_data_button = QtGui.QPushButton(Form)
        self.upload_data_button.setGeometry(QtCore.QRect(120, 120, 151, 23))
        self.upload_data_button.setObjectName(_fromUtf8("upload_data_button"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(130, 60, 131, 16))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.logout_button.setText(_translate("Form", "Logout", None))
        self.back_button.setText(_translate("Form", "Back", None))
        self.upload_data_button.setText(_translate("Form", "Upload Data (override)", None))
        self.headline.setText(_translate("Form", "Choose an option", None))

