import sys
import LoginController, ManagerMenu, MainPage
import ManagerUIsController
from PyQt4 import QtCore, QtGui


class ManagerMenuWin (QtGui.QMainWindow):

    currentWindow = None
    formerWindow = None

    def __init__(self, parent):
        #super(ManagerMenuWin, self).__init__(parent)
        app = QtGui.QApplication(sys.argv)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def back(self):
        pass
        #app = QtGui.QApplication(sys.argv)

        # ManagerMenuWin.currentWindow.hide()
        # ManagerMenuWin.formerWindow = QtGui.QMainWindow()
        # myapp = ManagerUIsController.LoginWin(ManagerUIsController.LoginWin)
        # ui = MainPage.Ui_MainWindow()
        # ui = Login.Ui_Form()
        # ui.setupUi(ManagerMenuWin.formerWindow)
        # ManagerMenuWin.formerWindow.show()

    def uploadTweets (self):
        pass

    def uploadScripts (self):
        pass

    def logout (self):
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ManagerMenuWin.currentWindow = QtGui.QMainWindow()
    ui = ManagerMenu.Ui_Form()
    ui.setupUi(ManagerMenuWin.currentWindow)
    ui.back_button.clicked.connect(ManagerMenuWin.back)
    myapp = ManagerMenuWin(ManagerMenuWin)
    ManagerMenuWin.currentWindow.show()
    sys.exit(app.exec_())
