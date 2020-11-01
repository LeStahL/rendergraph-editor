from PyQt5 import QtCore, QtGui, QtWidgets
import ui_mainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application
        self.ui = ui_mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        return
