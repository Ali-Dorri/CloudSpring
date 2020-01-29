from datetime import datetime
import time
import random
import string

""" User Data Type Class Definition"""


class User:
    id = None
    first_name = None
    last_name = None
    national_code = None
    email = None
    password = None
    salt = None
    registrationdate = None
    balance = None

    @classmethod
    def emptyUser(cls):
        dateString = str(datetime.now().date()).replace("-","", 10)
        return cls(id = None, First_name = None, Last_name = None, National_code = None, Email = None, Password = None
                   , Salt = randomString(10), RegistrationDate = dateString, Balance = 0)

    def __init__(self, id, First_name, Last_name,National_code, Email ,Password, Salt,RegistrationDate , Balance):
        self.id = id
        self.first_name = First_name
        self.last_name = Last_name
        self.national_code = National_code
        self.email = Email
        self.password = Password
        self.salt = Salt
        self.registrationdate = RegistrationDate
        self.balance = Balance

    @staticmethod
    def tupleToUser(userTuple):
        return User(userTuple[0], userTuple[1], userTuple[2], userTuple[3], userTuple[4], userTuple[5], userTuple[6], userTuple[7],
                    userTuple[8])


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

class ServicePacket:

    def __init__(self, packetId, createDate, endDate, os, ram, cpu, hd, bw, core = 4, otherResources = []):
        self.packetId = packetId
        self.createDate = createDate
        self.endDate = endDate
        self.os = os
        self.ram = ram
        self.cpu = cpu
        self.hd = hd
        self.bw = bw
        self.core = core
        self.otherResources = otherResources

    @staticmethod
    def tupleToPacket(packetTuple):
        return ServicePacket(packetTuple[0], packetTuple[1], packetTuple[2], packetTuple[3], packetTuple[4], packetTuple[5], packetTuple[6],
                    packetTuple[7], packetTuple[8])

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))