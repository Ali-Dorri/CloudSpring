import psycopg2
from Example import DBType
from Example import Repository
from Example.UI.UserUI import UserUI
from Example.UI.AdminUI import AdminUI
from Example.UI import MainUI
from PyQt5 import  QtCore, QtGui, QtWidgets
from Example.UI import  SignInSetup
from Example.UI.SignInSetup import SignInSetup

class UserType:
    user = 1
    admin = 2

class RegisterUI:

    def __init__(self, connection, repo):
        self.connection = connection
        self.repo = repo
        self.signinWindow = None
        self.signupWindow = None
        #user info
        self.first_name = None
        self.last_name = None
        self.national_code = None
        self.email = None
        self.registrationdate = None
        self.email = None
        self.password = None

    def startUI(self):
        MainUI.MainUI.storeObject(self)
        self.createSigninWindiow()
        # self.email = 'jafar1370@mashti.com'
        # self.password = 'sample password'
        # self.openPanelWindow()

    def createSignupWindiow(self):
        if self.signupWindow is None:
            self.signupWindow = QtWidgets.QMainWindow()

        
        self.setupSignup()
        self.retranslateSignup()
        self.signupWindow.show()
        if self.signinWindow is not None and not self.signinWindow.isHidden():
            self.signinWindow.hide()

    def setupSignup(self):
        #TODO connect createSigninWindow() to signin button
        self.signupWindow.setObjectName("Register UI")
        self.signupWindow.resize(350, 517)
        self.signupWindow.setStyleSheet("")
        self.signupWindow.setWindowTitle("Register UI")

        #other setup








    def retranslateSignup(self):
        pass

    def createSigninWindiow(self):
        if self.signinWindow is None:
            self.signinWindow = QtWidgets.QMainWindow()

        siginInSetup = SignInSetup.SignInSetup(0)
        SignInSetup.setupUi(self.signinWindow)
        SignInSetup.retranslateUi(self.signinWindow)
        self.signinWindow.show()
        if self.signupWindow is not None and not self.signupWindow.isHidden():
            self.signupWindow.hide()

    def setupSignin(self):
        #TODO connect createSignupWindow() to signup button




    def retranslateSignin(self):
        self.signinTitle.setText("Sign In")
        self.label_2.setText("Email:")
        self.label_3.setText( "Password:")
        self.pushButton.setText("Sign In")
        self.label_4.setText("No account?")
        self.pushButton_2.setText("Sign Up")

    def setInfo(self):
        #TODO check user inputs for validation and sql injection
        pass

    def openPanelWindow(self):
        self.setInfo()
        if self.repo.CheckUser(self.email, self.password):
            userTuples = self.repo.GetUser(self.email)
            user = DBType.User.tupleToUser(userTuples[0])
            if (self.repo.isAdmin(user.id)):
                adminWindow = AdminUI(admin=user, repository=self.repo)
                adminWindow.startUI()
            else:
                userWindow = UserUI(user=user, repository=self.repo)
                userWindow.startUI()

