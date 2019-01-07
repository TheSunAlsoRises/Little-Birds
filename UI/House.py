# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\UI\House.ui'
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
        Form.resize(400, 300)
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 170, 71, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(80, 170, 71, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 170, 61, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(110, 60, 181, 20))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.next_button = QtGui.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.next_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 120, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.checkBox_3.setText(_translate("Form", "Targaryen", None))
        self.checkBox.setText(_translate("Form", "Lannister", None))
        self.checkBox_2.setText(_translate("Form", "Stark", None))
        self.headline.setText(_translate("Form", "Who do you stand with?", None))
        self.back_button.setText(_translate("Form", "Back", None))
        self.next_button.setText(_translate("Form", "Next", None))
        self.label.setText(_translate("Form", "Select a house:", None))

