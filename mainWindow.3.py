import os
import pathlib
import re
import sys
from datetime import datetime
from os.path import expanduser
from threading import Timer

import PyQt5.uic
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QFileDialog, QFileSystemModel,
                             QHBoxLayout, QLabel, QMessageBox, QTreeView,
                             QVBoxLayout, QWidget)

from snowcatmans_media_filter import FFMF as M_F  # movie filter

# from snowcatmans_media_filter import my_path as M_F_F # fake path
Ui, UiBase = PyQt5.uic.loadUiType(pathlib.Path(__file__).with_name
                                  ('test_window.ui'),)


class MainWindow(UiBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui()
        self.ui.setupUi(self)
        # button actions
        self.ui.actionexit.triggered.connect(self.exit)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionOpen_Folder.triggered.connect(self.folderOpen)
        # lineEdit input from users. movies, tvmovies, tvshows
        self.ui.movie_lineEdit.textChanged.connect(self.text_Changed)
        self.ui.TVshow_movie_lineEdit.textChanged.connect(self.text_Changed)
        self.ui.TVshow_lineEdit.textChanged.connect(self.text_Changed)
        self.model = QFileSystemModel()
        # set defualt directories
        self.path = (expanduser("~")+'\\Videos')        # windows path
        self.index = self.model.setRootPath(self.path)  # path QT indexed
        print(self.index)
        print(self.index.data()) # gets Videos... nothing else...
        print(self.index.data(1)) # I guess I am looking for the rest of the info.
        # if i add an int other then 0 it gives me the object again. 
        # the document say nothing to me about what to do about this???
        # self.new_path = (expanduser("~")+'\\Videos') 
        # self.future_index = self.model.setRootPath(self.new_path)
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
        #  self.ui.treeView_future.setRootIndex(self.index)
        self.ui.treeView_future.setColumnHidden(1, True)
        self.ui.treeView_future.setColumnHidden(2, True)
        self.ui.treeView_future.setColumnHidden(3, True)
        
                        
        #  print('this is the path:', M_F_F(self.path)) #  results of 
        #  print(str(M_F(self.path)))

    class fake_media():
        now = datetime.now()
        fake_year = (now.strftime("%Y"))
        FakefolderFile = "C:\\mymovies\\B\\The Best Movie Ever.2018.PG\\The Best Movie Ever.2018.PG.mp4"
        # FakefolderFile = "C:\\The Best Movie Ever.2018.PG\\The Best Movie Ever.2018.PG.mp4"
        Title = "The Best Movie Ever" # Our fake Title
        Year = (fake_year) # always the curent year
        CR = "Pg" # CR = Certified Rating 

        def F_O(self): # F_O = Fake Orginize
            parts = self.FakefolderFile.split("\\")
            A = str(self.Title)
            B = self.Title+str(self.Year)
            # B = re.match(self.Title, str(self.Year))
            C = self.Title+str(self.Year)+ self.CR
            # C = re.match(self.Title, str(self.Year), self.CR)
            D = "Must have Title and Year name"
            # print(parts)
            # print(parts[3])
            # print(parts[3].split("."))
            # print(A+B+C+D)
            # print(A, B, C, D)
        

    fake_media().F_O()
    # rules for media title
    class media_title():
        pass
 
    # rules for media year
    class media_year():
        pass

    # rules for media certified rating
    class media_certified_rating():
        pass

    # user text input from movies, tv movies, tvshows
    def text_Changed(self):
        # user_text = [self.sender().objectName(), repr(self.sender().text())]
        # print(user_text) #wanting to know witch lineEdit text is changing?

    # if text input is from lineEdit change label text
        def label_output(self):
            Txt = self.sender().text()
            Objn = self.sender().objectName()
            if  Objn == ('movie_lineEdit'):
                if Txt == (''):
                    self.ui.movie_recipe_results.setText('Must start with Title')
                elif Txt == ('T'):
                    self.ui.movie_recipe_results.setText('The Best Movie Ever') 
                elif Txt == ('T Y'):
                    self.ui.movie_recipe_results.setText('The Best Movie Ever 2018')
                elif Txt == ('T Y CR'):
                    self.ui.movie_recipe_results.setText('The Best Movie Ever 2018 PG')
            elif Objn == ('TVshow_movie_lineEdit'):
                if Txt == (''):
                    self.ui.Tvshow_movie_recipe_results.setText('Must start with Title')
                elif Txt == ('T'):
                    self.ui.Tvshow_movie_recipe_results.setText('The Best Movie Ever') 
                elif Txt == ('T Y'):
                    self.ui.Tvshow_movie_recipe_results.setText('The Best Movie Ever 2018')
                elif Txt == ('T Y CR'):
                    self.ui.Tvshow_movie_recipe_results.setText('The Best Movie Ever 2018 TV-PG')
            elif Objn == ('TVshow_lineEdit'):
                if Txt == (''): 
                    self.ui.Tvshow_recipe_results.setText('Must start with Title')
                elif Txt == ('T'):
                    self.ui.Tvshow_recipe_results.setText('The Best TVShow Ever') 
                elif Txt == ('T Y'):
                    self.ui.Tvshow_recipe_results.setText('The Best TVShow Ever 2018') 
                elif Txt == ('T Y CR'):
                    self.ui.Tvshow_recipe_results.setText\
                    ('The Best TVShow Ever 2018 TV-PG')
                elif Txt == ('T Y CR S-E'):
                    self.ui.Tvshow_recipe_results.setText\
                    ('The Best TVShow Ever 2018 TV-PG S01E01')
                elif Txt == ('T Y CR S-E ET'):
                    self.ui.Tvshow_recipe_results.setText\
                    ('The Best TVShow Ever 2018 TV-PG S01E01 Best Episode')

        label_output(self)



    # for gwtting directories of media files
    def folderOpen(self):
        input_dir = QFileDialog.getExistingDirectory(
            None, 'Select a folder:', self.path)
        if input_dir == '': 
            return self.path
        else:
            pass
        index = self.model.setRootPath(input_dir)
        self.ui.treeView.setRootIndex(index)
    
    # to show user what folders and files will look like after they submit
    def futureTreeview(self):
        self.ui.treeView.setRootIndex(self._future_index)

    # the about popup window
    def about(self):
        QMessageBox.about(self, "About", "This is a Template")

    # um, the exit for this application or software
    def exit(self):
        print('exit main window')
        QtWidgets.QApplication.instance().exit()

    def timon(self):
        # print('timer on')
        t = Timer(6.0, self.exit)
        t.start()



#   https://stackoverflow.com/a/45106515
#   https://www.programcreek.com/python/example/81317/PyQt5.QtWidgets.QMainWindow
class SplashWindow1(UiBase):
    def __init__(self, parent=None):
        super().__init__(parent) # borderless works    , flags=QtCore.Qt.FramelessWindowHint
        print('show_splash')
        #  self.imagePath = "/home/ily19/Desktop/images/11.jpg"
        #  self.imagePath = "C:\Users\shawn quintal\Documents\snowcatemans_media_software_main\snowcatmans_media_software.exe\test1.png"
        self.imagePath = "snowcatmans.png"
        #  print("check file", os.path.isfile(self.imagePath))
        #  print("curent path", os.getcwd())

        self.resize(600, 400)
        self.center
        #  self.label = QtWidgets.QLabel(self.window)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #  self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        #  self.setStyleSheet("background-color: rgba(250, 0, 0, 250);")
        
        #  label goes here

        #  The QLabel where we can display an Image
        self.label = QtWidgets.QLabel(self) # for this window splash screen
        self.label.setGeometry(0,0,600,400)
        #  https://stackoverflow.com/questions/19087822/how-to-make-qt-widgets-fade-in-or-fade-out <-------<--------<-----
        #  self.label.setStyleSheet("background-color:#ffffff")

        #  The image
        self.image = QtGui.QImage(self.imagePath)
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        
        #  display our image on the label
        self.label.setPixmap(self.pixmapImage)

        #  frame our image on the label
        self.label.setScaledContents(True)

        #  end label here

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def timons(self):
        #  print('timed splash screen set on')
        tt = Timer(5.0, window1.hide)
        tt.start()

class SettingsWindow1(UiBase):
    def __init__(self, parent=None):

        super().__init__(parent)    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # window1 = SplashWindow1()
    # window1.show()
    window.show()
    #  window1.activateWindow()
    #  window.timon() # main window
    # window1.timons() # splash screen
    sys.exit(app.exec_())
#  End of File
