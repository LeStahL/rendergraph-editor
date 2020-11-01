#!/usr/bin/env python
import mainWindow, sys
from PyQt5 import QtCore, QtWidgets, QtGui

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = mainWindow.MainWindow(application)
    window.show()
    application.exec()
