import sys
from PyQt4 import QtCore, QtGui
from MainPage import Ui_MainWindow

class MainPage(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.helloworld)


    def helloworld(self):
        self.ui.textEdit.setText("hell")
        print('fef')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainPage()
    myapp.show()
    sys.exit(app.exec_())
