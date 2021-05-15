import os,sys,pymysql,frequent
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


class Connection():
    def __init__(self):
        self.connection = pymysql.connect(
        host,
        user,
        password,
        database
)
        # self.cursor = self.connection.cursor()

    def greeting(self):
        print("Successfully opened Database", self.cursor)
        
        
##### CREATE DB / TABLES ######
class Create_Tables(Connection):
    def __init__(self):
        super().__init__()
    
    def create_table(self, menu_name):
        self.cursor = self.connection.cursor()
        
        if menu_name == "Product":
            sql = "create table Products (prod_id INT NOT NULL AUTO_INCREMENT, prod_name VARCHAR(255), prod_price FLOAT, PRIMARY KEY (prod_id));"
            self.cursor.connection(sql)
            self.connection.commit()
            
        if menu_name == "Courier":
            sql = "create table Couriers (c_id INT NOT NULL AUTO_INCREMENT, c_name VARCHAR(255), c_number BIGINT, PRIMARY KEY (c_id));"
            self.cursor.connection(sql)
            self.connection.commit()
            
        if menu_name == "Order":
            sql = "create table Orders (order_id INT NOT NULL AUTO_INCREMENT, order_name VARCHAR(255), order_add VARCHAR(255), order_phone INT, order_courier VARCHAR(255), order_status VARCHAR(255), order_items VARCHAR(255), PRIMARY KEY (order_id));"
            self.cursor.connection(sql)
            self.connection.commit()

########### LOAD FUNCTIONS ###############

class Load_From_Table(Connection):
    def __init__(self):
        super().__init__()
    
    def get_previous_attr(self, table, index, list):
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        
        if table == "Courier":
            sql = "select c_name, c_number from Couriers where c_id = {}".format(index)
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            list.clear()
            for row in myresult:
                list.append(row)
            
            # cursor.close()
            # connection.close()
            
        elif table == "Product":
            sql = "select prod_name, prod_price from Products where prod_id = {}".format(index)
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            list.clear()
            for row in myresult:
                list.append(row)
                    
            # cursor.close()
            # connection.close()    
            
        elif table == "Order":
            sql = "SELECT order_name,order_add,order_phone,order_courier,order_status,order_items FROM Orders where order_id = {}".format(str(index))
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            list.clear()
            for row in myresult:
                list.append(row)
            
            # cursor.close()
            # connection.close()
            
    def get_ids_from_db(self, table, list):
        self.cursor = self.connection.cursor()

        if table == "Courier":
            sql = "SELECT c_id FROM Couriers"
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            list.clear()
            for id in myresult:
                list.append(id[0])
                
        elif table == "Product":
            sql = "SELECT prod_id FROM Products"
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            list.clear()
            for id in myresult:
                list.append(id[0])
                
        elif table == "Order":
            sql = "SELECT order_id FROM Orders"
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            list.clear()
            for id in myresult:
                list.append(id[0])
        

############# DISPLAY ITEMS ############
class Display_Items(Connection):
    def __init__(self):
        super().__init__()
        
    def display_items(self,table):
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM {}s'.format(str(table)))
        rows = self.cursor.fetchall()
        for row in rows:
            if table == "Product":
                print(f'{str(row[0])}: {row[1]} - £{row[2]}')
        
            elif table == "Courier":
                print(f'{str(row[0])}: {row[1]} - {row[2]}')
            
            elif table == "Order":
                print(f'{str(row[0])}- Customer Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {str(row[4])}, Status: {row[5]}, Items: {row[6]}')
        # cursor.close()
        # connection.close()

    def display_item_at_index(self, menu_name, index):
        self.cursor = self.connection.cursor()
        if menu_name == "Order":
            self.cursor.execute('SELECT * FROM {}s WHERE order_id = {}'.format(str(menu_name, index)))    
            rows = self.cursor.fetchall()
            for row in rows:
                print(f'{str(row[0])}- Customer Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {str(row[4])}, Status: {row[5]}, Items: {row[6]}')

        elif menu_name == "Product":
            self.cursor.execute('SELECT * FROM {}s WHERE prod_id = {}'.format(str(menu_name,index)))
            rows = self.cursor.fetchall()
            for row in rows:
                print(f'{str(row[0])}: {row[1]} - £{row[2]}')
        
        elif menu_name == "Courier":
            self.cursor.execute('SELECT * FROM {}s WHERE c_id = {}'.format(str(menu_name, index)))
            rows = self.cursor.fetchall()
            for row in rows:
                print(f'{str(row[0])}: {row[1]} - {row[2]}')
    # cursor.close()
    # connection.close()

########## ADD ITEM TO DB ############

class alter_item(Connection):
    def __init__(self):
        super().__init__()

    def add_item_to_db(self,menu_name,name,attribute):
        self.cursor = self.connection.cursor()
        if menu_name == "Product":
            sql = "INSERT INTO Products (prod_name, prod_price) VALUES (%s, %s)"
            val = (name, attribute)
            
        elif menu_name == "Courier":
            sql = "INSERT INTO Couriers (c_name, c_number) VALUES (%s, %s)"
            val = (name, attribute)
            
        self.cursor.execute(sql, val)
        self.connection.commit()
    # cursor.close()
    # connection.close()
        
    #################### UPDATE ITEMS ###########################
    def update_item(self, menu_name, index, name, attribute):
        self.cursor = self.connection.cursor()
        frequent.clear()
        if menu_name == "Product":
            sql = "UPDATE Products SET prod_name = '{}', prod_price = '{}' WHERE prod_id = {}".format(name, attribute, index)
        
        elif menu_name == "Courier":
            sql = "UPDATE Couriers SET c_name = '{}', c_number = '{}' WHERE c_id = {}".format(name, attribute, index)
        
        self.cursor.execute(sql)
        self.connection.commit()
    # cursor.close()
    # connection.close()

############### DELETE ITEMS ###################
    def delete_item(self,menu_name,item_index):
        self.cursor = self.connection.cursor()
        if menu_name == "Product":
            sql = f"DELETE FROM Products WHERE prod_id = {item_index}"
        elif menu_name == "Courier":
            sql = f"DELETE FROM Couriers WHERE c_id = {item_index}"
        elif menu_name == "Order":
            sql = f"DELETE FROM Orders WHERE order_id = {item_index}"
            

        self.cursor.execute(sql)
        self.connection.commit()
    # cursor.close()
    # connection.close()
    
############ ADD ORDERS #############################
class Alter_Orders(Connection):
    def __init__(self):
        super().__init__()
        
    def add_order_to_db(self,name,address,phone,courier,status,items):
        self.cursor = self.connection.cursor()
        sql = "INSERT INTO Orders (order_name, order_add, order_phone, order_courier, order_status, order_items) VALUES ('{}', '{}', '{}', {}, '{}', '{}')".format(name,address,phone,courier,status,items)
        self.cursor.execute(sql)
        

    ############# UPDATE ORDER STATUS #####################

    def update_order_status_seperate(self,new_status, order_index):
        sql = "UPDATE Orders SET order_status = '{}' WHERE order_id = '{}'".format(new_status, order_index)
        self.cursor.execute(sql)
        print("Status Update Done\n")

        
        
    ################# UPDATE ORDERS #########################

    def update_order_in_db(self,order_index, new_name, new_address, new_phone, new_courier, new_status, new_products):
        
        sql = "UPDATE Orders SET order_name = '{}', order_add = '{}', order_phone = '{}', order_courier = {}, order_status = '{}', order_items = '{}' where order_id = {}".format(new_name,new_address,new_phone,new_courier,new_status,new_products,order_index)
        self.cursor.execute(sql)

        self.connection.commit()
        # cursor.close()
        # connection.close()
    

######################## GET ID's ###########################

# def get_ids_from_db(table, list):
    
#     if table == "Courier":
#         sql = "SELECT c_id FROM Couriers"
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         list.clear()
#         for id in myresult:
#             list.append(id[0])
            
#     elif table == "Product":
#         sql = "SELECT prod_id FROM Products"
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         list.clear()
#         for id in myresult:
#             list.append(id[0])
            
#     elif table == "Order":
#         sql = "SELECT order_id FROM Orders"
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         list.clear()
#         for id in myresult:
#             list.append(id[0])
        
    # cursor.close()
    # connection.close()
    
############### GET PREVIOUS ATTRIBUTES #################

# def get_previous_attr(table, index, list):
#     cursor = connection.cursor(pymysql.cursors.DictCursor)
    
#     if table == "Courier":
#         sql = "select c_name, c_number from Couriers where c_id = {}".format(index)
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         list.clear()
#         for row in myresult:
#             list.append(row)
        
#         # cursor.close()
#         # connection.close()
        
#     elif table == "Product":
#         sql = "select prod_name, prod_price from Products where prod_id = {}".format(index)
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         list.clear()
#         for row in myresult:
#             list.append(row)
                
#         # cursor.close()
#         # connection.close()    
        
#     elif table == "Order":
#         sql = "SELECT order_name,order_add,order_phone,order_courier,order_status,order_items FROM Orders where order_id = {}".format(str(index))
#         cursor.execute(sql)
#         myresult = cursor.fetchall()
#         list.clear()
#         for row in myresult:
#             list.append(row)
        
#         # cursor.close()
#         # connection.close()

