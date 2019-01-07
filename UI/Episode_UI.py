# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\UI\Episode_UI.ui'
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
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.next_button = QtGui.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.next_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 130, 181, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(110, 60, 181, 20))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.back_button.setText(_translate("Form", "Back", None))
        self.next_button.setText(_translate("Form", "Next", None))
        self.comboBox.setItemText(0, _translate("Form", "#1   Dragonstone", None))
        self.comboBox.setItemText(1, _translate("Form", "#2   Stormborn", None))
        self.comboBox.setItemText(2, _translate("Form", "#3   The Queen\'\'s Justice", None))
        self.comboBox.setItemText(3, _translate("Form", "#4   The Spoils of War", None))
        self.comboBox.setItemText(4, _translate("Form", "#5   Eastwatch", None))
        self.comboBox.setItemText(5, _translate("Form", "#6   Beyond the Wall", None))
        self.comboBox.setItemText(6, _translate("Form", "#7   The Dragon and the Wolf", None))
        self.headline.setText(_translate("Form", "Choose an episode", None))

