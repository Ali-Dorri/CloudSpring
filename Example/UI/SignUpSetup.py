from PyQt5 import  QtCore, QtGui, QtWidgets
from Example import DBType
from Example.UI import MainUI

class SignUpSetup:

    def __init__(self, registerUI):
        self.registerUI = registerUI
        self.window = QtWidgets.QMainWindow()

    def setupUi(self):
        self.window.setObjectName("SignUp")
        self.window.resize(385, 452)
        self.window.setMaximumSize(QtCore.QSize(385, 452))
        self.window.setMinimumSize(QtCore.QSize(385, 452))
        self.window.setStyleSheet("")
        self.window.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(120, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setText("")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(5, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.passLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passLineEdit.setGeometry(QtCore.QRect(120, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passLineEdit.setFont(font)
        self.passLineEdit.setText("")
        self.passLineEdit.setObjectName("passLineEdit")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(120, 340, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.signUpButton.setFont(font)
        self.signUpButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.signUpButton.setObjectName("signUpButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 400, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(200, 401, 61, 28))
        self.signInButton.setStyleSheet("background-color: #A3C1DA; color: blue;")
        self.signInButton.setFlat(True)
        self.signInButton.setObjectName("signInButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(5, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setGeometry(QtCore.QRect(120, 180, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstNameLineEdit.setFont(font)
        self.firstNameLineEdit.setText("")
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(5, 220, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setGeometry(QtCore.QRect(120, 230, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastNameLineEdit.setFont(font)
        self.lastNameLineEdit.setText("")
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(5, 270, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.nationalCodeLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nationalCodeLineEdit.setGeometry(QtCore.QRect(150, 280, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nationalCodeLineEdit.setFont(font)
        self.nationalCodeLineEdit.setText("")
        self.nationalCodeLineEdit.setObjectName("nationalCodeLineEdit")
        self.window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.connectButtons()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "Sign Up"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.signUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.label_4.setText(_translate("MainWindow", "Have account?"))
        self.signInButton.setText(_translate("MainWindow", "Sign In"))
        self.label_5.setText(_translate("MainWindow", "First Name:"))
        self.label_6.setText(_translate("MainWindow", "Last Name:"))
        self.label_7.setText(_translate("MainWindow", "Nartional Code:"))

    def startUI(self):
        self.window.show()
        if self.registerUI.user.email is not None:
            self.emailLineEdit.setText(self.registerUI.user.email)
        if self.registerUI.user.password is not None:
            self.passLineEdit.setText(self.registerUI.user.password)
        if self.registerUI.user.first_name is not None:
            self.firstNameLineEdit.setText(self.registerUI.user.first_name)
        if self.registerUI.user.last_name is not None:
            self.lastNameLineEdit.setText(self.registerUI.user.last_name)
        if self.registerUI.user.national_code is not None:
            self.nationalCodeLineEdit.setText(self.registerUI.user.national_code)

    def connectButtons(self):
        self.signUpButton.clicked.connect(self.openPanelWindow)
        self.signInButton.clicked.connect(self.toSignIn)

    def toSignIn(self):
        self.setInfo()
        self.registerUI.createSigninWindow()

    def setInfo(self):
        user = DBType.User.emptyUser()
        user.first_name = self.firstNameLineEdit.text()
        user.last_name = self.lastNameLineEdit.text()
        user.national_code = self.nationalCodeLineEdit.text()
        user.email = self.emailLineEdit.text()
        user.password = self.passLineEdit.text()
        self.registerUI.user = user

    def checkInfo(self):
        if self.registerUI.checkInput():
            if self.emailLineEdit.text() and self.passLineEdit.text() and self.firstNameLineEdit.text() and self.lastNameLineEdit.text()\
                    and self.nationalCodeLineEdit.text():
                """add user and check it's repeatition on sql trigger"""
                try:
                    if self.registerUI.repo.AddUser(self.registerUI.user):
                        return True
                    else:
                        MainUI.MainUI.showMessage('user email is repeated or some connection error was occurred')
                        return False
                except:
                    MainUI.MainUI.showMessage('some error occurred in database')
                    return False
            else:
                MainUI.MainUI.showMessage('not all fields are filled!')
                return False
        else:
            return False

    def openPanelWindow(self):
        self.setInfo()
        if self.checkInfo():
            userTuples = self.registerUI.repo.GetUser(self.registerUI.user.email)
            user = DBType.User.tupleToUser(userTuples[0])
            self.registerUI.user = user
            self.registerUI.openPanelWindow()
            self.registerUI.signUpSetup = None
