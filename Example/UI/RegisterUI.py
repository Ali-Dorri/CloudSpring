import psycopg2
from Example import DBType
from Example import Repository
from Example.UI.UserUI import UserUI
from Example.UI.AdminUI import AdminUI
from Example.UI import MainUI
from PyQt5 import  QtCore, QtGui, QtWidgets
from Example.UI import  SignInSetup
from Example.UI.SignInSetup import SignInSetup
from Example.UI.SignUpSetup import SignUpSetup

class UserType:
    user = 1
    admin = 2

class RegisterUI:

    def __init__(self, connection, repo):
        self.connection = connection
        self.repo = repo
        self.signInSetup = None
        self.signUpSetup = None
        self.user = DBType.User.emptyUser()

    def startUI(self):
        MainUI.MainUI.trackObject(self)
        self.createSigninWindow()

    def createSignupWindow(self):
        if self.signUpSetup is None:
            self.signUpSetup = SignUpSetup(self)
        self.signUpSetup.setupUi()
        self.signUpSetup.retranslateUi()
        self.signUpSetup.startUI()
        if self.signInSetup is not None and not self.signInSetup.window.isHidden():
            self.signInSetup.window.hide()

    def createSigninWindow(self):
        if self.signInSetup is None:
            self.signInSetup = SignInSetup(self)
        self.signInSetup.setupUi()
        self.signInSetup.retranslateUi()
        self.signInSetup.startUI()
        if self.signUpSetup is not None and not self.signUpSetup.window.isHidden():
            self.signUpSetup.window.hide()

    def checkInput(self):
        #TODO check input validation and sql injection
        #QtWidgets.QMessageBox()
        return True

        #else:
        MainUI.MainUI.showMessage('no valid input')
        return False

        pass

    def openPanelWindow(self):
        if (self.repo.isAdmin(self.user.id)):
            adminWindow = AdminUI(admin=self.user, repository=self.repo)
            adminWindow.startUI()
        else:
            userWindow = UserUI(user=self.user, repository=self.repo)
            userWindow.startUI()
