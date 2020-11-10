import sys
from  PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtGui import QIcon
import time

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 TestApp")
        self.setGeometry(300,300,300,300)
        self.setMinimumHeight(100)
        self.setMaximumHeight(250)
        self.setIcon()

    def setIcon(self):
        appIcon = QIcon('penguin.png')
        self.setWindowIcon(appIcon)


myApp = QApplication(sys.argv)
win = Window()
win.show()


myApp.exec_()

sys.exit(0)
