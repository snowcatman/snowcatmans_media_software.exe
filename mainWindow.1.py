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
        
        
        # lineEdit movies
        self.ui.movie_lineEdit.textChanged.connect(self.text_Changed)

        self.model = QFileSystemModel()
        # set defualt directory
        self.path = (expanduser("~")+'\\Videos')
        self.index = self.model.setRootPath(self.path)
        # <widget class="QTreeView" name="treeView">
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setAnimated(False)
        self.ui.treeView.setIndentation(20)
        self.ui.treeView.setSortingEnabled(True)
        self.ui.treeView.setRootIndex(self.index)
        self.ui.treeView.setColumnHidden(1, True)
        self.ui.treeView.setColumnHidden(2, True)
        self.ui.treeView.setColumnHidden(3, True)
        # <widget class="QTreeView" name="treeView_future">
        self.ui.treeView_future.setModel(self.model)
        self.ui.treeView_future.setAnimated(False)
        self.ui.treeView_future.setIndentation(20)
        self.ui.treeView_future.setSortingEnabled(True)
        self.ui.treeView_future.setRootIndex(self.index)
        self.ui.treeView_future.setColumnHidden(1, True)
        self.ui.treeView_future.setColumnHidden(2, True)
        self.ui.treeView_future.setColumnHidden(3, True)
    
    # text input for movies
    def text_Changed(self):
        FakeFile = ('\\The Best Movie Ever 2018 PG\\The Best Movie Ever 2018 PG.mp4')
        user_text_input = self.sender().text()
        if self.sender().text() == 'Title Year Certified Rating':
            self.ui.movie_recipe_results.setText(self.sender().text())
            print(repr(self.sender().text()))
        else:
            pass
        # print(user_text_input)
        # print(repr(self)) # print(self)
        # want to pass fake results to change label text.
        # I liked the recipe results in media center master
        # """" best movie ever, The 2018(use curent year) PG(certified rating)""""
        pass
    
         ## text input for movies
    #def text_Changed(self):
        #FakeFile = ('\\The Best Movie Ever 2018 PG\\The Best Movie Ever 2018 PG.mp4')
        #user_text_input = self.sender().text()
        #if self.sender().text() == 'Title Year Certified Rating':
        #    self.ui.movie_recipe_results.setText(self.sender().text())
        #    print(repr(self.sender().text()))
        #else:
        #    pass
        ## print(user_text_input)
        ## print(repr(self)) # print(self)
        ## want to pass fake results to change label text.
        ## I liked the recipe results in media center master
        ## """" best movie ever, The 2018(use curent year) PG(certified rating)""""
        # pass

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
        self.ui.treeView.setRootIndex(self.index)

    def about(self):
        QMessageBox.about(self, "About", "This is a Template")

    def exit(self):
        QtWidgets.QApplication.instance().exit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
