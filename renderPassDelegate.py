from PyQt5 import QtCore, QtGui, QtWidgets

class RenderPassDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super(RenderPassDelegate).__init__()
        return

    def paint(self, painter, option, index):
        