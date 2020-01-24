# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amir\Desktop\qt code\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from config import config

help(config)
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
        order_id_pk INTEGER ,
        PRIMARY KEY(order_id_pk),
        created_date DATE ,
        end_date DATE NULL ,
        ssh_key VARCHAR(800) ,
        ssh_name VARCHAR(500)
        )
        """
        ,
        """
        CREATE TABLE user_services(
        user_id_fk INTEGER ,
        FOREIGN KEY (user_id_fk) REFERENCES users(user_id) ,
        service_id_fk INTEGER ,
        FOREIGN KEY (service_id_fk) REFERENCES services(service_id) ,
        order_id INTEGER ,
        FOREIGN KEY (order_id) REFERENCES user_service_info(order_id_pk) ,
        PRIMARY KEY(user_id_fk,service_id_fk,order_id)
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
            params = config()
            print('connecting to PostgreSql DB ...')
            con = psycopg2.connect(port="5432",host="localhost",database="CloudSpring", user="postgres", password="postgres")
            print('after .connct')
            # create cursor
            cursor = con.cursor()
            Connection = con
            print('Connected to PostgreSql DB !')
            """sqlservercommand = Create_Tables_Commands
            for command in sqlservercommand:
                cursor.execute(command)

            con.commit()"""
            print('commands execution done ! :)')
            db_version = cursor.fetchone()
            print(db_version)

            # close the communication with the PostgreSQL
            # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is None:
                con.close()
                print('DB Cnnection Closed !')





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

    
if __name__ == "__main__":
    import sys
    connecttodb()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
