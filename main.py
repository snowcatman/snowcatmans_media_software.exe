#!/bin/python3

from PyQt5.QtWidgets import QApplication, QMainWindow
from startwindow import Ui_startWindow
from homewindow import Ui_homeWindow
from window1 import Ui_Window1
from window2 import Ui_Window2
from window3 import Ui_Window3


class start(QMainWindow, Ui_startWindow):
    def __init__(self):
        super(start, self).__init__(None)
        self.setupUi(self)
        self.homeButton.clicked.connect(self.toHome)
        self.home = home()

    def toHome(self):
        self.home.show()
        self.hide()

class home(QMainWindow, Ui_homeWindow):
    def __init__(self):
        super(home, self).__init__(None)
        self.setupUi(self)
        self.window1Button.clicked.connect(self.toWindow1)
        self.window2Button.clicked.connect(self.toWindow2)
        self.window3Button.clicked.connect(self.toWindow3)
        self.Window1 = window1(self)
        self.Window2 = window2(self)
        self.Window3 = window3(self)

    def toWindow1(self):
        self.Window1.show()
        self.setEnabled(False)
        self.Window1.setEnabled(True)

    def toWindow2(self):
        self.Window2.show()
        self.setEnabled(False)
        self.Window2.setEnabled(True)

    def toWindow3(self):
        self.Window3.show()
        self.setEnabled(False)
        self.Window3.setEnabled(True)

    def reEnable(self):
        self.setEnabled(True)

class window1(QMainWindow, Ui_Window1):
    def __init__(self, home):
        super(window1, self).__init__(home)
        self.home = home
        self.setupUi(self)
        self.homeButton.clicked.connect(self.toHome)

    def toHome(self):
        self.home.setEnabled(True)
        self.hide()


class window2(QMainWindow, Ui_Window2):
    def __init__(self, home):
        super(window2, self).__init__(home)
        self.home = home
        self.setupUi(self)
        self.homeButton.clicked.connect(self.toHome)

    def toHome(self):
        self.home.setEnabled(True)
        self.hide()

class window3(QMainWindow, Ui_Window3):
    def __init__(self, home):
        super(window3, self).__init__(home)
        self.home = home
        self.setupUi(self)
        self.homeButton.clicked.connect(self.toHome)

    def toHome(self):
        self.home.setEnabled(True)
        self.hide()