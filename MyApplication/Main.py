from PyQt5.QtWidgets import (QMainWindow)

from MyApplication import MyClass
from MyApplication.ui import gui

Ui_MainWindow = gui.Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Fill you buttons with content and connect you signals and slots
        self.actionExit.triggered.connect(self.close)