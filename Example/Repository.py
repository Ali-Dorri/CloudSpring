
from Example.DBType import User


class Repository:
    Connection = None
    def __init__(self,connection):
        self.Connection = connection




    def AddUser(self,User):
        passwordhash = hash(User.user_passwordhash)
        Query = "INSERT INTO users(user_id,user_name,user_national_code,user_email,user_passwordhash,user_salt,user_registerdate) VALUES " +
         "("
        Connection.execute('')





