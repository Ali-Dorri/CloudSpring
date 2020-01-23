
from Example.DBType import User
from  datetime import datetime

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
        if(User.user_passwordhash is not None):
            # self.Cursor.execute("""SELECT NOW()::date""")
            # datetimenow = self.Cursor.fetchone()
            datetimenow = datetime.now().date()
            print("gharare print beshe")
            print(datetimenow)
            query = """INSERT INTO users(user_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate) VALUES('%s', '%s', '%s', '%s', '%s', '%s')"""\
                    % (User.user_name, User.user_national_code, User.user_email, User.user_passwordhash, User.user_salt, datetimenow)
            Query = "INSERT INTO users(user_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate) VALUES(' " + User.user_name + "',' " + User.user_national_code + " ', ' " + User.user_email + " ' ,' " + User.user_passwordhash + " ' , ' " + User.user_salt + " ' ,'" + str(datetimenow) + "')"
            print(query)
            result = self.Cursor.execute(query)
            if(result == None):
                RepositoryResult.code = True
                RepositoryResult.Error = None
                return RepositoryResult
        else :
            RepositoryResult.code = False
            RepositoryResult.Error = "Bad Request"
            return RepositoryResult


    def AddService(self,Service):
        if(Service.service_name is not None & Service.resource_id is not None & Service.stock >= 1):
            Query = "INSERT INTO services(service_name,resource_id_fk,stock) VALUES('" + Service.service_name + "'," + Service.resource_id + " ,'" + Service.stock + "')"
            result = self.Cursor.execute(Query)
            if (result == None):
                RepositoryResult.code = True
                RepositoryResult.Error = None
                return RepositoryResult
            else:
                RepositoryResult.code = False
                RepositoryResult.Error = "Bad Request"
                return RepositoryResult



    def AddUser_Service(self,User,Service,Packet_Number):
        if ( Service.service_id is not None & Service.service_name is not None & Service.resource_id is not None & Service.stock >= 1 & User.user_id is not None):
            Query =  "INSERT INTO user_services(user_id_fk,service_id_fk,resource_id_fk,created_date,end_date,packet_id) VALUES(" + User.user_id  + " , " + Service.service_id + " , " + Service.resource_id + ")"





