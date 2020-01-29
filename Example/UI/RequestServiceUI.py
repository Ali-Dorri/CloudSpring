import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from Example import DBType


class RequestServiceUI:

    def __init__(self, userUI):
        self.userUI = userUI

    def initialize(self):
        pass

    def fillUI(self):
        # SQL
        pass

    def clearUI(self):
        pass

    def getTab(self):
        return self.userUI.requestServiceTab

    def setupUI(self):
        pass

    def retranslateUI(self):
        pass

    def setDefaultServices(self, servicePacket):
        #TODO set combo box default values
        pass