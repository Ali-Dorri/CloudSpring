from datetime import datetime
import time

""" User Data Type Class Definition"""


class User:
    user_name = None
    user_national_code = None
    user_passwordhash = None
    user_salt = None
    user_registrationdate = None
    user_email = None
    user_id = None

    def __init__(self, username, national_code, UserEmail ,passwordhash, salt):
        self.user_name = username
        self.user_national_code = national_code
        self.user_passwordhash = passwordhash
        self.user_salt = salt
        self.user_registrationdate = datetime.now()
        self.user_email = UserEmail


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


