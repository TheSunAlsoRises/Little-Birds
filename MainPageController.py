import sys
import ManagerUIsController
from PyQt4 import QtCore, QtGui
from MainPage import Ui_MainWindow


class MainPageWin (QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.manager_area_button.clicked.connect(self.manager_area)
        #ManagerUIsController._Login = ManagerUIsController.Login

    def manager_area(self):
        self.hide()
        #if ManagerUIsController.Login is None:
            #self._Login = ManagerUIsController.Login(self)
        #ManagerUIsController.Login.show()
        pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainPageWin()
    myapp.show()
    sys.exit(app.exec_())
