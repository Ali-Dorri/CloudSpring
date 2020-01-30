import psycopg2
from Example import DBType
from Example import Repository
from Example.UI import MainUI
from PyQt5 import QtCore, QtGui, QtWidgets
from Example.UI.ServicePacketsTabUI import ServicePacketsTabUI
from Example.UI.RequestServiceUI import RequestServiceUI
from Example.UI.ReportProblemTabUI import ReportProblemTabUI
from Example.UI.UserDetailsTabUI import UserDetailsTabUI

class UserUI:

    def __init__(self, user, repository):
        self.user = user
        self.repo = repository
        self.connection = repository.DBConnection
        self.window = None
        self.servicePacketsTabUI = ServicePacketsTabUI(self)
        self.requestServiceTabUI = RequestServiceUI(self)
        self.reportProblemTabUI = ReportProblemTabUI(self)
        self.userDetailsTabUI = UserDetailsTabUI(self)
        self.currentTabIndex = -1

    def startUI(self):
        MainUI.MainUI.trackObject(self)
        print('start user ui')
        self.window = QtWidgets.QMainWindow()
        self.setupUI()
        self.retranslateUI()
        self.servicePacketsTabUI.initialize()
        self.requestServiceTabUI.initialize()
        self.reportProblemTabUI.initialize()
        self.userDetailsTabUI.initialize()
        self.currentTabIndex = self.tabWidget.currentIndex()
        startTabUI = self.__getTabUI(self.currentTabIndex)
        startTabUI.fillUI()
        self.window.show()

    def setupUI(self):
        self.window = QtWidgets.QMainWindow()
        self.window.setObjectName("UserWindow")
        self.window.resize(798, 517)
        self.window.setMinimumSize(QtCore.QSize(798, 517))
        self.window.setMaximumSize(QtCore.QSize(798, 517))
        self.window.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.servicePacketsTab = QtWidgets.QWidget()
        self.servicePacketsTab.setObjectName("ServicePacketsTab")
        self.tabWidget.addTab(self.servicePacketsTab, "")
        self.requestServiceTab = QtWidgets.QWidget()
        self.requestServiceTab.setObjectName("requestServiceTab")

        self.tabWidget.addTab(self.requestServiceTab, "")
        self.reportProblemTab = QtWidgets.QWidget()
        self.reportProblemTab.setObjectName("reportProblemTab")
        self.problemTextEdit = QtWidgets.QTextEdit(self.reportProblemTab)
        self.problemTextEdit.setGeometry(QtCore.QRect(20, 30, 641, 61))
        self.problemTextEdit.setObjectName("problemTextEdit")
        self.reportButton = QtWidgets.QPushButton(self.reportProblemTab)
        self.reportButton.setGeometry(QtCore.QRect(670, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.reportButton.setFont(font)
        self.reportButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.reportButton.setObjectName("reportButton")
        self.label_9 = QtWidgets.QLabel(self.reportProblemTab)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label_9.setObjectName("label_9")
        self.ticketsScrollArea = QtWidgets.QScrollArea(self.reportProblemTab)
        self.ticketsScrollArea.setGeometry(QtCore.QRect(0, 100, 791, 341))
        self.ticketsScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ticketsScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ticketsScrollArea.setWidgetResizable(True)
        self.ticketsScrollArea.setObjectName("ticketsScrollArea")
        self.ticketsScrollAreaWidgetContents = QtWidgets.QWidget()
        self.ticketsScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 339))
        self.ticketsScrollAreaWidgetContents.setObjectName("ticketsScrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ticketsScrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ticketGroup = QtWidgets.QGroupBox(self.ticketsScrollAreaWidgetContents)
        self.ticketGroup.setMinimumSize(QtCore.QSize(0, 230))
        self.ticketGroup.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ticketGroup.setBaseSize(QtCore.QSize(0, 230))
        self.ticketGroup.setStyleSheet("background-color: rgb(206, 255, 245);\n"
                                       "border-color: rgb(0, 170, 255);")
        self.ticketGroup.setObjectName("ticketGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ticketGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.ticketGroup)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(60, 15))
        self.label_7.setMaximumSize(QtCore.QSize(60, 15))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.reportDateLabel = QtWidgets.QLabel(self.groupBox)
        self.reportDateLabel.setMinimumSize(QtCore.QSize(60, 15))
        self.reportDateLabel.setMaximumSize(QtCore.QSize(60, 15))
        self.reportDateLabel.setStyleSheet("")
        self.reportDateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.reportDateLabel.setObjectName("reportDateLabel")
        self.horizontalLayout.addWidget(self.reportDateLabel)
        self.verticalLayout.addWidget(self.groupBox)
        self.problemTextBrowser = QtWidgets.QTextBrowser(self.ticketGroup)
        self.problemTextBrowser.setMinimumSize(QtCore.QSize(0, 55))
        self.problemTextBrowser.setStyleSheet("background-color: rgb(255, 255, 203);")
        self.problemTextBrowser.setObjectName("problemTextBrowser")
        self.verticalLayout.addWidget(self.problemTextBrowser)
        self.groupBox_2 = QtWidgets.QGroupBox(self.ticketGroup)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 40))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setMinimumSize(QtCore.QSize(60, 15))
        self.label_8.setMaximumSize(QtCore.QSize(60, 15))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.reportDateLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.reportDateLabel_2.setMinimumSize(QtCore.QSize(60, 15))
        self.reportDateLabel_2.setMaximumSize(QtCore.QSize(60, 15))
        self.reportDateLabel_2.setStyleSheet("")
        self.reportDateLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.reportDateLabel_2.setObjectName("reportDateLabel_2")
        self.horizontalLayout_2.addWidget(self.reportDateLabel_2)
        self.ticketStatusLabel = QtWidgets.QLabel(self.groupBox_2)
        self.ticketStatusLabel.setMinimumSize(QtCore.QSize(120, 25))
        self.ticketStatusLabel.setMaximumSize(QtCore.QSize(120, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ticketStatusLabel.setFont(font)
        self.ticketStatusLabel.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.ticketStatusLabel.setLineWidth(1)
        self.ticketStatusLabel.setTextFormat(QtCore.Qt.AutoText)
        self.ticketStatusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ticketStatusLabel.setWordWrap(False)
        self.ticketStatusLabel.setObjectName("ticketStatusLabel")
        self.horizontalLayout_2.addWidget(self.ticketStatusLabel)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.replyTextBrowser = QtWidgets.QTextBrowser(self.ticketGroup)
        self.replyTextBrowser.setMinimumSize(QtCore.QSize(0, 55))
        self.replyTextBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.replyTextBrowser.setStyleSheet("background-color: rgb(255, 255, 203);")
        self.replyTextBrowser.setObjectName("replyTextBrowser")
        self.verticalLayout.addWidget(self.replyTextBrowser)
        self.verticalLayout_2.addWidget(self.ticketGroup)
        spacerItem1 = QtWidgets.QSpacerItem(20, 500, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.ticketsScrollArea.setWidget(self.ticketsScrollAreaWidgetContents)
        self.tabWidget.addTab(self.reportProblemTab, "")
        self.userDetailsTab = QtWidgets.QWidget()
        self.userDetailsTab.setObjectName("tab")
        self.label_42 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_42.setGeometry(QtCore.QRect(230, 0, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.label_11 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.userDetailFirstNameLineEdit = QtWidgets.QLineEdit(self.userDetailsTab)
        self.userDetailFirstNameLineEdit.setGeometry(QtCore.QRect(160, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userDetailFirstNameLineEdit.setFont(font)
        self.userDetailFirstNameLineEdit.setText("")
        self.userDetailFirstNameLineEdit.setObjectName("userDetailFirstNameLineEdit")
        self.label_12 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_12.setGeometry(QtCore.QRect(410, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.userDetailLastNameLineEdit = QtWidgets.QLineEdit(self.userDetailsTab)
        self.userDetailLastNameLineEdit.setGeometry(QtCore.QRect(560, 90, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userDetailLastNameLineEdit.setFont(font)
        self.userDetailLastNameLineEdit.setText("")
        self.userDetailLastNameLineEdit.setObjectName("userDetailLastNameLineEdit")
        self.label_13 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_13.setGeometry(QtCore.QRect(10, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.userDetailEmailLineEdit = QtWidgets.QLineEdit(self.userDetailsTab)
        self.userDetailEmailLineEdit.setGeometry(QtCore.QRect(160, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userDetailEmailLineEdit.setFont(font)
        self.userDetailEmailLineEdit.setText("")
        self.userDetailEmailLineEdit.setObjectName("userDetailEmailLineEdit")
        self.label_14 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_14.setGeometry(QtCore.QRect(410, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.userDetailPasswordLineEdit = QtWidgets.QLineEdit(self.userDetailsTab)
        self.userDetailPasswordLineEdit.setGeometry(QtCore.QRect(560, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userDetailPasswordLineEdit.setFont(font)
        self.userDetailPasswordLineEdit.setText("")
        self.userDetailPasswordLineEdit.setObjectName("userDetailPasswordLineEdit")
        self.label_15 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_15.setGeometry(QtCore.QRect(10, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.userDetailNationalCodeLineEdit = QtWidgets.QLineEdit(self.userDetailsTab)
        self.userDetailNationalCodeLineEdit.setGeometry(QtCore.QRect(160, 330, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userDetailNationalCodeLineEdit.setFont(font)
        self.userDetailNationalCodeLineEdit.setText("")
        self.userDetailNationalCodeLineEdit.setObjectName("userDetailNationalCodeLineEdit")
        self.label_16 = QtWidgets.QLabel(self.userDetailsTab)
        self.label_16.setGeometry(QtCore.QRect(410, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.userDetailBalanceLineEdit = QtWidgets.QLineEdit(self.userDetailsTab)
        self.userDetailBalanceLineEdit.setGeometry(QtCore.QRect(560, 330, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userDetailBalanceLineEdit.setFont(font)
        self.userDetailBalanceLineEdit.setText("")
        self.userDetailBalanceLineEdit.setObjectName("userDetailBalanceLineEdit")
        self.tabWidget.addTab(self.userDetailsTab, "")
        self.logOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutButton.setGeometry(QtCore.QRect(360, 480, 91, 31))
        self.logOutButton.setObjectName("logOutButton")
        self.window.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("UserWindow", "User Panel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.servicePacketsTab),
                                  _translate("UserWindow", "Service Packets"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.requestServiceTab),
                                  _translate("UserWindow", "Request Service"))

        self.reportButton.setText(_translate("UserWindow", "Report Problem"))
        self.label_9.setText(_translate("UserWindow", "New Problem:"))
        self.ticketGroup.setTitle(_translate("UserWindow", "Ticket 1"))
        self.label_7.setText(_translate("UserWindow", "Problem"))
        self.reportDateLabel.setText(_translate("UserWindow", "1398/5/10"))
        self.problemTextBrowser.setHtml(_translate("UserWindow",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Problem Content</p></body></html>"))
        self.label_8.setText(_translate("UserWindow", "Reply"))
        self.reportDateLabel_2.setText(_translate("UserWindow", "1398/6/10"))
        self.ticketStatusLabel.setText(_translate("UserWindow", "Waiting For Reply"))
        self.replyTextBrowser.setHtml(_translate("UserWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Problem Content</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportProblemTab),
                                  _translate("UserWindow", "Report Problem"))
        self.label_42.setText(_translate("UserWindow", "User Details Not Ready"))
        self.label_11.setText(_translate("UserWindow", "First Name:"))
        self.label_12.setText(_translate("UserWindow", "Last Name:"))
        self.label_13.setText(_translate("UserWindow", "Email:"))
        self.label_14.setText(_translate("UserWindow", "Password:"))
        self.label_15.setText(_translate("UserWindow", "National Code:"))
        self.label_16.setText(_translate("UserWindow", "Balance:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userDetailsTab), _translate("UserWindow", "User Details"))
        self.logOutButton.setText(_translate("UserWindow", "Log Out"))

    def onTabManualSwitched(self, index):
        tabUI = self.__getTabUI(index)
        if tabUI is not None:
            self.switchTab()

    def switchTab(self, nextTabUI):
        previousTabUI = self.__getTabUI(self.currentTabIndex)
        if previousTabUI is not None and nextTabUI is not None and nextTabUI != previousTabUI:
            previousTabUI.clearUI()
            nextTabUI.fillUI()
            self.currentTabIndex = self.__getTabIndex(nextTabUI)
            self.tabWidget.setCurrentIndex(self.currentTabIndex)

    def __getTabUI(self, index):
        if index < 0 or index >= self.tabWidget.count():
            return None

        if self.servicePacketsTab == self.tabWidget.widget(index):
            return self.servicePacketsTabUI
        elif self.requestServiceTab == self.tabWidget.widget(index):
            return self.requestServiceTabUI
        elif self.reportProblemTab == self.tabWidget.widget(index):
            return self.reportProblemTabUI
        elif self.userDetailsTab == self.tabWidget.widget(index):
            return self.userDetailsTabUI
        return None

    def __getTabIndex(self, tabUI):
        if tabUI is None:
            return -1

        for i in range(self.tabWidget.count()):
            if tabUI.getTab() == self.tabWidget.widget(i):
                return i
        return -1
