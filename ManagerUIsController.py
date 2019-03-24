import sys, os
import MainPage, Login, ManagerMenu, Graph, UploadFrame, FileUploadDandD, Episode_UI, Category, Character, Location, House, ErrorMessage
import ScriptFilesController, DBconnect, CleaningTweetsController, AnalysisController, TweetsSummingController, LoginController
import ScriptlinesSummingController
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, QWidget, QMessageBox
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QThread, SIGNAL


class TweetsThread(QThread):

    def __init__(self, urls):
        QThread.__init__(self)
        self.urls = urls

    def __del__(self):
        self.wait()

    def run(self):
        #  Truncate all the existing tweets
        # leave it out for now so we can add the files one by one
        # TODO:
#        DBconnect.DBconnect.send_query("truncate table littlebirds.tweet")
        # Call function to upload the tweets
        for url in self.urls:
            DBconnect.DBconnect.upload_tweets_file(url)
        # Clean the tweets
        CleaningTweetsController.CleaningTweetsController.cleanTweets()
        # Analyze them
        AnalysisController.AnalysisController.analyze_tweets_by_episode()


class ScriptsThread(QThread):

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


class SummingThread(QThread):

    tweetsSum = ""

    def __init__(self, parameters):
        QThread.__init__(self)
        self.parameters = parameters

    def __del__(self):
        self.wait()

    def run(self):
        # Call function to sum the relevant tweets
        self.tweetsSummingObj = TweetsSummingController.TweetsSummingController(self.parameters)
        Graph.GraphUI.tweetsSum = self.tweetsSummingObj.tweetsSumming()

        if Graph.GraphUI.tweetsSum is not None:
            # Noramlize the result as percents:
            maximal_value = max(Graph.GraphUI.tweetsSum[0])
            if maximal_value == 0:  # Never divide by zero!
                maximal_value = 0.1

            for i in range(8):
                Graph.GraphUI.tweetsSum[0][i] = (Graph.GraphUI.tweetsSum[0][i] / maximal_value) * 100
                # Raise it up a little, '0' value can make close values barely seen
                if Graph.GraphUI.tweetsSum[0][i] == 0:
                    Graph.GraphUI.tweetsSum[0][i] = 2.5

                print(Graph.GraphUI.tweetsSum[0][i])

            print(Graph.GraphUI.tweetsSum[1])
            print(Graph.GraphUI.tweetsSum[2])

        # Call function to sum the relevant scriptlines
        self.scriptlinesSummingObj = ScriptlinesSummingController.ScriptlinesSummingController(self.parameters)
        Graph.GraphUI.scriptsSum = self.scriptlinesSummingObj.scriptlinesSumming()

        if Graph.GraphUI.scriptsSum is not None:

            # Noramlize the result as percents:
            maximal_value = max(Graph.GraphUI.scriptsSum[0])
            if maximal_value == 0:  # Never divide by zero!
                maximal_value = 0.1

            for i in range(8):
                Graph.GraphUI.scriptsSum[0][i] = (Graph.GraphUI.scriptsSum[0][i] / maximal_value) * 100
                # Raise it up a little, '0' value can make close values barely seen
                if Graph.GraphUI.scriptsSum[0][i] == 0:
                    Graph.GraphUI.scriptsSum[0][i] = 2.5

                print(Graph.GraphUI.scriptsSum[0][i])

            print(Graph.GraphUI.scriptsSum[1])
            print(Graph.GraphUI.scriptsSum[2])


class MainPageUI(QWidget):
    def __init__(self, parent=None):
        super(MainPageUI, self).__init__(parent)
        self.ui = MainPage.Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet("background-image: url(craw.jpg); background-attachment: fixed")


class EpisodeUI(QWidget):
    def __init__(self, parent=None):
        super(EpisodeUI, self).__init__(parent)
        self.ui = Episode_UI.Ui_Form()
        self.ui.setupUi(self)


class CategoryUI(QWidget):
    def __init__(self, parent=None):
        super(CategoryUI, self).__init__(parent)
        self.ui = Category.Ui_Form()
        self.ui.setupUi(self)


class CharacterUI(QWidget):
    def __init__(self, parent=None):
        super(CharacterUI, self).__init__(parent)
        self.ui = Character.Ui_Form()
        self.ui.setupUi(self)


class LocationUI(QWidget):
    def __init__(self, parent=None):
        super(LocationUI, self).__init__(parent)
        self.ui = Location.Ui_Form()
        self.ui.setupUi(self)


class HouseUI(QWidget):
    def __init__(self, parent=None):
        super(HouseUI, self).__init__(parent)
        self.ui = House.Ui_Form()
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
    urlsList = None

    # Current user details
    username = ""

    # Selection parameters
    parameters = None
    episode = None
    episode_text = None
    category = None
    character = None
    character_text = None
    location = None
    location_text = None
    house = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setFixedSize(891, 541)
        #self.adjustSize()

        # Center the window in the screen
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        # another way - takes the screen a little lower
        #self.move(QtGui.QApplication.desktop().screen().rect().center() - self.rect().center())

        #self.setGeometry(400,50,50,0)

        self.startMainPageUI()

    def startMainPageUI(self):
        self.Window = MainPageUI(self)
        self.setWindowTitle("Main Page")
        self.setCentralWidget(self.Window)
        self.Window.ui.label_2.setStyleSheet("background-image: url(./pictures/craw.jpg);")
        # self.Window.CPSBTN.clicked.connect(self.startManagerMenuUI)

        # Set buttons destinations:
        self.Window.ui.start_button.clicked.connect(self.startEpisodeUI)
        login_status = LoginController.LoginController.isLoggedIn(self.username)
        if login_status == -1:
            self.Window.ui.manager_area_button.clicked.connect(self.startLoginUI)
        elif login_status == 1:
            self.Window.ui.manager_area_button.clicked.connect(self.startManagerMenuUI)

        # Give the graph a reference of the window
        Graph.GraphUI.window = self

        self.show()

    def startEpisodeUI(self):
        self.Window = EpisodeUI(self)
        self.setWindowTitle("Little Birds")
        self.setCentralWidget(self.Window)
        #self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter1.jpeg);")
        self.Window.ui.label.setStyleSheet("background-image: url(:buttons/winter1.jpeg);")
        self.Window.ui.next_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/tran_right.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.next_button.clicked.connect(lambda:self.saveEpisodeSelection("next"))
        self.Window.ui.back_button.clicked.connect(lambda:self.saveEpisodeSelection("back"))
        # Show current chosen episode
        if self.episode is not None:
            self.Window.ui.comboBox.setCurrentIndex(self.episode - 1)
        self.show()

    def saveEpisodeSelection(self, direction):
        # Save the number of the chosen episode
        self.episode = self.Window.ui.comboBox.currentIndex() + 1
        self.episode_text = self.Window.ui.comboBox.currentText()[5:]
        print("Chosen episode: " + str(self.episode))
        if direction == "next":
            self.startCategoryUI()
        elif direction == "back":
            self.startMainPageUI()

    def startCategoryUI(self):
        self.Window = CategoryUI(self)
        self.setWindowTitle("Little Birds")
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter1.jpeg);")
        self.Window.ui.next_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/tran_right.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.next_button.setDisabled(True)
        self.Window.ui.back_button.clicked.connect(self.startEpisodeUI)
        # Make the checkBoxes mutually exclusive
        self.bgCategory = QButtonGroup()
        self.bgCategory.addButton(self.Window.ui.checkBox, 1)
        self.bgCategory.addButton(self.Window.ui.checkBox_2, 2)
        self.bgCategory.addButton(self.Window.ui.checkBox_3, 3)
        # Show current selection
        if self.category == "Character":
            self.Window.ui.checkBox.setChecked(True)
            self.Window.ui.next_button.clicked.connect(self.startCharacterUI)
            self.Window.ui.next_button.setEnabled(True)
        else:
            self.Window.ui.checkBox.setChecked(False)
        if self.category == "House":
            self.Window.ui.checkBox_2.setChecked(True)
            self.Window.ui.next_button.clicked.connect(self.startHouseUI)
            self.Window.ui.next_button.setEnabled(True)
        else:
            self.Window.ui.checkBox_2.setChecked(False)
        if self.category == "Location":
            self.Window.ui.checkBox_3.setChecked(True)
            self.Window.ui.next_button.clicked.connect(self.startLocationUI)
            self.Window.ui.next_button.setEnabled(True)
        else:
            self.Window.ui.checkBox_3.setChecked(False)
        self.Window.ui.checkBox.stateChanged.connect(lambda:self.saveCategorySelection(1))
        self.Window.ui.checkBox_2.stateChanged.connect(lambda:self.saveCategorySelection(2))
        self.Window.ui.checkBox_3.stateChanged.connect(lambda:self.saveCategorySelection(3))
        self.show()

    def saveCategorySelection(self, id):
        # Save the chosen category
        if id == 1:
            self.category = "Character"
            self.Window.ui.next_button.clicked.connect(self.startCharacterUI)
        elif id == 2:
            self.category = "House"
            self.Window.ui.next_button.clicked.connect(self.startHouseUI)
        elif id == 3:
            self.category = "Location"
            self.Window.ui.next_button.clicked.connect(self.startLocationUI)
        print("Chosen category: " + self.category)
        self.Window.ui.next_button.setEnabled(True)

    def startCharacterUI(self):
        self.Window = CharacterUI(self)
        self.setWindowTitle("Little Birds")
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter1.jpeg);")
        self.Window.ui.next_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/tran_right.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.next_button.clicked.connect(lambda:self.saveCharacterSelection("next"))
        self.Window.ui.back_button.clicked.connect(lambda:self.saveCharacterSelection("back"))

        # Get options from DB
        q = '"'
        query_string = "SELECT CharacterName FROM littlebirds.category where CategoryName = " + q + "character" + q
        result = DBconnect.DBconnect.tuple_to_list(query_string)
        for name in result:
            name[0] = name[0][0].upper() + name[0][1:]
            lastNameIndex = name[0].find(" ") + 1
            name[0] = name[0][:lastNameIndex] + name[0][lastNameIndex].upper() + name[0][lastNameIndex+1:]
            self.Window.ui.comboBox.addItem(name[0])

        # Show current chosen character
        if self.character is not None:
            self.Window.ui.comboBox.setCurrentIndex(self.character)
        self.show()

    def saveCharacterSelection(self, direction):
        # Save the chosen character
        self.character = self.Window.ui.comboBox.currentIndex()
        self.character_text = self.Window.ui.comboBox.currentText().lower()
        self.location = None
        self.location_text = None
        self.house = None
        print("Chosen character: " + self.character_text + ",  Index: " + str(self.character))
        if direction == "next":
            self.sumData()
        elif direction == "back":
            self.startCategoryUI()

    def startLocationUI(self):
        self.Window = LocationUI(self)
        self.setWindowTitle("Little Birds")
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter1.jpeg);")
        self.Window.ui.next_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/tran_right.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.next_button.clicked.connect(lambda:self.saveLocationSelection("next"))
        self.Window.ui.back_button.clicked.connect(lambda:self.saveLocationSelection("back"))

        # Get options from DB
        q = '"'
        query_string = "SELECT LocationName FROM littlebirds.category where CategoryName = " + q + "location" + q
        result = DBconnect.DBconnect.tuple_to_list(query_string)
        for name in result:
            name[0] = (name[0])[0].upper() + (name[0])[1:]
            self.Window.ui.comboBox.addItem(name[0])

        # Show current chosen location
        if self.location is not None:
            self.Window.ui.comboBox.setCurrentIndex(self.location)
        self.show()

    def saveLocationSelection(self, direction):
        # Save the chosen location
        self.location = self.Window.ui.comboBox.currentIndex()
        self.location_text = self.Window.ui.comboBox.currentText().lower()
        self.character = None
        self.character_text = None
        self.house = None
        print("Chosen location: " + self.location_text + ",  Index: " + str(self.location))
        if direction == "next":
            self.sumData()
        elif direction == "back":
            self.startCategoryUI()

    def startHouseUI(self):
        self.flag = 0

        self.Window = HouseUI(self)
        self.setWindowTitle("Little Birds")
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter1.jpeg);")
        self.Window.ui.next_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/tran_right.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.next_button.setDisabled(True)
        self.Window.ui.back_button.clicked.connect(self.startCategoryUI)
        # Make the checkBoxes mutually exclusive
        self.bgHouse = QButtonGroup()
        self.bgHouse.addButton(self.Window.ui.checkBox, 1)
        self.bgHouse.addButton(self.Window.ui.checkBox_2, 2)
        self.bgHouse.addButton(self.Window.ui.checkBox_3, 3)
        # Show current selection
        if self.house == "Lannister":
            self.Window.ui.checkBox.setChecked(True)
            self.Window.ui.next_button.setDisabled(False)
        else:
            self.Window.ui.checkBox.setChecked(False)
        if self.house == "Stark":
            self.Window.ui.checkBox_2.setChecked(True)
            self.Window.ui.next_button.setDisabled(False)
        else:
            self.Window.ui.checkBox_2.setChecked(False)
        if self.house == "Targaryen":
            self.Window.ui.checkBox_3.setChecked(True)
            self.Window.ui.next_button.setDisabled(False)
        else:
            self.Window.ui.checkBox_3.setChecked(False)
        self.Window.ui.checkBox.stateChanged.connect(lambda: self.saveHouseSelection(1))
        self.Window.ui.checkBox_2.stateChanged.connect(lambda: self.saveHouseSelection(2))
        self.Window.ui.checkBox_3.stateChanged.connect(lambda: self.saveHouseSelection(3))
        self.show()

    def saveHouseSelection(self, id):
        # Save the chosen house
        if id == 1:
            self.house = "Lannister"
        elif id == 2:
            self.house = "Stark"
        elif id == 3:
            self.house = "Targaryen"
        self.character = None
        self.character_text = None
        self.location = None
        self.location_text = None
        print("Chosen house: " + self.house)
        self.Window.ui.next_button.setDisabled(False)
        self.Window.ui.next_button.clicked.connect(self.sumData)

    def sumData(self):
        self.parameters = list()
        self.parameters.insert(0, self.episode)
        self.parameters.insert(1, None)
        self.parameters.insert(2, self.category.lower())

        if self.category == "Character":
            self.parameters.insert(3, self.character_text.lower())
            self.Window.ui.comboBox.hide()

        if self.category == "House":
            self.parameters.insert(3, self.house.lower())
            self.Window.ui.checkBox.hide()
            self.Window.ui.checkBox_2.hide()
            self.Window.ui.checkBox_3.hide()

        if self.category == "Location":
            self.parameters.insert(3, self.location_text.lower())
            self.Window.ui.comboBox.hide()

        self.Window.ui.label_2.hide()
        self.Window.ui.back_button.hide()
        self.Window.ui.next_button.hide()

        # Show process message
        self.Window.ui.headline.setText("Collecting data, please wait . . .")

        self.thready_palavra = SummingThread(self.parameters)
        self.connect(self.thready_palavra, SIGNAL("finished()"), self.startGraphUI)
        self.thready_palavra.start()

    def startGraphUI(self):
        self.Window = Graph.GraphUI(self)
        self.setCentralWidget(self.Window)
        # Hide the main program window
        self.hide()
        # Show the graph window
        self.Window.show()
        #self.Window.CPSBTN.clicked.connect(self.startManagerMenuUI)

    def startLoginUI(self):
        self.Window = LoginUI(self)
        self.setWindowTitle("Login")
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter2.jpeg);")
        self.Window.ui.next_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/tran_right.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.next_button.clicked.connect(self.login)
        self.Window.ui.back_button.clicked.connect(self.startMainPageUI)
        self.show()

    def login(self):
        login_result = LoginController.LoginController.login(self.Window.ui.username_input.toPlainText(),
                                                             self.Window.ui.password_input.toPlainText())
        if login_result[0] == 1:
            self.username = login_result[1]
            self.startManagerMenuUI()

        elif login_result[0] == -1:
            text = "  Failed to login\n" \
                   "  Please check your input and try again       "
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(text)
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            return msg

    def startManagerMenuUI(self):
        self.Window = ManagerMenuUI(self)
        self.setWindowTitle("Manager Menu")
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter2.jpeg);")
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))
        self.Window.ui.back_button.clicked.connect(self.startMainPageUI)
        self.Window.ui.logout_button.clicked.connect(self.logout)
        self.Window.ui.upload_data_button.clicked.connect(self.uploadTweets)
        self.show()

    def logout(self):
        self.username = ""
        pass

        self.startMainPageUI()

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
        self.connect(self.Window, QtCore.SIGNAL("dropped"), self.fileDropped)
        self.setCentralWidget(self.Window)
        self.Window.ui.label.setStyleSheet("background-image: url(./pictures/winter2 down.jpeg);")
        self.Window.ui.label_6.setStyleSheet("background-image: url(./pictures/winter2 left.jpeg);")
        self.Window.ui.label_5.setStyleSheet("background-image: url(./pictures/winter2 right.jpeg);")
        self.Window.ui.label_4.setStyleSheet("background-image: url(./pictures/winter2 up.jpg);")
        self.Window.ui.upload_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-upload-100.png')))
        self.Window.ui.back_button.setIcon(QtGui.QIcon(QtGui.QPixmap('./buttons/icons8-reply-arrow-100.png')))

        if self.uploadScriptsStatus == 1:
            # Scripts:
            # Disable Back option
            self.Window.ui.back_button.setDisabled(True)
            # Set proper headline
            self.Window.ui.headline.setText("Drop the script files below")
        else:
            # Tweets:
            self.Window.ui.back_button.clicked.connect(self.upload_canceled)
            self.Window.ui.headline.setText("Drop the tweets files below")
        self.Window.ui.upload_button.clicked.connect(self.upload_requested)
        self.Window.ui.uploading_message.setText("")
        # Initialize an empty list
        self.urlsList = list()
        self.show()

    def fileDropped(self, l):
        for url in l:
            if os.path.exists(url):
                print(url)
                self.urlsList.append(url)
                # Show images icons
                #icon = QtGui.QIcon(url)
                #pixmap = icon.pixmap(72, 72)
                #icon = QtGui.QIcon(pixmap)

                #self.Window.ui.filesList.move(241, 221)
                #self.Window.ui.filesList.setMaximumHeight(17 * 4)
                #self.Window.ui.filesList.setMaximumWidth(411)

                # hererererere
                #self.Window.ui.filesList.setGeometry(240, 360, 410, 85)

                #self.Window.ui.filesList.setStyleSheet("    ")

                # writes on the window itself, covered by the labels...
                item = QtGui.QListWidgetItem(url, self.Window.ui.filesList)

                # item = QtGui.QLabel(url)
                # #item.move(221,241)
                # item.move(500,500)
                # item.setMaximumWidth(411)
                # item.setMaximumHeight(211)
                # item.setStyleSheet("background-color: rgb(29, 202, 255);"
                #                           "color: rgb(200, 100, 100);"
                #                           "margin-top: 15px; margin-bottom: 5px; margin-right: 15px; margin-left: 15px;"
                #                           "padding: 15px;"
                #                           "font-size: 18px;")

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
            self.Window.ui.uploading_message.setText("Uploading, please wait . . .")

            #thread_args = tuple()
            #thread_args.__add__(tuple(self.urlsList))
            #thread = Thread(target=self.threaded_function, args=(thread_args))
            #thread.start()
            #thread.join()

            self.thready_palavra = TweetsThread(self.urlsList)
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

            self.thready_palavra = ScriptsThread(self.urlsList)
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
