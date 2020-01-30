import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from Example import DBType
from Example.UI import MainUI



class RequestServiceUI:

    def __init__(self, userUI):
        self.userUI = userUI
        """status == 1 -> new service,    status == 2 -> edit service"""
        self.status = 1
        self.editPacketId = -1

    def initialize(self):
        self.setupUI()
        self.retranslateUI()
        self.connectButtons()

    def fillUI(self):
        # SQL
        pass

    def clearUI(self):
        pass

    def getTab(self):
        return self.userUI.requestServiceTab

    def setupUI(self):
        self.label = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 111, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label_3.setGeometry(QtCore.QRect(390, 130, 111, 31))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 111, 31))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label_5.setGeometry(QtCore.QRect(390, 20, 111, 31))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label_6.setGeometry(QtCore.QRect(390, 240, 111, 31))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.osComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.osComboBox.setGeometry(QtCore.QRect(150, 30, 181, 22))
        self.osComboBox.setObjectName("osComboBox")
        self.osComboBox.addItem("")
        self.osComboBox.addItem("")
        self.osComboBox.addItem("")
        self.ramComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.ramComboBox.setGeometry(QtCore.QRect(150, 140, 181, 22))
        self.ramComboBox.setObjectName("ramComboBox")
        self.ramComboBox.addItem("")
        self.ramComboBox.addItem("")
        self.ramComboBox.addItem("")
        self.ramComboBox.addItem("")
        self.coreComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.coreComboBox.setGeometry(QtCore.QRect(150, 250, 181, 22))
        self.coreComboBox.setObjectName("coreComboBox")
        self.coreComboBox.addItem("")
        self.coreComboBox.addItem("")
        self.coreComboBox.addItem("")
        self.cpuComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.cpuComboBox.setGeometry(QtCore.QRect(530, 30, 181, 22))
        self.cpuComboBox.setObjectName("cpuComboBox")
        self.cpuComboBox.addItem("")
        self.cpuComboBox.addItem("")
        self.cpuComboBox.addItem("")
        self.cpuComboBox.addItem("")
        self.cpuComboBox.addItem("")
        self.cpuComboBox.addItem("")
        self.cpuComboBox.addItem("")
        self.hdComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.hdComboBox.setGeometry(QtCore.QRect(530, 140, 181, 22))
        self.hdComboBox.setObjectName("hdComboBox")
        self.hdComboBox.addItem("")
        self.hdComboBox.addItem("")
        self.hdComboBox.addItem("")
        self.hdComboBox.addItem("")
        self.bwComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.bwComboBox.setGeometry(QtCore.QRect(530, 250, 181, 22))
        self.bwComboBox.setObjectName("bwComboBox")
        self.bwComboBox.addItem("")
        self.bwComboBox.addItem("")
        self.bwComboBox.addItem("")
        self.bwComboBox.addItem("")
        self.bwComboBox.addItem("")
        self.confirmNewPacketButton = QtWidgets.QPushButton(self.userUI.requestServiceTab)
        self.confirmNewPacketButton.setGeometry(QtCore.QRect(490, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirmNewPacketButton.setFont(font)
        self.confirmNewPacketButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.confirmNewPacketButton.setObjectName("confirmNewPacketButton")
        self.costLabel = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.costLabel.setGeometry(QtCore.QRect(470, 320, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.costLabel.setFont(font)
        self.costLabel.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.costLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.costLabel.setObjectName("costLabel")
        self.label_10 = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.label_10.setGeometry(QtCore.QRect(20, 350, 111, 31))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.durationComboBox = QtWidgets.QComboBox(self.userUI.requestServiceTab)
        self.durationComboBox.setGeometry(QtCore.QRect(150, 360, 181, 22))
        self.durationComboBox.setObjectName("durationComboBox")
        self.durationComboBox.addItem("")
        self.durationComboBox.addItem("")
        self.durationComboBox.addItem("")
        self.durationComboBox.addItem("")
        self.durationComboBox.addItem("")
        self.durationComboBox.addItem("")
        self.osComboBox.setCurrentIndex(0)
        self.ramComboBox.setCurrentIndex(0)
        self.coreComboBox.setCurrentIndex(0)
        self.cpuComboBox.setCurrentIndex(0)
        self.hdComboBox.setCurrentIndex(0)
        self.bwComboBox.setCurrentIndex(0)
        self.durationComboBox.setCurrentIndex(0)
        self.requestServiceModeButton = QtWidgets.QPushButton(self.userUI.requestServiceTab)
        self.requestServiceModeButton.setGeometry(QtCore.QRect(660, 380, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.requestServiceModeButton.setFont(font)
        self.requestServiceModeButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.requestServiceModeButton.setObjectName("requestServiceModeButton")
        self.requestServiceModeLabel = QtWidgets.QLabel(self.userUI.requestServiceTab)
        self.requestServiceModeLabel.setGeometry(QtCore.QRect(680, 340, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.requestServiceModeLabel.setFont(font)
        self.requestServiceModeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.requestServiceModeLabel.setObjectName("requestServiceModeLabel")

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("UserWindow", "Operating System"))
        self.label_2.setText(_translate("UserWindow", "RAM"))
        self.label_3.setText(_translate("UserWindow", "Hard Drive Space"))
        self.label_4.setText(_translate("UserWindow", "CPU Core"))
        self.label_5.setText(_translate("UserWindow", "CPU Frequency"))
        self.label_6.setText(_translate("UserWindow", "Band Width"))
        self.osComboBox.setCurrentText(_translate("UserWindow", "Windows"))
        self.osComboBox.setItemText(0, _translate("UserWindow", "Windows"))
        self.osComboBox.setItemText(1, _translate("UserWindow", "Mac"))
        self.osComboBox.setItemText(2, _translate("UserWindow", "Linux"))
        self.ramComboBox.setCurrentText(_translate("UserWindow", "2 GB"))
        self.ramComboBox.setItemText(0, _translate("UserWindow", "2 GB"))
        self.ramComboBox.setItemText(1, _translate("UserWindow", "4 GB"))
        self.ramComboBox.setItemText(2, _translate("UserWindow", "8 GB"))
        self.ramComboBox.setItemText(3, _translate("UserWindow", "16 GB"))
        self.coreComboBox.setCurrentText(_translate("UserWindow", "2 Cores"))
        self.coreComboBox.setItemText(0, _translate("UserWindow", "2 Cores"))
        self.coreComboBox.setItemText(1, _translate("UserWindow", "4 Cores"))
        self.coreComboBox.setItemText(2, _translate("UserWindow", "8 Cores"))
        self.cpuComboBox.setCurrentText(_translate("UserWindow", "4 GHz"))
        self.cpuComboBox.setItemText(0, _translate("UserWindow", "4 GHz"))
        self.cpuComboBox.setItemText(1, _translate("UserWindow", "5 GHz"))
        self.cpuComboBox.setItemText(2, _translate("UserWindow", "6 GHz"))
        self.cpuComboBox.setItemText(3, _translate("UserWindow", "7 GHz"))
        self.cpuComboBox.setItemText(4, _translate("UserWindow", "8 GHz"))
        self.cpuComboBox.setItemText(5, _translate("UserWindow", "9 GHz"))
        self.cpuComboBox.setItemText(6, _translate("UserWindow", "10 GHz"))
        self.hdComboBox.setCurrentText(_translate("UserWindow", "500 GB"))
        self.hdComboBox.setItemText(0, _translate("UserWindow", "500 GB"))
        self.hdComboBox.setItemText(1, _translate("UserWindow", "1 TB"))
        self.hdComboBox.setItemText(2, _translate("UserWindow", "2 TB"))
        self.hdComboBox.setItemText(3, _translate("UserWindow", "3 TB"))
        self.bwComboBox.setCurrentText(_translate("UserWindow", "100 Kb/s"))
        self.bwComboBox.setItemText(0, _translate("UserWindow", "100 Kb/s"))
        self.bwComboBox.setItemText(1, _translate("UserWindow", "250 Kb/s"))
        self.bwComboBox.setItemText(2, _translate("UserWindow", "500 Kb/s"))
        self.bwComboBox.setItemText(3, _translate("UserWindow", "1 Mb/s"))
        self.bwComboBox.setItemText(4, _translate("UserWindow", "2 Mb/s"))
        self.confirmNewPacketButton.setText(_translate("UserWindow", "Confirm"))
        self.costLabel.setText(_translate("UserWindow", "20000$"))
        self.label_10.setText(_translate("UserWindow", "Duration"))
        self.durationComboBox.setCurrentText(_translate("UserWindow", "6 Months"))
        self.durationComboBox.setItemText(0, _translate("UserWindow", "6 Months"))
        self.durationComboBox.setItemText(1, _translate("UserWindow", "1 Year"))
        self.durationComboBox.setItemText(2, _translate("UserWindow", "2 Years"))
        self.durationComboBox.setItemText(3, _translate("UserWindow", "3 Years"))
        self.durationComboBox.setItemText(4, _translate("UserWindow", "4 Years"))
        self.durationComboBox.setItemText(5, _translate("UserWindow", "5 Years"))
        self.requestServiceModeButton.setText(_translate("UserWindow", "New Service"))
        self.requestServiceModeLabel.setText(_translate("UserWindow", "Mode"))

    def connectButtons(self):
        self.requestServiceModeButton.clicked.connect(self.setToNewMode)
        self.confirmNewPacketButton.clicked.connect(self.buyNewPacket)

    def buyNewPacket(self):
        # balance = self.userUI.repo.GetUserBalance(self.userUI.user.id)
        # if balance is None:
        #     MainUI.MainUI.showMessage('some error in database. Try again later')
        

        pass

    def setToEditMode(self, packet):
        self.status = 2
        self.editPacketId = packet.packetId
        self.requestServiceModeButton.setText("Edit Service")
        # TODO set combo box to packet values

    def setToNewMode(self):
        self.status = 1
        self.editPacketId = -1
        self.requestServiceModeButton.setText("New Service")