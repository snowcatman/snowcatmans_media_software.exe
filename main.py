import sys, os
from os.path import expanduser
from PyQt5.QtWidgets import QMainWindow, QApplication, \
QWidget, QPushButton, QAction, QDesktopWidget, QPushButton, \
QMessageBox, QFileSystemModel, QTreeView, QVBoxLayout, \
QAbstractItemView, QFileDialog, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - Template'
        self.initUI()
 
    def initUI(self):
        self.resize(640, 400)
        self.setWindowTitle('My Template example')
        self.center()

        # menubar        
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        # open folder in file menu in menu bar
        openFolder = QAction(QIcon('unknown.png'), 'Open Folder', self)
        openFolder.setShortcut('Ctrl+O')
        openFolder.setStatusTip('Add Select Root Folder')
        openFolder.triggered.connect(self.folderOpen)
        fileMenu.addAction(openFolder)        
        # exit button in file menu in menu bar
        exitButton = QAction(QIcon('unknown.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        # About button in help menu in menu bar
        aboutButton = QAction(QIcon('unknown.png'), 'About', self)
        aboutButton.setStatusTip('About Application')
        aboutButton.triggered.connect(self.about)
        helpMenu.addAction(aboutButton)

# ----- defult tree view -- untell root folder added ------
# we need to know each root directory to add a search peramitor
# of the meadia in question. could use the open folder button 
# in file menu. updating or adding to a defual tree view of selected 
# folders would be nice .
                                # I know i don't know exactly 
                                # what i am doing. To add the 
                                # treeview. to the main window.
                                # I am a beginner. Thank you.

        
        

# -----------------------------------------------------------

        self.statusBar().showMessage('Message in statusbar - Template.')
        self.show()

    def folderOpen(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        return input_dir

    def about(self):
        QMessageBox.about(self, "About", "This is a Template")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())