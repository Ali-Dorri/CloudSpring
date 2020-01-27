
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
            print("gharare print beshe")
            print(datetimenow)
            temp = User.password + User.salt
            passwordhash = hashlib.md5(temp.encode())
            print("Final Password hash is : %s"%(passwordhash.hexdigest()))
            finalpasswordhash = passwordhash.hexdigest()
            query = """INSERT INTO users (first_name,last_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate,balance) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');"""\
                    % (User.first_name,User.last_name,User.national_code,User.email,finalpasswordhash,User.salt,User.registrationdate,User.balance)
            #Query = "INSERT INTO users(user_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate) VALUES(' " + User.user_name + "',' " + User.user_national_code + " ', ' " + User.user_email + " ' ,' " + User.user_passwordhash + " ' , ' " + User.user_salt + " ' ,'" + str(datetimenow) + "')"
            print(query)
            try:
                result = self.Cursor.execute(query)
                self.DBConnection.commit()
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






    def CheckUser(self,username,password):
        query = """SELECT user_salt FROM users U WHERE U.user_email = '%s'""" %(username)
        print(query)
        self.Cursor.execute(query)
        salt = self.Cursor.fetchone()[0]
        print(salt)
        if(salt is None):
            return False
        else:
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
            print(query)
            try:
                self.Cursor.execute(query)
                result = self.Cursor.fetchall()
                print(result)
                return result
            except (Exception) as error:
                print(error)
                return False



    def GetUserId(self,user_email):
        if(user_email is not None):
            getuseridquery = """SELECT user_id FROM users U WHERE U.user_email = '%s'""" % (user_email)
            print(getuseridquery)
            try:
                self.Cursor.execute(getuseridquery)
                result = self.Cursor.fetchone()[0]
                return result
            except (Exception) as error:
                print(error)
                return False


    def GetUserPacket(self,user_id):
        if(user_id is not None):
            query = """SELECT order_id_pk FROM user_service_info U WHERE U.user_id_fk = '%s'"""%(user_id)
            print(query)
            try:
                self.Cursor.execute(query)
                result = self.Cursor.fetchall()
                return result
            except (Exception) as error:
                print(error)
                return False


    def GetCurrentUserServices(self,user_email):
        if(user_email is not None):
            user_id = self.GetUserId(user_email)
            print(user_id)
            packtids = None
            packtids = self.GetUserPacket(user_id)
            for packet_id in packtids:
                print(packet_id)
                if(packet_id != []):
                    query = """SELECT service_id_fk FROM user_services U WHERE U.order_id = '%s' ORDER BY service_id_fk"""%(packet_id)
                    print(query)
                    try:
                        self.Cursor.execute(query)
                        result = self.Cursor.fetchall()
                        print(result)
                    except (Exception) as error:
                        print(error)
                        return False



    def GetCurrentUserPackt(self,user_email):
        if(user_email is not None):
            result = self.GetUserId(User.email)
            print(result)
            packtids = self.GetUserPacket(result)
            return packtids





    def UpdateUserServices(self,new_services,packet_id):
        if(new_services is not None and packet_id is not None):
            query = """SELECT service_id_fk FROM user_services U WHERE U.order_id = '%s' ORDER BY service_id_fk"""%(packet_id)
            count_query = """SELECT COUNT(service_id_fk) FROM user_services U WHERE U.order_id = '%s'"""%(packet_id)
            print(query)
            try:
                self.Cursor.execute(query)
                old_services = self.Cursor.fetchall()
                li = []
                j=0
                for j in old_services:
                    li.append(j[0])
                self.Cursor.execute(count_query)
                count_number = self.Cursor.fetchone()
                print(li)
                print(new_services)
                i=0
                for i in range(count_number[0]):
                    final_query = """UPDATE user_services SET service_id_fk = '%s' WHERE service_id_fk = '%s' And order_id = '%s';"""%(new_services[i],li[i],packet_id)
                    print(final_query)
                    self.Cursor.execute(final_query)
                    self.DBConnection.commit()
                    print("UPDATE SUCCESSFULLY DONE !")
            except (Exception) as error:
                print(error)
                return False







    "to add couple of new services with new packet_id for given user"
    def AddUserService(self,services,user_email,ssh_key,ssh_name):
        if(services is not None):
            user_id = self.GetUserId(user_email)
            query = """SELECT MAX(order_id_pk) FROM user_service_info """
            print(query)
            try:
                self.Cursor.execute(query)
                maximumorder_id = self.Cursor.fetchone()[0]
                maximumorder_id = maximumorder_id +1
                print(maximumorder_id)
                datetimenow = datetime.now().date()
                user_id = self.GetUserId(user_email)
                adduserpacketquery = """INSERT INTO user_service_info (order_id_pk, user_id_fk,created_date,end_date,ssh_key,ssh_name) VALUES ('%s','%s','%s','%s','%s','%s')"""\
                %(maximumorder_id,user_id,datetimenow,datetimenow,ssh_key,ssh_name)
                print(adduserpacketquery)
                self.Cursor.execute(adduserpacketquery)
                self.DBConnection.commit()
                for service in services:
                    add_services_to_packet_query = """INSERT INTO user_services (service_id_fk,order_id) VALUES ('%s','%s')"""%(service,maximumorder_id)
                    self.Cursor.execute(add_services_to_packet_query)
                self.DBConnection.commit()
            except (Exception) as error:
                print(error)
                return False




    def GetAvailableResources(self,Resource_id):
        if(Resource_id is not None):
            query = """SELECT service_id FROM services S WHERE S.resource_id_fk = '%s' and S.stock > 1"""%(Resource_id)
            try:
                self.Cursor.execute(query)
                result = self.Cursor.fetchall()
                print(result)
                return result
            except (Exception) as error:
                print(error)
                return False


    def GetUserBalance(self,user_email):
        if(user_email is not None):
            user_id = self.GetUserId(user_email)
            query = """SELECT balance FROM users U WHERE U.user_id = '%s'"""%(user_id)
            print(query)
            try:
                self.Cursor.execute(query)
                result = self.Cursor.fetchone()[0]
                print(result)
                return result
            except(Exception) as Error:
                print(Error)
                return False



    def UpdateUserBalance(self,user_email,new_user_balance):
        if(user_email is not None and new_user_balance is not None):
            self.UpdateUserByEmail(new_user_balance,user_email)





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






    #def AddUser_Service(self,User,Service,Packet_Number):
     #   if ( Service.service_id is not None & Service.service_name is not None & Service.resource_id is not None & Service.stock >= 1 & User.user_id is not None):
      #      Query =  "INSERT INTO user_services(user_id_fk,service_id_fk,resource_id_fk,created_date,end_date,packet_id) VALUES(" + User.user_id  + " , " + Service.service_id + " , " + Service.resource_id + ")"





