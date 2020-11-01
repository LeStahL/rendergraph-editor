from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import renderPass

class RenderPassPropertyDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super(RenderPassPropertyDelegate, self).__init__()
        return

    def createEditor(self, parent, option, index):
        if index.column() == 1:
            if index.row() == 0:
                editor = QtWidgets.QLineEdit(parent)
                editor.setText(str(index.model().data(index)))
                return editor
            elif index.row() == 1:
                editor = QtWidgets.QComboBox(parent)
                editor.addItems([renderPass.RenderPass.Buffer, renderPass.RenderPass.Screen])
                editor.setCurrentText(str(index.model().data(index)))
                return editor
        return 0
