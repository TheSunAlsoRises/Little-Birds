# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\MainPage.ui'
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
        Form.resize(889, 541)
        Form.setStyleSheet(_fromUtf8(""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-120, 80, 531, 81))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("background-color:  rgb(0, 0, 0);\n"
"color: rgb(240, 240, 240);\n"
"font-size:50px;"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-150, -10, 1051, 561))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setToolTip(_fromUtf8(""))
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-70, 160, 421, 51))
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 172, 237)"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 200, 351, 51))
        self.label_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 172, 237)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.start_button = QtGui.QPushButton(Form)
        self.start_button.setGeometry(QtCore.QRect(90, 330, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(_fromUtf8("QPushButton\n"
"{ \n"
"background-color: 000000;\n"
"  color: black;\n"
"  border: 6px solid #00aced;\n"
"margin: 3px;\n"
"border-radius: 30px;\n"
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
"  border: 4px solid #00aced;\n"
"}\n"
"\n"
""))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.manager_area_button = QtGui.QPushButton(Form)
        self.manager_area_button.setGeometry(QtCore.QRect(115, 420, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.manager_area_button.setFont(font)
        self.manager_area_button.setStyleSheet(_fromUtf8("QPushButton\n"
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
        self.manager_area_button.setObjectName(_fromUtf8("manager_area_button"))
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
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.start_button.raise_()
        self.manager_area_button.raise_()
        self.help_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Little Birds", None))
        self.label_3.setText(_translate("Form", "What Twitter Feels ", None))
        self.label_4.setText(_translate("Form", "About #Game_of_Thrones", None))
        self.start_button.setText(_translate("Form", "Start", None))
        self.manager_area_button.setText(_translate("Form", "Manager area", None))
        self.help_button.setText(_translate("Form", "?", None))

