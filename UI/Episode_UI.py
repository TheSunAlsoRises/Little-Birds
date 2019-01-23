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
        Form.resize(891, 541)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(300, 270, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("background-color:  rgb(250,250,250);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(0, 40, 891, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, 0, 921, 611))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter1.jpeg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 811, 471))
        self.label_2.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.next_button = QtGui.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(720, 370, 102, 102))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.next_button.setFont(font)
        self.next_button.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,100);\n"
"\n"
""))
        self.next_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.next_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../buttons/tran_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon)
        self.next_button.setIconSize(QtCore.QSize(80, 80))
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(70, 370, 102, 102))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,100);\n"
"\n"
""))
        self.back_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../buttons/icons8-reply-arrow-100.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QtCore.QSize(80, 80))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.label.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.headline.raise_()
        self.next_button.raise_()
        self.back_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.comboBox.setItemText(0, _translate("Form", "#1   Dragonstone", None))
        self.comboBox.setItemText(1, _translate("Form", "#2   Stormborn", None))
        self.comboBox.setItemText(2, _translate("Form", "#3   The Queen\'\'s Justice", None))
        self.comboBox.setItemText(3, _translate("Form", "#4   The Spoils of War", None))
        self.comboBox.setItemText(4, _translate("Form", "#5   Eastwatch", None))
        self.comboBox.setItemText(5, _translate("Form", "#6   Beyond the Wall", None))
        self.comboBox.setItemText(6, _translate("Form", "#7   The Dragon and the Wolf", None))
        self.headline.setText(_translate("Form", "Choose an episode", None))

