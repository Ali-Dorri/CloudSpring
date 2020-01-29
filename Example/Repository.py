
from Example.DBType import User
from  datetime import datetime
import hashlib

class RepositoryResult:
    code = None
    Error = None



class Repository:
    DBConnection = None
    Cursor = None
    def __init__(self,connection):
        self.DBConnection = connection
        self.Cursor = self.DBConnection.cursor()




    def AddUser(self,User):
        if(User.password is not None):
            # self.Cursor.execute("""SELECT NOW()::date""")
            # datetimenow = self.Cursor.fetchone()
            datetimenow = datetime.now().date()
            print(datetimenow)
            temp = User.password + User.salt
            passwordhash = hashlib.md5(temp.encode())
            print("Final Password hash is : %s"%(passwordhash.hexdigest()))
            finalpasswordhash = passwordhash.hexdigest()
            query = """INSERT INTO USERS (first_name,last_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate,balance) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');"""\
                    % (User.first_name,User.last_name,User.national_code,User.email,finalpasswordhash,User.salt,User.registrationdate,User.balance)
            #Query = "INSERT INTO users(user_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate) VALUES(' " + User.user_name + "',' " + User.user_national_code + " ', ' " + User.user_email + " ' ,' " + User.user_passwordhash + " ' , ' " + User.user_salt + " ' ,'" + str(datetimenow) + "')"
            print(query)
            try:
                result = self.Cursor.execute(query)
                self.DBConnection.commit()

                """check addition was succeeded"""
                query = """SELECT user_id FROM users WHERE user_email = '%s'"""%(User.email)
                self.Cursor.execute(query)
                userTuple = self.Cursor.fetchone()
                return userTuple is not None
            except (Exception) as error:
                print(error)
            #finally:
             #   if self.DBConnection is None:
              #      self.Cursor.close()
            #if(result == None):
                #RepositoryResult.code = True
                #RepositoryResult.Error = None
                #return RepositoryResult
        #else :
            #RepositoryResult.code = False
            #RepositoryResult.Error = "Bad Request"
            #return RepositoryResult
            return False






    def CheckUser(self,username,password):
        if username is None or password is None:
            return False

        query = """SELECT user_salt FROM users U WHERE U.user_email = '%s'""" %(username)
        print(query)
        self.Cursor.execute(query)
        saltEntity = self.Cursor.fetchone()
        if saltEntity is None:
            return False
        else:
            salt = saltEntity[0]
            print(salt)
            temp = password + salt
            passwordhash = hashlib.md5(temp.encode())
            print("Run Checkuser")
            finalpasswordhash = passwordhash.hexdigest()
            checkquery = """SELECT user_email FROM users U WHERE U.user_email = '%s' AND U.user_passwordhash = '%s' """ %(username,finalpasswordhash)
            print(checkquery)
            self.Cursor.execute(checkquery)
            entity = self.Cursor.fetchone()[0]
            if(entity is None):
                return False
            else:
                print(entity)
                return True

    def isAdminByEmail(self, userEmail):
        userId = self.GetUser(userEmail)[0]
        return self.isAdmin(userId)

    def isAdmin(self, userId):
        query = """SELECT admin_id_pk FROM admins WHERE user_id_fk = '%s'""" % (userId)
        self.Cursor.execute(query)
        entity = self.Cursor.fetchone()
        if entity is None:
            return False
        else:
            return True


    def AddTicket(self,Ticket):
        if(Ticket.Content is not None):
            datetimenow = datetime.now().date()
            query = """INSERT INTO ticket (user_id_fk,created_date,content,reply_date,reply_content,status) VALUES ('%s','%s','%s','%s','%s','%s')"""\
            %(Ticket.User_id,datetimenow,Ticket.Content,datetimenow,None,'1')
            print(query)
            try:
                self.Cursor.execute(query)
                self.DBConnection.commit()
                return True
            except (Exception) as error:
                print(error)
        else:
            return False



    def UpdateUser(self,User):
        if(User.balance is not None):
            query = """UPDATE users U SET U.balance = '%s' WHERE U.user_email = '%s'"""%(User.balance,User.email)
            print(query)
            try:
                self.Cursor.execute(query)
                self.DBConnection.commit()
                return True
            except (Exception) as error:
                print(error)



    def UpdateUserByEmail(self, balance,user_email):
        if (balance is not None):
            query = """UPDATE users SET balance = '%s' WHERE user_email = '%s'""" % (balance,user_email)
            print(query)
            try:
                self.Cursor.execute(query)
                self.DBConnection.commit()
                return True
            except (Exception) as error:
                print(error)
                return False



    def GetUser(self,user_email):
        if(user_email is not None):
            query="""SELECT * From users U Where U.user_email = '%s' """%(user_email)
            try:
                self.Cursor.execute(query)
                result = self.Cursor.fetchall()
                print(result)
                return result
            except (Exception) as error:
                print(error)
                return False



    def AddService(self,Service):
        if(Service.service_name is not None & Service.resource_id is not None & Service.stock >= 1):
            query = """INSERT INTO services(service_name,resource_id_fk,stock) VALUES('%s','%s','%s')"""%(Service.service_name,Service.resource_id,Service.stock)
            print(query)
            try:
                self.Cursor.execute(query)
                self.DBConnection.commit()
                return True
            except (Exception) as error:
                print(error)
                return False



    def AddUser_Service(self,User,Service,Packet_Number):
        if ( Service.service_id is not None & Service.service_name is not None & Service.resource_id is not None & Service.stock >= 1 & User.user_id is not None):
            Query =  "INSERT INTO user_services(user_id_fk,service_id_fk,resource_id_fk,created_date,end_date,packet_id) VALUES(" + User.user_id  + " , " + Service.service_id + " , " + Service.resource_id + ")"





