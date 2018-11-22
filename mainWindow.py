from os.path import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QFileDialog
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

    def folderOpen(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        return input_dir

    def about(self):
        QMessageBox.about(self, "About", "This is a Template")

    def exit(self):
        QtWidgets.QApplication.instance().exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())