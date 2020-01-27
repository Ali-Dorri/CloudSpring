# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amir\Desktop\qt code\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from Example import config
from Example import Repository
from Example import DBType

Create_Tables_Commands=(
        """ 
        CREATE TABLE resources (
            resource_id  SERIAL PRIMARY KEY ,
            resource_name VARCHAR(15) NOT NULL
        ) 
        """
        ,
        """
         CREATE TABLE services(
         service_id  SERIAL PRIMARY KEY ,
         Value VARCHAR(15) NOT NULL ,
         resource_id_fk INTEGER ,
         FOREIGN KEY (resource_id_fk) REFERENCES resources(resource_id) ,
         stock INTEGER NOT NULL
            )
        """
        ,
        """
        CREATE TABLE users(
        user_id SERIAL PRIMARY KEY NOT NULL ,
        first_name VARCHAR(50) ,
        last_name VARCHAR(80) ,
        user_national_code VARCHAR(15) ,
        user_email VARCHAR(80) ,
        user_passwordhash VARCHAR(500) ,
        user_salt VARCHAR(80) ,
        user_registerdate DATE NULL ,
        Balance INTEGER
        )
        """
        ,
        """
        CREATE TABLE user_service_info(
        order_id_pk SERIAL INTEGER ,
        user_id_fk INTEGER ,
        PRIMARY KEY(order_id_pk),
        FOREIGN KEY (user_id_fk) REFERENCES users(user_id) ,
        created_date DATE ,
        end_date DATE NULL ,
        ssh_key VARCHAR(800) ,
        ssh_name VARCHAR(500)
        )
        """
        ,
        """
        CREATE TABLE user_services(
        service_id_fk INTEGER ,
        FOREIGN KEY (service_id_fk) REFERENCES services(service_id) ,
        order_id INTEGER ,
        FOREIGN KEY (order_id) REFERENCES user_service_info(order_id_pk) ,
        PRIMARY KEY(service_id_fk,order_id)
        )
        """
        ,

        """
        CREATE TABLE ticket(
        ticket_id SERIAL,
        PRIMARY KEY(ticket_id),
        user_id_fk INTEGER ,
        FOREIGN KEY (user_id_fk) REFERENCES users(user_id) ,
        created_date DATE ,
        content VARCHAR(500) ,
        reply_date DATE ,
        reply_content VARCHAR(500),
        status INTEGER
        )
        """
    )

Connection = None


def connecttodb():
        con = None
        try:
            params = config.config()
            print('connecting to PostgreSql DB ...')
            con = psycopg2.connect(port="5400",host="localhost",database="CloudSpring", user="postgres", password="rememberme")
            # create cursor
            cursor = con.cursor()
            global Connection
            Connection = con
            print('Connected to PostgreSql DB !')
            #sqlservercommand = Create_Tables_Commands
            #for command in sqlservercommand:
             #   cursor.execute(command)

            #con.commit()
            #print("Commands Executed Successfully")
            #insert = "INSERT INTO resources (resource_id,resource_name) VALUES (2,'OS')"
            #cursor.execute(insert)
            #cursor.close()
            #con.commit()
            db_version = cursor.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is None:
                con.close()






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.firstbutton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "first button"))

    def firstbutton(self):
        print ("Hello-World Amir")


def AddUser_Service_Info():
        queries = ("""INSERT INTO user_service_info (order_id_pk, user_id_fk,created_date,end_date,ssh_key,ssh_name) VALUES (1, 1,'20120315','20130426','7753sdfxcv','name_1')""",
                 """INSERT INTO user_service_info (order_id_pk, user_id_fk,created_date,end_date,ssh_key,ssh_name) VALUES (2, 2,'20130415','20140315','4512asxczx48','name_2')""",
                 """INSERT INTO user_service_info (order_id_pk, user_id_fk,created_date,end_date,ssh_key,ssh_name) VALUES (3, 1,'20120705','20140517','xzxc155a54','name_3')""")
        global Connection
        for qeury in queries:
            Connection.cursor().execute(qeury)
            Connection.commit()
            print("resources successfully added")


def AddResources():
    queries = ("""INSERT INTO resources (resource_name) VALUES ('OS')""",
               """INSERT INTO resources (resource_name) VALUES ('RAM')""",
               """INSERT INTO resources (resource_name) VALUES ('CPU FREQUENCY')""",
               """INSERT INTO resources (resource_name) VALUES ('HD')""",
               """INSERT INTO resources (resource_name) VALUES ('BANDWIDTH')""",
               """INSERT INTO resources (resource_name) VALUES ('CPU CORE')""")
    global Connection
    for qeury in queries:
        Connection.cursor().execute(qeury)
        Connection.commit()
        print("resources successfully added")

def DELETEALLRESOIRCE():
    query = "DELETE FROM resources WHERE resource_id > 0"
    global Connection
    try:
        Connection.cursor().execute(query)
        Connection.commit()
        print("All Resources Deleted Successfuly")
    except(Exception) as error:
        print(error)

def AddServices():
    queries = ("""INSERT INTO resources (resource_name) VALUES ('OS')""",
               """INSERT INTO resources (resource_name) VALUES ('RAM')""",
               """INSERT INTO resources (resource_name) VALUES ('CPU FREQUENCY')""",
               """INSERT INTO resources (resource_name) VALUES ('HD')""",
               """INSERT INTO resources (resource_name) VALUES ('BANDWIDTH')""",
               """INSERT INTO resources (resource_name) VALUES ('CPU CORE')""")
    global Connection
    for qeury in queries:
        Connection.cursor().execute(qeury)
        Connection.commit()
        print("resources successfully added")



def AddUserEmailTriger():
    query = """CREATE  TRIGGER  CheckUserEmail
	    BEFORE INSERT ON users 
	    REFERENCING NEW ROW AS NewTuple
	    FOR EACH ROW
	    WHEN (NewTuple.user_email NOT IN (SELECT user_email FROM users))
	    INSERT INTO users (first_name,last_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate,balance) VALUES (NewTuple.first_name,NewTuple.last_name,NewTuple.user_national_code,NewTuple.user_email,NewTuple.user_passwordhash,NewTuple.user_salt,NewTuple.user_registerdate,NewTuple.balance);"""
    global Connection
    try:
        Connection.cursor().execute(query)
        Connection.commit()
        print("Trigger Added Successfully")
    except(Exception) as error:
        print(error)
    
if __name__ == "__main__":
    import sys
    connecttodb()
    #AddUser_Service_Info()
    #Repo = Repository.Repository(Connection)
    #user = DBType.User('hossein','sharifian','045874425','hossein@yahoo.com','hossein1234','f1nd1ngn3m0','20120618','25000')
    user = DBType.User('Amir', 'sharifian', '045887425', 'Amir@yahoo.com', 'Amir1234', 'f1nd1ngn3m0','20120618', '25000')
    #user = DBType.User('mahdi', 'kazemi', '045887425', 'asf@yahoo.com', 'kazemi1234', 'f1nd1ngn3m0', '20120618','25000')
    #ticket = DBType.Ticket('1',None,'the content of ticket',None,None,'1')
    AddUserEmailTriger()
    #Connection.cursor.execute()
    #result = Repository.RepositoryResult()
    #result = Repo.AddUser(user)
    #result = Repo.GetCurrentUserServices(user)
    #result = Repo.CheckUser(user.email,"hossein1234")
    #Repo.GetAvailableOs()
    #services_to_add = [2,4,7,8,12,13]
    #result = Repo.AddUserService(services_to_add,user.email,"gdf54g54dfgdg6","sample_ssh_name")
    #result = Repo.AddTicket(ticket)
    #result = Repo.UpdateUserByEmail("85000","asf@yahoo.com")
    #result = Repo.GetUser("asf@yahoo.com")
    #print(result)

    """app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
