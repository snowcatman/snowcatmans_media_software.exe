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
        # menubar file - openfolder button // may need to make this part 
        # of the function that populates the treeview.
        self.ui.actionOpen_Folder.triggered.connect(self.folderOpen)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# QTreeview  
        self.model = QtGui.QStandardItemModel()
        self.ui.treeView.setModel(self.model)
        # Next line has me woundering what its doing.
        # I dont think it will be triggered as is. 
        # The line above my refure to the QTreeview
        # and the line below may neet to refure to 
        # the treeView.
        self.ui.actionOpen_Folder.triggered.connect(self.add_item)

    def add_item(self): 
        
        # using qt4 from https://stackoverflow.com/questions/11639293/minimal-example-qtreeview-for-pyqt-and-the-qt-designer
        # Thinking that treeview is not configured yet. Need to 
        # convigure to qt5 and create the the treeview in the py file.
        # that there is no name attribute "lineEdit_Moebel" 
        # from the ui file um, when use of name attribute 
        # "treeView" then I get error no name attribute "text"
        # I think this methode keeps refrancing to the ui file,
        # instead of me doing the work here in the py file.

        t = self.ui.treeView()
        if len(t) > 0: 
            item = QtGui.QStandardItem(t)
            self.model.appendRow(item)
            self.ui.treeView()
        else:
            self.ui.statusBar.showMessage('error: no text in Moebel')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def folderOpen(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        print(input_dir)
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
