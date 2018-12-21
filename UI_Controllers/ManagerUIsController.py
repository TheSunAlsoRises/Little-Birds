import sys, os
import MainPage ,Login, ManagerMenu, Graph, UploadFrame, FileUploadDandD, ErrorMessage
import ScriptFilesController, DBconnect, CleaningTweetsController, AnalysisController
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QWidget, QMessageBox
from PyQt4 import QtGui, QtCore

from PyQt4.QtCore import QThread, SIGNAL


class tweetsThread(QThread):

    def __init__(self, urls):
        QThread.__init__(self)
        self.urls = urls

    def __del__(self):
        self.wait()

    def run(self):
        #  Truncate all the existing tweets
        DBconnect.DBconnect.send_query("truncate table littlebirds.tweet")
        # Call function to upload the tweets
        for url in self.urls:
            DBconnect.DBconnect.upload_tweets_file(url)
        # Clean the tweets
        CleaningTweetsController.CleaningTweetsController.cleanTweets()
        # Analyze them
        AnalysisController.AnalysisController.analyze_tweets_by_episode()


class scriptsThread(QThread):

    def __init__(self, urls):
        QThread.__init__(self)
        self.urls = urls

    def __del__(self):
        self.wait()

    def run(self):
        # Truncate all the existing scriptlines
        DBconnect.DBconnect.send_query("truncate table littlebirds.scriptline")
        # Call function to upload the scripts
        for url in self.urls:
            ScriptFilesController.ScriptFilesController.file_to_scriptLines(url, int((url[-5:])[:1]))
        AnalysisController.AnalysisController.analyze_scriptlines_by_script()


class MainPageUI(QWidget):
    def __init__(self, parent=None):
        super(MainPageUI, self).__init__(parent)
        self.ui = MainPage.Ui_Form()
        self.ui.setupUi(self)


class LoginUI(QWidget):
    def __init__(self, parent=None):
        super(LoginUI, self).__init__(parent)
        self.ui = Login.Ui_Form()
        self.ui.setupUi(self)


class ManagerMenuUI(QWidget):
    def __init__(self, parent=None):
        super(ManagerMenuUI, self).__init__(parent)
        self.ui = ManagerMenu.Ui_Form()
        self.ui.setupUi(self)


class UploadUI(QWidget):
    def __init__(self, parent=None):
        super(UploadUI, self).__init__(parent)
        self.ui = UploadFrame.Ui_Form()
        self.ui.setupUi(self)


class ErrorMessageUI (QWidget):
    def __init__(self, parent=None):
        super(ErrorMessageUI, self).__init__(parent)
        self.ui = ErrorMessage.Ui_Form()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):

    # Determines whether the user chose to upload scripts or tweets files
    uploadScriptsStatus = 0
    uploadTweetsStatus = 0

    # Paths to files that the manager uploads
    urlsList = list()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(400, 350)
        self.startMainPageUI()
        #self.startErrorMessageUI()
        #self.startUploadUI()
        #self.startGraphUI()

    def startMainPageUI(self):
        self.Window = MainPageUI(self)
        self.setWindowTitle("Main Page")
        self.setCentralWidget(self.Window)
        # self.Window.CPSBTN.clicked.connect(self.startManagerMenuUI)
        # if not logged in:
        self.Window.ui.manager_area_button.clicked.connect(self.startLoginUI)
        #else:
        #self.Window.ui.manager_area_button.clicked.connect(self.startManagerMenuUI)
        # Show Graph:
        #self.Window.ui.manager_area_button.clicked.connect(self.startGraphUI)
        #self.ui = Login.Ui_Form()
        self.show()

    def startManagerMenuUI(self):
        self.Window = ManagerMenuUI(self)
        self.setWindowTitle("Manager Menu")
        self.setCentralWidget(self.Window)
        #self.Window.CPSBTN.clicked.connect(self.startLoginUI)
        self.Window.ui.back_button.clicked.connect(self.startMainPageUI)
        #TODO: self.Window.ui.logout_button.clicked.connect(Logout method, and then call self.startMainPageUI)
        self.Window.ui.logout_button.clicked.connect(self.startMainPageUI)
        self.Window.ui.upload_data_button.clicked.connect(self.uploadTweets)
        #self.Window.ui.upload_scripts_button.clicked.connect(self.uploadScripts)
        self.show()

    def startLoginUI(self):
        self.Window = LoginUI(self)
        self.setWindowTitle("Login")
        self.setCentralWidget(self.Window)
        #self.Window.CPSBTN.clicked.connect(self.startManagerMenuUI)
        self.Window.ui.next_button.clicked.connect(self.startManagerMenuUI)
        self.Window.ui.back_button.clicked.connect(self.startMainPageUI)
        #self.ui = Login.Ui_Form()
        self.show()

    def startGraphUI(self):
        self.Window = Graph.GraphUI(self)
        self.setCentralWidget(self.Window)
        # Hide the main program window
        self.hide()
        # Show the graph window
        self.Window.show()
        #self.Window.CPSBTN.clicked.connect(self.startManagerMenuUI)

    def uploadScripts(self):
        self.uploadTweetsStatus = 0
        self.uploadScriptsStatus = 1
        self.setWindowTitle("Upload Scripts")
        self.startUploadUI()

    def uploadTweets(self):
        self.uploadScriptsStatus = 0
        self.uploadTweetsStatus = 1
        self.setWindowTitle("Upload Tweets")
        self.startUploadUI()

    def startUploadUI(self):
        self.Window = FileUploadDandD.TestListView(self)
        self.connect(self.Window, QtCore.SIGNAL("dropped"), self.pictureDropped)
        self.setCentralWidget(self.Window)
        #self.ui = UploadFrame.Ui_Form()
        #self.ui.setupUi(self)
        if self.uploadScriptsStatus == 1:
            # Disable Back option
            self.Window.ui.back_button.setDisabled(True)
        else:
            self.Window.ui.back_button.clicked.connect(self.upload_canceled)
        self.Window.ui.upload_button.clicked.connect(self.upload_requested)
        self.show()

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                print(url)
                self.urlsList.append(url)
                # Show images icons
                #icon = QtGui.QIcon(url)
                #pixmap = icon.pixmap(72, 72)
                #icon = QtGui.QIcon(pixmap)
                item = QtGui.QListWidgetItem(url, self.Window)
                #item.setIcon(icon)
                #item.setStatusTip(url)

    def upload_requested(self):
        #TODO: Check uploaded file and show success or rejection message - scriptline duplications?
        if len(self.urlsList) != 0 and self.uploadTweetsStatus == 1:
            for url in self.urlsList:
                # Check file type
                if url[-4:] != ".csv":
                    showdialog("Upload Rejected", "  Please upload CSV files only        ", 0)
                    self.urlsList = list()
                    self.startUploadUI()
                    return

            # Disable Back option
            self.Window.ui.back_button.setDisabled(True)
            # Show process message
            item = QtGui.QListWidgetItem("\n\n\nUploading, please wait . . .", self.Window)

            #thread_args = tuple()
            #thread_args.__add__(tuple(self.urlsList))
            #thread = Thread(target=self.threaded_function, args=(thread_args))
            #thread.start()
            #thread.join()

            self.thready_palavra = tweetsThread(self.urlsList)
            self.connect(self.thready_palavra, SIGNAL("finished()"), self.done)
            self.thready_palavra.start()

            # Clean the files list
            self.urlsList = list()

        elif len(self.urlsList) != 0 and self.uploadScriptsStatus == 1:
            for url in self.urlsList:
                # Check file type
                if url[-4:] != ".txt":
                    showdialog("Upload Rejected", "  Please upload TXT files only        ", 0)
                    self.urlsList = list()
                    self.startUploadUI()
                    return

                # Check file name format
                if str.isdigit((url[-5:])[:1]) == False or (url[-6:])[:1] != '/':
                    showdialog("Upload Rejected", "  File name must be a single digit,\n  that represents the script's number       ", 0)
                    self.urlsList = list()
                    self.startUploadUI()
                    return

            # Show process message
            item = QtGui.QListWidgetItem("\n\n\nUploading, please wait . . .", self.Window)

            self.thready_palavra = scriptsThread(self.urlsList)
            self.connect(self.thready_palavra, SIGNAL("finished()"), self.done)
            self.thready_palavra.start()

            # Clean the files list
            self.urlsList = list()

    def upload_canceled(self):
        self.startManagerMenuUI()

    def done(self):
        if self.uploadTweetsStatus == 1:
            text = "  The tweets were uploaded successfully        "
            self.uploadScripts()
        elif self.uploadScriptsStatus == 1:
            text = "  The scripts were uploaded successfully        "
            self.startManagerMenuUI()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Upload succeeded")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        return msg


def showdialog(title, text, status):
    msg = QMessageBox()
    if status == 0:
        msg.setIcon(QMessageBox.Critical)
    elif status == 1:
        msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    #msg.setInformativeText("This is additional information")
    msg.setWindowTitle(title)
    #msg.setDetailedText("The details are as follows:")
    #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setStandardButtons(QMessageBox.Ok)
    #msg.buttonClicked.connect(msgbtn)
    retval = msg.exec_()
    #print("value of pressed message box button:", retval)
    return msg
#def msgbtn(i):
    #print("Button pressed is:", i.text())


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
