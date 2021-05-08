import os,sys,pymysql,frequent,csv
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

############
products_names_list = []
couriers_names_list = []

orders_master_list = []

order_products_list = []
courier_ids_list = []
product_ids_list = []
order_ids_list = []

selected_product_info_dict= []
selected_courier_info_dict = []
selected_order_info_dict = []
#####################
def import_cache(table,file_name):
    pass

def export_cache(table):
    select_all = f'SELECT * FROM {table}s'
    cursor.execute(select_all)
    if table == "Product":
        with open("..\data\products.csv","w",newline='') as prod_file:
            writer = csv.writer(prod_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(col[0] for col in cursor.description)
            for row in cursor:
                writer.writerow(row)
                
    if table == "Courier":
        with open("..\data\couriers.csv","w", newline='') as c_file:
            writer = csv.writer(c_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(col[0] for col in cursor.description)
            for row in cursor:
                writer.writerow(row)
            
    if table == "Order":
        with open("..\data\orders.csv", "w", newline="") as orders_file:
            writer = csv.writer(orders_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(col[0] for col in cursor.description)
            for row in cursor:
                writer.writerow(row)
        