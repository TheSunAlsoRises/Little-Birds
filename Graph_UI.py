# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\Graph_UI.ui'
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
        self.next_button.setGeometry(QtCore.QRect(310, 250, 75, 23))
        self.next_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(0, 0, 401, 51))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.next_button.setText(_translate("Form", "Next", None))
        self.back_button.setText(_translate("Form", "Home", None))
        self.headline.setText(_translate("Form", "Title", None))

