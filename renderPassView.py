from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import renderPass

class RenderPassView(QtWidgets.QAbstractItemView):
    def __init__(self, parent = None):
        super(RenderPassView, self).__init__(parent)
        self.passName = "RenderPass Name"
        self.passType = "Buffer"
        self.bufferUniforms = dict()
        return

    def indexAt(self, point):
        pass

    def scrollTo(self, index, hint = QtWidgets.QAbstractItemView.EnsureVisible):
        pass

    def visualRect(self, index):
        pass

    def dataChanged(self, topLeft, bottomRight, roles):
        super(RenderPassView, self).dataChanged(topLeft, bottomRight, roles)

        if not roles.contains(QtCore.Qt.DisplayRole):
            return

        self.passName = self.model().data(self.model().index(0, 0, self.rootIndex())).value()
        self.passType = self.model().data(self.model().index(0, 1, self.rootIndex())).value()
        
        self.bufferUniforms.clear()
        for i in range(1,self.model().rowCount(self.rootIndex())):
            self.bufferUniforms[self.model().data(self.model().index(i, 0, self.rootIndex())).value()] = self.model().data(self.model().index(i, 1, self.rootIndex())).value()
        self.viewport().update()

    def rowsInserted(self, parent, start, end):
        pass

    def rowsAboutToBeRemoved(self, parent, start, end):
        pass

    def edit(self, index, trigger, event):
        pass

    def moveCursor(self, cursorAction, keyboardModifiers):
        pass
    
    def horizontalOffset(self):
        pass

    def verticalOffset(self):
        pass

    def isIndexHidden(self, index):
        pass

    def setSelection(self, rect, flags):
        pass

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        pass

    def mouseReleaseEvent(self, event):
        pass

    def paintEvent(self, event):
        option = self.viewOptions()
        backgroundBrush = option.palette.base()
        foregroundPen = QtGui.QPen(option.palette.color(QtGui.QPalette.WindowText))

        painter = QtGui.QPainter(self.viewport())
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        painter.fillRect(event.rect(), backgroundBrush)
        painter.setPen(foregroundPen)

    def resizeEvent(self, event):
        pass

    def scrollContentsBy(self, dx, dy):
        pass

    def visualRegionForSelection(self, selection):
        pass

    def selectionChanged(self, selected, deselected):
        pass
