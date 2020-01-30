import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from Example.UI.ServicePacketBox import ServicePacketBox
from Example import DBType

class ServicePacketsTabUI:

    def __init__(self, userUI):
        self.userUI = userUI
        self.packetBoxes = []

    def initialize(self):
        self.setupUI()
        self.retranslateUI()

    def fillUI(self):
        servicePacketTuples = self.userUI.repo.GetUserPackets(self.userUI.user.id)
        self.createBoxes(servicePacketTuples)

    def clearUI(self):
        for i in range(len(self.packetBoxes)):
            self.packetBoxes[i].servicePackGroup.setParent(None)
        self.packetBoxes.clear()

    def getTab(self):
        return self.userUI.servicePacketsTab

    def setupUI(self):
        QtWidgets.QScrollArea()
        self.servicePacketsScrollArea = QtWidgets.QScrollArea(self.userUI.servicePacketsTab)
        self.servicePacketsScrollArea.setGeometry(QtCore.QRect(0, 10, 791, 431))
        self.servicePacketsScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.servicePacketsScrollArea.setWidgetResizable(True)
        self.servicePacketsScrollArea.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.servicePacketsScrollArea.setObjectName("servicePacketsScrollArea")
        self.servicePacketsScrollAreaWidgetContents = QtWidgets.QWidget()
        self.servicePacketsScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 429))
        self.servicePacketsScrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.servicePacketsScrollAreaWidgetContents.setObjectName("servicePacketsScrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.servicePacketsScrollAreaWidgetContents)
        self.gridLayout_3.setContentsMargins(-1, 11, -1, -1)
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.servicePacketsScrollArea.setWidget(self.servicePacketsScrollAreaWidgetContents)

    def createBoxes(self, servicePacketTuples):
        if servicePacketTuples is not None:
            for i in range(len(servicePacketTuples)):
                packetTuple = servicePacketTuples[i]
                packet = DBType.ServicePacket.tupleToPacket(packetTuple)
                packetBox = ServicePacketBox(packet, self)
                packetBox.createBox(parentWidget=self.servicePacketsScrollAreaWidgetContents,
                                    parentLayout=self.gridLayout_3, index=i)
                packetBox.connectButtons()
                packetBox.retranslateUI()
                self.packetBoxes.append(packetBox)
        self.setSpacer()

    def setSpacer(self):
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)

    def retranslateUI(self):
        pass

    def editPacket(self, packet):
        self.userUI.switchTab(self.userUI.requestServiceTabUI)
        self.userUI.requestServiceTabUI.setToEditMode(packet)

    def removePacket(self, packetBox):
        self.packetBoxes.remove(packetBox)
        #remove from database
        self.userUI.repo.RemoveServicePacket(packetBox.packet.packetId)