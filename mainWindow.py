from PyQt5 import QtCore, QtGui, QtWidgets
import ui_mainWindow

import renderPassPropertyModel, renderPass, renderPassPropertyDelegate, renderPassView

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, application):
        super().__init__()
        self.application = application
        self.ui = ui_mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO: remove test ground below
        renderpass = renderPass.RenderPass()
        model = renderPassPropertyModel.RenderPassPropertyModel(renderpass)
        delegate = renderPassPropertyDelegate.RenderPassPropertyDelegate()
        self.ui.tableView.setModel(model)
        self.ui.tableView.setItemDelegate(delegate)

        view = renderPassView.RenderPassView(self.ui.centralwidget)
        self.ui.centralwidget.layout().addWidget(view)

        self.update()

        return
