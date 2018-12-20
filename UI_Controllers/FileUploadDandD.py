import sys
import os
from PyQt4 import QtGui, QtCore
import UploadFrame, ManagerUIsController


class TestListView(QtGui.QListWidget):
    def __init__(self, type, parent=None):
        super(TestListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QtCore.QSize(72, 72))
        self.ui = UploadFrame.Ui_Form()
        self.ui.setupUi(self)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.ignore()

class FileUploadDandD():
    pass
    # def upload_requested(self, win):
    #     win.startManagerMenuUI()
    #
    # def upload_canceled(self, win):
    #     win.startManagerMenuUI()


# class MainForm(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(MainForm, self).__init__(parent)
#
#         self.view = TestListView(self)
#         self.connect(self.view, QtCore.SIGNAL("dropped"), self.pictureDropped)
#         self.setCentralWidget(self.view)
#
#     def pictureDropped(self, l):
#         for url in l:
#             if os.path.exists(url):
#                 print(url)
#                 icon = QtGui.QIcon(url)
#                 pixmap = icon.pixmap(72, 72)
#                 icon = QtGui.QIcon(pixmap)
#                 item = QtGui.QListWidgetItem(url, self.view)
#                 item.setIcon(icon)
#                 item.setStatusTip(url)
#
# def main():
#     app = QtGui.QApplication(sys.argv)
#     form = MainForm()
#     form.show()
#     app.exec_()
#
# if __name__ == '__main__':
#     main()
