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
        # servicePacketTuples = self.userUI.repo.GetPackets(self.userUI.user.id)
        tuple0 = (0, '20150513', '20160614', 'Mac', '8GB', '10GHz', '500GB', '200KB', 4)
        tuple1 = (0, '20150823', '20160620', 'Windows', '16GB', '10GHz', '1TB', '250KB', 8)
        servicePacketTuples = [tuple0, tuple1]
        self.createBoxes(servicePacketTuples)
        self.retranslateUI()

    def fillUI(self):
        #SQL
        pass

    def clearUI(self):
        for i in range(len(self.packetBoxes)):
            self.removePacket(i)

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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.servicePacketsScrollArea.setWidget(self.servicePacketsScrollAreaWidgetContents)

    def createBoxes(self, servicePacketTuples):
        if servicePacketTuples is not None:
            for i in range(len(servicePacketTuples) - 1, -1, -1):
                packetTuple = servicePacketTuples[i]
                packet = DBType.ServicePacket.tupleToPacket(packetTuple)
                packetBox = ServicePacketBox(packet, self, i)
                packetBox.createBox(parentWidget=self.servicePacketsScrollAreaWidgetContents,
                                    parentLayout=self.gridLayout_3)
                packetBox.connectButtons()
                packetBox.retranslateUI()
                self.packetBoxes.append(packetBox)

    def retranslateUI(self):
        pass

    def editPacket(self, packIndex):
        self.userUI.switchTab(self.userUI.requestServiceTabUI)

    def removePacket(self, packIndex):
        #test just removing fromn list
        del self.packetBoxes[packIndex]
        pass