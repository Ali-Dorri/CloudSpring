from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
    def trackObject(cls, object):
        if object not in cls.storedObjects:
            cls.storedObjects.append(object)

    @classmethod
    def unTrackObject(cls, object):
        cls.storedObjects.remove(object)

    @staticmethod
    def showMessage(message, title = "Message", infoText = "", detailsText = ""):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setInformativeText(infoText)
        msg.setWindowTitle(title)
        msg.setDetailedText(detailsText)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()