import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, \
QWidget, QPushButton, QAction, QDesktopWidget, QPushButton, QMessageBox, \
QFileSystemModel, QTreeView, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Snowcatman\'s Media Software Orginizer'
        self.initUI()
 
    def initUI(self):
        self.resize(640, 400)
        self.setWindowTitle('Snowcatman\'s Media Software')
        self.center()
        # I think these next two lines need modified
        self.model = QFileSystemModel()
        self.model.setRootPath('') 
        # thinking should use a setting to set root path
        
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        # exit button in file menu
        exitButton = QAction(QIcon('unkown.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        # About button in help menu
        aboutButton = QAction(QIcon('unkown.png'), 'About', self)
        aboutButton.setStatusTip('About Application')
        aboutButton.triggered.connect(self.about)
        helpMenu.addAction(aboutButton)
        
        #  setting up for the tree view
        self.tree = QTreeView()
        self.tree.setModel(self.model)
 
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
 
        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)

        # show in main window to the left between the menubar 
        # and the status bar
        # windowLayout = QVBoxLayout()
        # windowLayout.addWidget(self.tree)
        # self.setLayout(windowLayout)

        self.statusBar().showMessage('Message in statusbar - Template.')
        self.show()

    def about(self):
        # need to make a frameless or boarderless window
        # would like to have a window be about 300 x 400 
        # would like to have several lines of information
        # text centered in window
        QMessageBox.about(self, "About", "This is a Template")

    def center(self):
        # This centers the main window to the center of 
        # the monitor screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())