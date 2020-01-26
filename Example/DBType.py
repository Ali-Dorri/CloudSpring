from datetime import datetime
import time

""" User Data Type Class Definition"""


class User:
    first_name = None
    last_name = None
    national_code = None
    email = None
    password = None
    salt = None
    registrationdate = None
    balance = None

    def __init__(self, First_name, Last_name,National_code, Email ,Password, Salt,RegistrationDate , Balance):
        self.first_name = First_name
        self.last_name = Last_name
        self.national_code = National_code
        self.email = Email
        self.password = Password
        self.salt = Salt
        self.registrationdate = RegistrationDate
        self.balance = Balance

""" Service Data Type Class Definition"""


class Service:
    service_name = None
    resource_id = None
    stock = None
    service_id = None

    def __init__(self, ServiceName, ResourceId, Stock):
        self.service_name = ServiceName
        self.resource_id = ResourceId
        self.stock = Stock


""" Resource Data Type Class Definition"""


class Resource:
    resource_name = None

    def __init__(self, ResourceName):
        self.resource_name = ResourceName


"""Ticket Class Type"""

class Ticket:
    User_id = None
    Created_date = None
    Content = None
    Reply_date = None
    Reply_content = None
    Status = None

    def __init__(self,user_id,created_date,content,reply_date,reply_content,status):
        self.User_id = user_id
        self.Created_date = created_date
        self.Content = content
        self.Reply_date = reply_date
        self.Reply_content = reply_content
        self.Status = status