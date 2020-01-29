from PyQt5 import  QtCore, QtGui, QtWidgets
from Example import DBType
from Example.UI import MainUI

class SignInSetup:

    def __init__(self, registerUI):
        self.registerUI = registerUI
        self.window = QtWidgets.QMainWindow()


    def setupUi(self):
        self.window.setObjectName("MainWindow")
        self.window.resize(385, 325)
        self.window.setMaximumSize(QtCore.QSize(385, 325))
        self.window.setMinimumSize(QtCore.QSize(385, 325))
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
        self.label_2.setGeometry(QtCore.QRect(10, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(110, 80, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setText("")
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.passLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passLineEdit.setGeometry(QtCore.QRect(110, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passLineEdit.setFont(font)
        self.passLineEdit.setText("")
        self.passLineEdit.setObjectName("passLineEdit")
        self.signInButton = QtWidgets.QPushButton(self.centralwidget)
        self.signInButton.setGeometry(QtCore.QRect(120, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.signInButton.setFont(font)
        self.signInButton.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.signInButton.setObjectName("signInButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.signUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.signUpButton.setGeometry(QtCore.QRect(200, 251, 61, 28))
        self.signUpButton.setStyleSheet("background-color: #A3C1DA; color: blue;")
        self.signUpButton.setFlat(True)
        self.signUpButton.setObjectName("signUpButton")
        self.window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.connectButtons()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "Sign In"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.signInButton.setText(_translate("MainWindow", "Sign In"))
        self.label_4.setText(_translate("MainWindow", "No account?"))
        self.signUpButton.setText(_translate("MainWindow", "Sign Up"))

    def startUI(self):
        self.window.show()
        if self.registerUI.user.email is not None:
            self.emailLineEdit.setText(self.registerUI.user.email)
        if self.registerUI.user.password is not None:
            self.passLineEdit.setText(self.registerUI.user.password)

    def connectButtons(self):
        self.signInButton.clicked.connect(self.openPanelWindow)
        self.signUpButton.clicked.connect(self.toSignUp)

    def toSignUp(self):
        self.setInfo()
        self.registerUI.createSignupWindow()


    def setInfo(self):
        user = DBType.User.emptyUser()
        user.email = self.emailLineEdit.text()
        user.password = self.passLineEdit.text()
        self.registerUI.user = user

    def checkInfo(self):
        if self.registerUI.checkInput():
            if self.registerUI.repo.CheckUser(self.registerUI.user.email, self.registerUI.user.password):
                return True
            else:
                MainUI.MainUI.showMessage('user email or password is incorrect')
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
            self.registerUI.signInSetup = None
