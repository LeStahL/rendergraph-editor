from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import renderPass

class RenderPassPropertyModel(QtCore.QAbstractTableModel):
    def __init__(self, renderPass):
        super(RenderPassPropertyModel, self).__init__()
        self.renderPass = renderPass
        return

    def rowCount(self, parent):
        return 2

    def columnCount(self, parent):
        return 2

    def data(self, index, role = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                if index.row() == 0:
                    return QtCore.QVariant('Renderpass name')
                elif index.row() == 1:
                    return QtCore.QVariant('Renderpass type')
            elif index.column() == 1:
                if index.row() == 0:
                    return QtCore.QVariant(self.renderPass.name)
                elif index.row() == 1:
                    return QtCore.QVariant(self.renderPass.type)
        return QtCore.QVariant()

    def headerData(self, section, orientation, role = QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                if section == 0:
                    return QtCore.QVariant('Identifier')
                elif section == 1:
                    return QtCore.QVariant('Value')
        return QtCore.QVariant()

    def setData(self, index, value, role = QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            if index.row() == 0:
                self.renderPass.name = value.value()
                self.dataChanged.emit(index, index, [QtCore.Qt.EditRole])
                return True
            elif index.row() == 1:
                self.renderPass.type = value.value()
                self.dataChanged.emit(index, index, [QtCore.Qt.EditRole])
                return True
        return False

    def flags(self, index):
        flags = super(RenderPassPropertyModel, self).flags(index)
        if index.column() == 1:
            flags = flags | QtCore.Qt.ItemIsEditable
        return flags
