import sys
from os.path import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication
from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import pathlib, PyQt5.uic, sys

Ui, UiBase = PyQt5.uic.loadUiType(
    pathlib.Path(__file__).with_name('test_window.ui'),
)


class MainWindow(UiBase):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui()
        self.ui.setupUi(self)
        
        # menubar file - exit button
        self.ui.actionexit.triggered.connect(self.exit)
        # menubar help - about button
        self.ui.actionAbout.triggered.connect(self.about)
        # menubar file - openfolder button
        self.ui.actionOpen_Folder.triggered.connect(self.folderOpen)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# QTreeview  

# [12:15] <altendky>06 snowcatman: maybe you want a new method set_root(self, path) 
# that will run those two lines. Then you can call it from __init__ and from openFolder
        path = (expanduser("~"), Vidios)

        def set_root(self, path) : # creating a funtion to help set root path
            index = self.model.setRootPath(path)
            # make an index from the string path
            self.ui.treeView.setRootIndex(index)
            # set's/uses index for current QTreeview

        # path = '%userprofile%\\Videos'
        self.model = QFileSystemModel()
        ###---------------------------------- setting defualt path for QTreeview
        # set_root(self.ui.treeView, path)
        # self.model(set_root(self, '%userprofile%Videos'))
        ###----------------------------------
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setAnimated(False)
        self.ui.treeView.setIndentation(20)
        self.ui.treeView.setSortingEnabled(True)

    def folderOpen(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        print(input_dir)
        # this give were the user wants to open folder. input_dir = folder path
        index = self.model.setRootPath(input_dir)
        # make an index from the string input_dir
        self.ui.treeView.setRootIndex(index)
        # set's/uses index for current QTreeview

    def about(self):
        QMessageBox.about(self, "About", "This is a Template")

    def exit(self):
        QtWidgets.QApplication.instance().exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
