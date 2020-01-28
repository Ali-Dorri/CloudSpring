from PyQt5 import  QtCore, QtGui, QtWidgets
import sys
from Example.UI.RegisterUI import RegisterUI

class MainUI:
    storedObjects = []

    def __init__(self, connection, repository):
        self.connection = connection
        self.repo = repository

    def startUI(self):
        app = QtWidgets.QApplication(sys.argv)
        registerUI = RegisterUI(self.connection, self.repo)
        registerUI.startUI()
        sys.exit(app.exec_())

    @classmethod
    def storeObject(cls, window):
        if window not in cls.storedObjects:
            cls.storedObjects.append(window)