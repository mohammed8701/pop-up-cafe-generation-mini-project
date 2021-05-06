import os,sys,pymysql,frequent
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
        host,
        user,
        password,
        database
)
cursor = connection.cursor()

############# DISPLAY ITEMS ############

def display_items(table):
    cursor.execute('SELECT * FROM {}s'.format(str(table)))
    rows = cursor.fetchall()
    for row in rows:
        if table == "Product":
            print(f'{str(row[0])}: {row[1]} - £{row[2]}')
    
        elif table == "Courier":
            print(f'{str(row[0])}: {row[1]} - {row[2]}')
        
        elif table == "Order":
            print(f'{str(row[0])}- Customer Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {str(row[4])}, Status: {row[5]}, Items: {row[6]}')
    cursor.close()
    connection.close()
    
    
    
######### DISPLAY ITEMS AT INDEX #############

def display_item_at_index(menu_name, index):
    
    if menu_name == "Order":
        cursor.execute('SELECT * FROM {}s WHERE order_id = {}'.format(str(menu_name, index)))    
        rows = cursor.fetchall()
        for row in rows:
            print(f'{str(row[0])}- Customer Name: {row[1]}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {str(row[4])}, Status: {row[5]}, Items: {row[6]}')

    elif menu_name == "Product":
        cursor.execute('SELECT * FROM {}s WHERE prod_id = {}'.format(str(menu_name,index)))
        rows = cursor.fetchall()
        for row in rows:
            print(f'{str(row[0])}: {row[1]} - £{row[2]}')
    
    elif menu_name == "Courier":
        cursor.execute('SELECT * FROM {}s WHERE c_id = {}'.format(str(menu_name, index)))
        rows = cursor.fetchall()
        for row in rows:
            print(f'{str(row[0])}: {row[1]} - {row[2]}')
    cursor.close()
    connection.close()

########## ADD ITEM TO DB ############

def add_item_to_db(menu_name,name,attribute):
    if menu_name == "Product":
        sql = "INSERT INTO Products (prod_name, prod_price) VALUES (%s, %s)"
        val = (name, attribute)
        
    elif menu_name == "Courier":
        sql = "INSERT INTO Couriers (c_name, c_number) VALUES (%s, %s)"
        val = (name, attribute)
        
    cursor.execute(sql, val)

    connection.commit()
    cursor.close()
    connection.close()
    
#################### UPDATE ITEMS ###########################
def update_item(menu_name, index, name, attribute):
    frequent.clear()
    if menu_name == "Product":
        sql = "UPDATE Products SET prod_name = '{}', prod_price = '{}' WHERE prod_id = {}".format(name, attribute, index)
    
    elif menu_name == "Courier":
        sql = "UPDATE Couriers SET c_name = '{}', c_number = '{}' WHERE c_id = {}".format(name, attribute, index)
    
    cursor.execute(sql)
        
    connection.commit()
    cursor.close()
    connection.close()

############### DELETE ITEMS ###################
def delete_item(menu_name,item_index):
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    cursor = connection.cursor()
    if menu_name == "Product":
        sql = f"DELETE FROM Products WHERE prod_id = {item_index}"

    elif menu_name == "Courier":
        sql = f"DELETE FROM Couriers WHERE c_id = {item_index}"
        
    elif menu_name == "Order":
        sql = f"DELETE FROM Orders WHERE order_id = {item_index}"
        

    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()
    
    
    
    
################# UPDATE ORDERS #########################

def update_order_in_db(order_index, new_name, new_address, new_phone, new_courier, new_status, new_products):
    
    sql = "UPDATE Orders SET order_name = '{}', order_add = '{}', order_phone = '{}', order_courier = {}, order_status = '{}', order_items = '{}' where order_id = {}".format(new_name,new_address,new_phone,new_courier,new_status,new_products,order_index)
    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()
    

######################## GET ID's ###########################

def get_ids_from_db(table, list):
    
    if table == "Courier":
        sql = "SELECT c_id FROM Couriers"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        list.clear()
        for id in myresult:
            list.append(id[0])
            
    elif table == "Product":
        sql = "SELECT prod_id FROM Products"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        list.clear()
        for id in myresult:
            list.append(id[0])
            
    elif table == "Order":
        sql = "SELECT order_id FROM Orders"
        cursor.execute(sql)
        myresult = cursor.fetchall()
        list.clear()
        for id in myresult:
            list.append(id[0])
        
    cursor.close()
    connection.close()
    
############### GET PREVIOUS ATTRIBUTES #################

def get_previous_attr(table, index, list):
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    if table == "Courier":
        sql = "select c_name, c_number from Couriers where c_id = {}".format(index)
        cursor.execute(sql)
        myresult = cursor.fetchall()
        list.clear()
        for row in myresult:
            list.append(row)
        
        cursor.close()
        connection.close()
        
    elif table == "Product":
        sql = "select prod_name, prod_price from Products where prod_id = {}".format(index)
        cursor.execute(sql)
        myresult = cursor.fetchall()
        list.clear()
        for row in myresult:
            list.append(row)
                
        cursor.close()
        connection.close()    
        
    elif table == "Order":
        sql = "SELECT order_name,order_add,order_phone,order_courier,order_status,order_items FROM Orders where order_id = {}".format(index)
        cursor.execute(sql)
        myresult = cursor.fetchall()
        list.clear()
        for row in myresult:
            list.append(row)
        
        cursor.close()
        connection.close()
