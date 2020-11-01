from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import renderPass

class RenderPassPropertyDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super(RenderPassPropertyDelegate, self).__init__()
        return

    def createEditor(self, parent, option, index):
        if index.column() == 1:
            if index.row() == 0:
                return QtWidgets.QLineEdit(parent)
            elif index.row() == 1:
                editor = QtWidgets.QComboBox(parent)
                editor.addItems([renderPass.RenderPass.Buffer, renderPass.RenderPass.Screen])
                return editor
        return 0

    def setEditorData(self, editor, index):
        if index.column() == 1:
            if index.row() == 0:
                editor.setText(index.model().data(index).value())
            elif index.row() == 1:
                editor.setCurrentText(index.model().data(index).value())
    
    def setModelData(self, editor, model, index):
        if index.column() == 1:
            if index.row() == 0:
                model.setData(index, QtCore.QVariant(editor.text()))
            elif index.row() == 1:
                model.setData(index, QtCore.QVariant(editor.currentText()))
