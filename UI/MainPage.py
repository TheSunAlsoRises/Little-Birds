# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\UI\MainPage.ui'
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
        Form.resize(400, 309)
        self.secondary_headline = QtGui.QLabel(Form)
        self.secondary_headline.setGeometry(QtCore.QRect(60, 110, 261, 41))
        self.secondary_headline.setAlignment(QtCore.Qt.AlignCenter)
        self.secondary_headline.setObjectName(_fromUtf8("secondary_headline"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(40, 20, 319, 121))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))
        self.start_button = QtGui.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(110, 200, 171, 41))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.manager_area_button = QtGui.QPushButton(Form)
        self.manager_area_button.setGeometry(QtCore.QRect(150, 260, 91, 23))
        self.manager_area_button.setObjectName(_fromUtf8("manager_area_button"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.secondary_headline.setText(_translate("Form", "What Twitter feels about #Game_of_Thrones", None))
        self.headline.setText(_translate("Form", "Little Birds", None))
        self.start_button.setText(_translate("Form", "Start", None))
        self.manager_area_button.setText(_translate("Form", "Manager area", None))

