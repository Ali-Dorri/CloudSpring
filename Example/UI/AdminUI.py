import psycopg2
from Example import DBType
from Example import Repository
from Example.UI import MainUI
from PyQt5 import QtCore, QtGui, QtWidgets



class AdminUI:

    def __init__(self, admin, repository):
        self.admin = admin
        self.repo = repository
        self.connection = repository.DBConnection
        self.window = None

    def startUI(self):
        MainUI.MainUI.storeObject(self)
        print('start admin ui')
        self.window = QtWidgets.QMainWindow()
        self.setupUI()
        self.retranslateUI()
        self.window.show()

    def setupUI(self):
        pass

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle("Admin Panel")