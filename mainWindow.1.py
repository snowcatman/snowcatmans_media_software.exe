import sys
from os.path import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication
from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import pathlib
import PyQt5.uic
import sys

Ui, UiBase = PyQt5.uic.loadUiType(pathlib.Path(__file__).with_name
                                  ('test_window.ui'),)


class MainWindow(UiBase):
    def __init__(self, parent=None):
        
        super().__init__(parent)

        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.actionexit.triggered.connect(self.exit)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionOpen_Folder.triggered.connect(self.folderOpen)
        self.model = QFileSystemModel()

        # path = (expanduser("~")+'\\Videos')
        self.path = (expanduser("~")+'\\Videos')
        index = self.model.setRootPath(self.path)
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setAnimated(False)
        self.ui.treeView.setIndentation(20)
        self.ui.treeView.setSortingEnabled(True)
        self.ui.treeView.setRootIndex(index)

    def folderOpen(self):

        input_dir = QFileDialog.getExistingDirectory(
            None, 'Select a folder:', self.path)
        if input_dir == '':
            return self.path
        else:
            pass
        
        index = self.model.setRootPath(input_dir)
        self.ui.treeView.setRootIndex(index)

    def about(self):
        QMessageBox.about(self, "About", "This is a Template")

    def exit(self):
        QtWidgets.QApplication.instance().exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
