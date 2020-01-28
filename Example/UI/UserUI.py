import psycopg2
from Example import DBType
from Example import Repository
from Example.UI import MainUI
from PyQt5 import QtCore, QtGui, QtWidgets

class UserUI:

    def __init__(self, user, repository):
        self.user = user
        self.repo = repository
        self.connection = repository.DBConnection
        self.window = None

    def startUI(self):
        MainUI.MainUI.storeObject(self)
        print('start user ui')
        pass

