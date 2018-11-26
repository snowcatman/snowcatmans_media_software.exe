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
        # set defualt directory
        self.path = (expanduser("~")+'\\Videos')
        index = self.model.setRootPath(self.path)
        # <widget class="QTreeView" name="treeView">
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setAnimated(False)
        self.ui.treeView.setIndentation(20)
        self.ui.treeView.setSortingEnabled(True)
        self.ui.treeView.setRootIndex(index)
        self.ui.treeView.setColumnHidden(1, True)
        self.ui.treeView.setColumnHidden(2, True)
        self.ui.treeView.setColumnHidden(3, True)
        # <widget class="QTreeView" name="treeView_future">
        self.ui.treeView_future.setModel(self.model)
        self.ui.treeView_future.setAnimated(False)
        self.ui.treeView_future.setIndentation(20)
        self.ui.treeView_future.setSortingEnabled(True)
        self.ui.treeView_future.setRootIndex(index)
        self.ui.treeView_future.setColumnHidden(1, True)
        self.ui.treeView_future.setColumnHidden(2, True)
        self.ui.treeView_future.setColumnHidden(3, True)
        # <widget class="QLineEdit" name="movie_lineEdit">

        # self.ui.movie_lineEdit.???


    def folderOpen(self):
        input_dir = QFileDialog.getExistingDirectory(
            None, 'Select a folder:', self.path)
        if input_dir == '': 
            return self.path
        else:
            pass
        index = self.model.setRootPath(input_dir)
        self.ui.treeView.setRootIndex(index)
    
    def futureTreeview(self):
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
