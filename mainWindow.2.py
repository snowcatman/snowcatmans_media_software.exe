import sys, re
from datetime import datetime
from os.path import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QApplication
from PyQt5.QtWidgets import QFileSystemModel, QTreeView, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import pathlib
import PyQt5.uic
# snowcatmans_media_filter takes folder and file info
# and sort title year and certified rating etc.
# import snowcatmans_media_filter as smf

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
        
        
        # lineEdit input from users. movies, tvmovies, tvshows
        self.ui.movie_lineEdit.textChanged.connect(self.text_Changed)
        self.ui.TVshow_movie_lineEdit.textChanged.connect(self.text_Changed)
        self.ui.TVshow_lineEdit.textChanged.connect(self.text_Changed)

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
    

    class fake_media():
        now = datetime.now()
        fake_year = (now.strftime("%Y"))
        FakefolderFile = \
        ('C:\\mymovies\\B\\The Best Movie Ever 2018 PG\\The Best Movie Ever 2018 PG.mp4')
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
            print(parts)
            print(parts[3])
            print(parts[3].split("2018"))
            # print(A+B+C+D)
            # print(A, B, C, D)
        
        #def F_O_A(self): # fake orginizer alpha
            #print(self.F_O.A+self.F_O.B+self.F_O.C+self.F_O.D)
            #obj1 = self.F_O() #o1.x=10
            #obj2 = fake_media() #o2.x=10
        #print(str(obj1.x))
        #print(str(obj2.x))
        #F_O(obj1) #o1.x=20
        #F_O(obj2) #o2.x=20
        #F_O(obj1) #o1.x=30
        #print(str(obj1.x))
        #print(str(obj2.x))


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
        user_text = [self.sender().objectName(), repr(self.sender().text())]
        print(user_text) #wanting to know witch lineEdit text is changing?
                
        
    # if text input is from lineEdit change label text
    def label_output(self):
        print(self.sender().text().split("2018"))
        
        # if self.sender().objectName() == ('movie_lineEdit'):
            #self.ui.movie_recipe_results.setText(mtf+" "+myf+" "+mcrf)
            #if self.sender().text()[0:5].lower() != "title":
                #self.ui.movie_recipe_results.setText('Must start with Title')
            
            #elif self.sender().text() == ('Title'):
                #self.ui.movie_recipe_results.setText(mtf) # set text to fake title
            # self.ui.movie_recipe_results.setText(self.sender().text())
            
            #elif self.sender().text() == ('Title'+" "+'Year'):
                #self.ui.movie_recipe_results.setText(mtf+" "+myf)


        #elif self.sender().objectName() == ('TVshow_movie_lineEdit'):
            #self.ui.Tvshow_movie_recipe_results.setText(self.sender().text())
            
        #elif self.sender().objectName() == ('TVshow_lineEdit'):
            #self.ui.Tvshow_recipe_results.setText(self.sender().text())
            
        #else:
            #pass

    # label_output(self)

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


# filtering media for naming labels
    # title = "the best movie ever"
    # year = this year "2018" for the moment
    # certified rating = "PG"
    # FakefolderFile = \
    # ('C:\\mymovies\\B\\The Best Movie Ever 2018 PG\\The Best Movie Ever 2018 PG.mp4')
    
    # text input for movies
    # def text_Changed(self):

        #FakeFolderFile = \
        # ('C:\\mymovies\\B\\The Best Movie Ever 2018 PG\\The Best Movie Ever 2018 PG.mp4')
        # Title = 'the best movie ever '
        # Year = '2018 '
        # Certified = ['PG ']
        # Rating = Certified

        # user_text_input = self.sender().text()
        # if self.sender().text() == 'Title Year Certified Rating':
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