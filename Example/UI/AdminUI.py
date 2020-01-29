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
        MainUI.MainUI.trackObject(self)
        print('start admin ui')
        self.window = QtWidgets.QMainWindow()
        self.setupUI()
        self.retranslateUI()
        self.window.show()

    def setupUI(self):
        self.window.resize(700, 500)
        self.window.setMaximumSize(QtCore.QSize(700, 500))
        self.window.setMinimumSize(QtCore.QSize(700, 500))

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle("Admin Panel")