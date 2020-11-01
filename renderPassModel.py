from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import renderPass

class RenderPassModel(QtCore.QAbstractTableModel):
    def __init__(self, renderPass):
        super(RenderPassModel, self).__init__()
        self.renderPass = renderPass
        return

    def rowCount(self, parent):
        return self.renderpass.bufferUniforms().length()

    def columnCount(self, parent):
        return 2

    def data(self, index, role = QtCore.Qt.DisplayRole):
        # if role == QtCore.Qt.DisplayRole:
            # if index.column() == 0:
