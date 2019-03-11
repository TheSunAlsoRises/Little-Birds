# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\House.ui'
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
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 190, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -10, 921, 621))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter1.jpeg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(200, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(520, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 811, 471))
        self.label_3.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(390, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(10, 40, 891, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))
        self.back_button = QtGui.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(70, 370, 102, 102))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../buttons/tran_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon1)
        self.next_button.setIconSize(QtCore.QSize(80, 80))
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.label.raise_()
        self.label_3.raise_()
        self.headline.raise_()
        self.label_2.raise_()
        self.checkBox.raise_()
        self.checkBox_3.raise_()
        self.checkBox_2.raise_()
        self.back_button.raise_()
        self.next_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Select a house:", None))
        self.checkBox.setText(_translate("Form", " Lannister", None))
        self.checkBox_3.setText(_translate("Form", " Targaryen", None))
        self.checkBox_2.setText(_translate("Form", " Stark", None))
        self.headline.setText(_translate("Form", "Who do you stand with?", None))

