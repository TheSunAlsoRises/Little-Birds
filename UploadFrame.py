# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\אליה\PycharmProjects\Little-Birds\UploadFrame.ui'
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
        Form.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 430, 411, 121))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter2 down.jpeg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.headline = QtGui.QLabel(Form)
        self.headline.setGeometry(QtCore.QRect(0, 40, 889, 151))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.headline.setFont(font)
        self.headline.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 0);"))
        self.headline.setAlignment(QtCore.Qt.AlignCenter)
        self.headline.setObjectName(_fromUtf8("headline"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, -10, 411, 231))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter2 up.jpg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(650, -10, 251, 551))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter2 right.jpeg")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(-10, -10, 251, 561))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("../pictures/winter2 left.jpeg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 201, 471))
        self.label_3.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(650, 40, 201, 471))
        self.label_7.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(240, 40, 410, 181))
        self.label_8.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_8.setLineWidth(0)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(240, 430, 411, 81))
        self.label_9.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,150);"))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.uploading_message = QtGui.QLabel(Form)
        self.uploading_message.setGeometry(QtCore.QRect(0, 140, 889, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Levenim MT"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.uploading_message.setFont(font)
        self.uploading_message.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255, 0);"))
        self.uploading_message.setAlignment(QtCore.Qt.AlignCenter)
        self.uploading_message.setObjectName(_fromUtf8("uploading_message"))
        self.filesList = QtGui.QListWidget(Form)
        self.filesList.setGeometry(QtCore.QRect(240, 360, 410, 85))
        self.filesList.setStyleSheet(_fromUtf8("background-color:  rgb(210,210,210,255);"))
        self.filesList.setFrameShape(QtGui.QFrame.NoFrame)
        self.filesList.setObjectName(_fromUtf8("filesList"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(239, 220, 8, 140))
        self.line.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(239, 352, 411, 8))
        self.line_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.line_2.setLineWidth(0)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(642, 220, 8, 140))
        self.line_3.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.line_3.setLineWidth(0)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(239, 220, 411, 8))
        self.line_4.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.line_4.setLineWidth(0)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
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
        self.upload_button = QtGui.QPushButton(Form)
        self.upload_button.setGeometry(QtCore.QRect(710, 370, 102, 102))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.upload_button.setFont(font)
        self.upload_button.setStyleSheet(_fromUtf8("background-color:  rgb(255,255,255,100);\n"
"\n"
""))
        self.upload_button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.upload_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../buttons/tran_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_button.setIcon(icon1)
        self.upload_button.setIconSize(QtCore.QSize(80, 80))
        self.upload_button.setObjectName(_fromUtf8("upload_button"))
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
        self.label_6.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.headline.raise_()
        self.uploading_message.raise_()
        self.filesList.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.back_button.raise_()
        self.upload_button.raise_()
        self.help_button.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.headline.setText(_translate("Form", "Drop the files below", None))
        self.uploading_message.setText(_translate("Form", " Drop the files below", None))
        self.help_button.setText(_translate("Form", "?", None))

