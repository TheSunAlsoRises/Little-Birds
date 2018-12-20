# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\UI\Login.ui'
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
        Form.resize(401, 300)
        self.next_button = QtGui.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.password_input = QtGui.QPlainTextEdit(Form)
        self.password_input.setGeometry(QtCore.QRect(190, 190, 104, 31))
        self.password_input.setPlainText(_fromUtf8(""))
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.username_input = QtGui.QPlainTextEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(190, 130, 104, 31))
        self.username_input.setPlainText(_fromUtf8(""))
        self.username_input.setObjectName(_fromUtf8("username_input"))
        self.username_label = QtGui.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(110, 140, 47, 13))
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.password_label = QtGui.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(110, 200, 47, 13))
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(110, 60, 181, 20))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.next_button.setText(_translate("Form", "Next", None))
        self.back_button.setText(_translate("Form", "Back", None))
        self.username_label.setText(_translate("Form", "Username", None))
        self.password_label.setText(_translate("Form", "Password", None))
        self.headline.setText(_translate("Form", "Please login to continue", None))

