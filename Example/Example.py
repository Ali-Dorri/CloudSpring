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
         service_name VARCHAR(15) NOT NULL ,
         resource_id_fk INTEGER ,
         FOREIGN KEY (resource_id_fk) REFERENCES resources(resource_id) ,
         stock INTEGER NOT NULL
            )
        """
        ,
        """
        CREATE TABLE users(
        user_id SERIAL PRIMARY KEY NOT NULL ,
        user_name VARCHAR(50) ,
        user_national_code VARCHAR(15) ,
        user_email VARCHAR(80) ,
        user_passwordhash VARCHAR(500) ,
        user_salt VARCHAR(80) ,
        user_registerdate DATE NULL 
        )
        """
        ,
        """
        CREATE TABLE user_services(
        user_id_fk INTEGER ,
        FOREIGN KEY (user_id_fk) REFERENCES users(user_id) ,
        service_id_fk INTEGER ,
        FOREIGN KEY (service_id_fk) REFERENCES services(service_id) ,
        resource_id_fk INTEGER,
        FOREIGN KEY (resource_id_fk) REFERENCES resources(resource_id) ,
        created_date DATE ,
        end_date DATE NULL ,
        packet_id INTEGER ,
        PRIMARY KEY(user_id_fk,packet_id)
        )
        """
        ,
        """
        CREATE TABLE user_additional(
        additional_id SERIAL PRIMARY KEY ,
        additional_name VARCHAR(50)
        )
        """
        ,
        """
        CREATE TABLE user_detail(
        user_id_fk INTEGER ,
        FOREIGN KEY (user_id_fk) REFERENCES users(user_id) ,
        user_additional_id_fk INTEGER ,
        FOREIGN KEY (user_additional_id_fk) REFERENCES user_additional(additional_id) ,
        content VARCHAR(500) NULL ,
        context_name VARCHAR(50) 
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
