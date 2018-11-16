import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, \
QWidget, QPushButton, QAction, QDesktopWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 menu - Template'
        # self.left = 10
        # self.top = 10
        # self.width = 640
        # self.height = 400
        self.initUI()
 
    def initUI(self):
        self.resize(640, 400)
        self.setWindowTitle('My Template example')
        self.center()
        # self.setGeometry(self.left, self.top, self.width, self.height)
        
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

        self.statusBar().showMessage('Message in statusbar - Template.')
        self.show()

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