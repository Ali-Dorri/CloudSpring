from Example.DBType import User
from datetime import datetime
import hashlib


class RepositoryResult:
    code = None
    Error = None


class AdminRepository:
    DBConnection = None
    Cursor = None

    def __init__(self, connection):
        self.DBConnection = connection
        self.Cursor = self.DBConnection.cursor()

    # first page for showing all users details on (user table) except pass_hash and salt
    def GetAllUser(self):
        query = """Select user_id , first_name , last_name , user_national_code , user_email , user_registerdate , balance from users"""
        try:
            self.Cursor.execute(query)
            result = self.Cursor.fetchall()
            return result
        except (Exception) as error:
            print(error)
            return False

    # by selecting on each user it will show all the services that user have bought so far
    def GetUserServices(self, userID):
        query = """select order_id_pk , resource_name,value , created_date , end_date
from user_service_info, user_services , services , resources
where user_id_fk = '%s' and order_id_pk = order_id and service_id_fk = service_id and resource_id = resource_id_fk""" % (
            userID)
        try:
            self.Cursor.execute(query)
            result = self.Cursor.fetchall()
            return result
        except (Exception) as error:
            print(error)
            return False

    # by clicking on each service remove button it will remove the service from the table with selected order_id
    def RemoveUserService(self, userId, orderId):
        query = """DELETE FROM user_services WHERE order_id = (select order_id_pk from user_service_info where user_id_fk = '%s' and order_id_pk = '%s');
DELETE FROM user_service_info WHERE user_id_fk = '%s' and order_id_pk = '%s';""" % (userId, orderId, userId, orderId)
        try:
            self.Cursor.execute(query)
        except (Exception) as error:
            print(error)
            return False
        self.DBConnection.commit()
        return True

    # by clicking on each service edit button it will send the user to edit page , then the edit page give ORDER_ID + a list of new values AND oldvalues to the method below :
    def EditUserService(self, orderId, oldValues, newValues):
        i = 0
        while i < len(oldValues):
            oldVal = oldValues[i]
            newVal = newValues[i]
            query = """UPDATE user_services
            SET service_id_fk = %s
            WHERE order_id = %s and service_id_fk = %s;""" % (newVal, orderId, oldVal)
            try:
                self.Cursor.execute(query)
            except (Exception) as error:
                print(error)
                return False
            i += 1
        self.DBConnection.commit()
        return True

    # this query will show all services available in system with their stock number and then
    # admin can either edit stock number for each service or add a new service
    def GetAvailableServices(self):
        query = """
        SELECT service_id,resource_name , value , stock FROM services , resources 
        WHERE resource_id_fk = resource_id """
        try:
            self.Cursor.execute(query)
            result = self.Cursor.fetchall()
            return result
        except (Exception) as error:
            print(error)
            return False

    #  edit stock query
    def EditServiceStock(self, serviceId, stock):
        query = """UPDATE services
        SET stock = %s
        WHERE service_id = %s;""" % (stock, serviceId)
        try:
            self.Cursor.execute(query)
        except (Exception) as error:
            print(error)
            return False
        self.DBConnection.commit()
        return True

    # adding new service to an existing resource
    def AddNewService(self, value, resourceId, stock):
        query = """INSERT INTO services (value,resource_id_fk,stock)
        VALUES ('%s',%s, %s);""" % (value, resourceId, stock)
        print(query)
        try:
            self.Cursor.execute(query)
        except (Exception) as error:
            print(error)
            return False
        self.DBConnection.commit()
        return True

    # this query shows all the ticket with status 1 -> waiting for reply
    def ShowTickets(self):
        query = """SELECT ticket_id ,  first_name , last_name ,content, created_date 
FROM users , ticket 
WHERE status = 1 AND user_id_fk = user_id"""
        try:
            self.Cursor.execute(query)
            result = self.Cursor.fetchall()
            return result
        except (Exception) as error:
            print(error)
            return False

    # in this tab admin can see all the ticket with status 2 or 3
    def ShowRepliedTickets(self):
        query = """SELECT ticket_id ,  first_name , last_name , created_date , content , reply_date , reply_content , status
        FROM users , ticket 
        WHERE status != 1 AND user_id_fk = user_id"""
        try:
            self.Cursor.execute(query)
            result = self.Cursor.fetchall()
            return result
        except (Exception) as error:
            print(error)
            return False

    # here admin can send a reply to for specefic ticket id
    def SendReply(self, replyText, ticketId):
        query = """UPDATE ticket
SET reply_date = CURRENT_DATE , reply_content = '%s' , status = 2
WHERE ticket_id = %s;""" % (replyText, ticketId)
        try:
            self.Cursor.execute(query)
        except (Exception) as error:
            print(error)
            return False
        self.DBConnection.commit()
        return True


    # here admin can deny a ticket
    def DenyTicket(self, ticketId):
        query = """UPDATE ticket
SET reply_date = CURRENT_DATE , reply_content = 'Sorry ! your request has been denied' , status = 3
WHERE ticket_id = %s;""" % (ticketId)
        try:
            self.Cursor.execute(query)
        except (Exception) as error:
            print(error)
            return False
        self.DBConnection.commit()
        return True
