

from frequent import clear

#####

import frequent
import main
import sql_cmds
import caches

#######################################
########## MULTI MENUS ################
#######################################

def multi_menu(menu_name):
    while True:
        
        print(f"\nYou are in the {menu_name}s menu.\n\nOptions:\n".format(menu_name.title()))
        print(f"Return to Home Menu: '0'\nShow {menu_name}s list: '1'\nCreate New {menu_name}: '2'\nUpdate {menu_name}: '3'\nDelete {menu_name}: '4'")
        user_choice = input()
        
        leave_multi_menu = user_choice == "0"
        show_items_list = user_choice == "1"
        add_new_item = user_choice == "2"
        update_item = user_choice == "3"
        delete_item = user_choice == "4"

        if leave_multi_menu:
            frequent.clear()
            print("Returning to Home Menu")
            # main.home_menu()
            False
            break
            
        
        elif show_items_list:
            frequent.clear()
            print(f"{menu_name}s List:\n\n")
            sql_cmds.display_items(menu_name)
            start_again()
            False
            
        elif add_new_item:
            frequent.clear()
            add_item_navigator(menu_name)
            False
            break
        
        elif update_item:
            frequent.clear()
            update_item_navigator(menu_name)
            False
        elif delete_item:
            frequent.clear()
            delete_item_navigator(menu_name)
            False
        else:
            frequent.clear()
            print(user_choice, frequent.error_message)
            multi_menu(menu_name)
            
def start_again():
    error_message = "is not an available option"
    while True:
        print("\nMain menu: '1'\nQuit: '0'\n")
        user_choice = input()
        
        if user_choice == "1":
            clear()
            main.home_menu()
            False
            
        elif user_choice == "0":
            quit_app()
            False
            
        else:
            clear()
            print(user_choice, error_message)
            print("\nPlease enter either '0' or '1'")
            
########### ADD ITEMS ############
            
def add_item_navigator(menu_name):
    if menu_name == "Product":
        name = item_name(menu_name)
        if name == "0":
            clear()
            multi_menu(menu_name)
        else:
            attribute = add_item_second_attr(menu_name,"price")
            sql_cmds.add_item_to_db(menu_name, name, attribute)
            caches.export_cache("Product")
            print(f"\n\n{menu_name} updated!\n\n")
            print(f"Here are the new {menu_name}s:\n")
            sql_cmds.display_items(menu_name)
            start_again()
        
    elif menu_name == "Courier":
        name = item_name(menu_name)
        if name == "0":
            multi_menu(menu_name)
        else:
            attribute = add_item_second_attr(menu_name,"phone number")
            sql_cmds.add_item_to_db(menu_name, name, attribute)
            caches.export_cache("Courier")
            print(f"\n{menu_name} updated!\n\n")
            print(f"Here are the new {menu_name}s:\n")
            sql_cmds.display_items(menu_name)
            start_again()

def add_item_second_attr(menu_name,option_type):
    while True:
        try:
            print(f"\nWhat's the {option_type} of the {menu_name} you would like to add:\n")
            item_second_attr = input()
            if option_type == "price":
                new_product_price = round(float(item_second_attr), 2)
                return new_product_price
                False
                
            elif option_type == "phone number":
                new_courier_number = int(item_second_attr)
                return new_courier_number
                False
                break
            
        
        except ValueError:
            frequent.clear()
            print("Error:\nPlease enter a valid number!\n")    

def add_item_name_prompt(menu_name):
    if menu_name == "Orders":
        add_item_prompt = f"You are in the Add {menu_name} menu\n\nWhat's the name of the customer making the order:\nPress '0' To return to Orders Menu\n\n"
    else:
        add_item_prompt = f"You are in the Add {menu_name} menu\nWhat's the name of the {menu_name} you would like to add:\nPress '0' To return to Orders Menu\n\n"
    print(add_item_prompt)
    
def item_name(menu_name):
    add_item_name_prompt(menu_name)
    # print(f"\n\nEnter '0' to return to {menu_name} menu\n")    
    item_name_input = input()
    # if item_name_input == "0":
    #     clear()
    #     multi_menu(menu_name)
        
    # else:
    new_name = item_name_input.title() 
    return new_name


############## UPDATE ITEMS ################
def update_item_navigator(menu_name):
    
    if menu_name == "Product":
        index = update_item_index_selector(menu_name,caches.product_ids_list)
        if index == "0":
            multi_menu(menu_name)
        else:
            name = update_item_name(menu_name, index)
            attribute = update_item_attribute(menu_name, index)

            try:
                frequent.clear()
                sql_cmds.update_item(menu_name, index, name, attribute)
                caches.export_cache("Product")
                print(f"{menu_name} updated!\n\n")
                print(f"Here are the new {menu_name}s:\n")
                sql_cmds.display_items(menu_name)
                start_again()
                
            except Exception as e:
                print(e)
            
    elif menu_name == "Courier":
        
        index = update_item_index_selector(menu_name,caches.courier_ids_list) 
        name = update_item_name(menu_name, index)
        attribute = update_item_attribute(menu_name, index)
    
        try:
            sql_cmds.update_item(menu_name, index, name, attribute)
            caches.export_cache("Courier")
            print(f"\n\n{menu_name} updated!\n\n")
            print(f"Here are the new {menu_name}s:\n")
            sql_cmds.display_items(menu_name)
            start_again() 
            
        except Exception as e:
            
            print(e)

def update_item_index_selector(menu_name, id_list):
    sql_cmds.get_ids_from_db(menu_name,id_list)
    while True:
        print(f"You are in the Update {menu_name} Menu\n")  
        sql_cmds.display_items(menu_name)
        print(f"\nWhat's the ID of the {menu_name} you would like to update?:\n\nEnter '0' to return to products menu\n(Please ensure it's in the list above)\n")
        item_to_select_index = input()
        
        if item_to_select_index == "0":
            return item_to_select_index
            False
            break
        
        elif item_to_select_index != "0" and int(item_to_select_index) in id_list:
            return int(item_to_select_index)
            False
            break
        
        else:
            frequent.clear()
        print(f"Error:\nPlease enter a number that corresponds with a {menu_name} ID\n")  

def update_item_name(menu_name, index):
    while True:
        if menu_name == "Product":
            sql_cmds.get_previous_attr(menu_name, index, caches.selected_product_info_dict)
            print(f"What's the new name of the {menu_name} you would like to update:\n")
            item_name_input = input()
            
            if item_name_input == "":
                updated_item_name = caches.selected_product_info_dict[0]['prod_name']
                return  updated_item_name
                False
        
            elif item_name_input != "":
                update_item_name = item_name_input.title() 
                return update_item_name
                False
            else:
                print("Update_item_name input error")
            
        if menu_name == "Courier":
            sql_cmds.get_previous_attr(menu_name, index, caches.selected_courier_info_dict)
            print(f"What's the new name of the {menu_name} you would like to update:\n")
            item_name_input = input()
            
            if item_name_input == "":
                updated_item_name = caches.selected_courier_info_dict[0]['c_name']
                return updated_item_name
                False
            elif item_name_input != "":
                update_item_name = item_name_input.title() 
                return update_item_name
                False
            else:
                print("Update_item_name input error")
        else:
            print("Error: incorrect menu name in update_item_name")
            break

def update_item_attribute(menu_name,index):
    while True:
        if menu_name == "Product":
            sql_cmds.get_previous_attr(menu_name, index, caches.selected_product_info_dict)
            print(f"\nWhat's the new price of the {menu_name} you would like to update:\n")
            item_second_attr = input()
            if item_second_attr == "":
                updated_item_attribute = caches.selected_product_info_dict[0]['prod_price']
                return  updated_item_attribute
                False
            elif item_second_attr != "":
                new_product_price = round(float(item_second_attr), 2)
                return new_product_price
                False
            else:
                frequent.clear()
                print("Error:\nPlease enter a valid number!\n")       
                
        elif menu_name == "Courier":
            sql_cmds.get_previous_attr(menu_name, index, caches.selected_courier_info_dict)
            print(f"\nWhat's the new phone number of the {menu_name} you would like to update:\n")
            item_second_attr = input()
            if item_second_attr == "":
                updated_item_attribute = caches.selected_courier_info_dict[0]['c_number']
                return  updated_item_attribute
                False
            elif item_second_attr != "":
                updated_item_attribute = item_second_attr.title()
                return updated_item_attribute
                False
            else:
                frequent.clear()
                print("Error:\nPlease enter a valid number!\n")       

############ DELETE ITEMS #############

def delete_item_navigator(menu_name):
    if menu_name == "Product":
        item_index = delete_item_index_selector(menu_name, id_list = caches.product_ids_list)
        if item_index == "0":
            multi_menu(menu_name)
        else:
            try:
                sql_cmds.delete_item(menu_name, item_index)
                caches.export_cache("Product")
                print(f"\n\n{menu_name} deleted!\n\n")
                print(f"Here are the remaining {menu_name}s:\n")
                sql_cmds.display_items(menu_name)
                start_again()

            except Exception as e:
                clear()
                print(e)
            
    elif menu_name == "Courier":
        try:
            sql_cmds.delete_item(menu_name, item_index = delete_item_index_selector(menu_name, id_list = caches.courier_ids_list))
            caches.export_cache("Courier")
            print(f"{menu_name} deleted!\n\n")
            print(f"Here are the remaining {menu_name}s:\n")
            sql_cmds.display_items(menu_name)
            start_again()
            
        except Exception as e:
            clear()
            print(e)

def delete_item_index_selector(menu_name, id_list):
    sql_cmds.get_ids_from_db(menu_name,id_list)
    print(f"You are in the delete {menu_name} menu\n")
    while True:
        print(f"Which {menu_name} do you want to delete from the list?:\nPress '0' to cancel\n(Please ensure it is in the list above)\n\n")
        sql_cmds.display_items(menu_name)  
        item_to_delete_index = input()
        if item_to_delete_index == "0":
            clear()
            return item_to_delete_index
            False
            break
        elif item_to_delete_index != "0" and int(item_to_delete_index) in id_list:
            clear()
            return int(item_to_delete_index)
            False
            break
        
        else:
            frequent.clear()
            print(f"Error:\nPlease enter a number that corresponds with a {menu_name} ID\n") 


#############################################
############ ORDERS MENU ####################
#############################################

def orders_menu():
    while True:
        orders_menu_prompt = ["\nYou are in the Orders menu.\n\nOptions:\n"]   
        orders_menu_choices = [
            "Return To Main Menu: '0'",
            "Show Orders List: '1'",
            "Create New Order: '2'",
            "Update Order Status : '3'",
            "Update Order: '4'",
            "Delete Order: '5'",
        ]
        print("\n".join((orders_menu_prompt + orders_menu_choices)))
        
        user_choice = input()
        
        leave_orders_menu = user_choice == "0"
        show_orders_list = user_choice == "1"
        add_new_orders = user_choice == "2"
        update_orders_status = user_choice == "3"
        update_orders = user_choice == "4"
        delete_orders = user_choice == "5"
        
        if leave_orders_menu:
            frequent.clear()
            print("Returning to main menu")
            False
            break
            # return main.home_menu()
        
        elif show_orders_list:
            clear()
            print("Current Orders:\n\n")
            sql_cmds.display_items("Order")
            start_again()
            False
            
        elif add_new_orders:
            clear()
            add_new_orders_navigator()
            False
        
        elif update_orders_status:
            frequent.clear()
            select_order("update status", update_orders_status_prompt())
            False
        
        elif update_orders:
            frequent.clear()
            select_order("update order", update_orders_prompts())
            # update_orders_navigator()
            False
        
        elif delete_orders:
            frequent.clear()
            select_order("delete order", delete_orders_prompts())
            # delete_orders_navigator()
            False

        else:
            frequent.clear()
            print(user_choice, frequent.error_message)
            
def select_order(menu_name, order_prompt):
    condition = True
    while True:
        order_prompt
        selected_order_index = int(input())
        if selected_order_index == 0:
            clear()
            orders_menu()
            False
            
        
        elif menu_name == "update status":
            return update_orders_status_menu("Order", selected_order_index)
            False
            
        
        elif menu_name == "update order":
            return update_orders_navigator("Order", selected_order_index)
            False
            
        
        elif menu_name == "delete order":
            return delete_orders_navigator(selected_order_index)
            False
            
        
        else:
            clear()
            print("Please enter a number listed above:\n")

            
################ ADD ORDERS #############################            
            
def add_new_orders_navigator():
    
    name = order_name()
    if name == "0":
        clear()
        orders_menu()
    else:
        address = order_address()
        if address == "0":
            clear()
            orders_menu()
        else:
            phone = order_phone()
            courier = order_courier()
            status = "Preparing"
            items = orders_products_compiler()
            
            try:
                frequent.clear()
                sql_cmds.add_order_to_db(name,address,phone,courier,status,items)
                caches.export_cache("Order")
                print("Order Added:\n")
                sql_cmds.display_items("Order")
                start_again()

            except Exception as e:
                print(e)  
            
def order_name():
    add_item_name_prompt("Orders")
    order_name_input = (input()).title()
    if order_name_input == "0":
        clear()
        return order_name_input
    else:
        return order_name_input
        # clear()

def order_address():
    order_address = (input("\nWhat's the address of the customer making the order:\nPress '0' To return to Orders Menu\n").title())
    if order_address == "0":
        clear()
        return order_address
    else:
        return order_address
    
def order_phone():
    order_phone = (input("\nWhat's the phone number for the customer making the order:\n")).title()
    return order_phone
    
def order_courier():
    sql_cmds.get_ids_from_db("Courier", caches.courier_ids_list)
    
    while True:
            frequent.clear()
            print("\nCouriers List:\n")
            sql_cmds.display_items("Courier")
            order_couriers_index = input("\n\nWhich courier you wish to use (Please ensure it's in the list above):\n")
            
            if order_couriers_index != "0" and int(order_couriers_index) in caches.courier_ids_list:
                return int(order_couriers_index)
                False
                break
            
            else:
                frequent.clear()
            print("Error: Choice not found\nPlease choose an existing Courier from this list:\n")
            
temp_new_order_products_list = []

def orders_products_compiler():
    temp_new_order_products_list.clear()
    sql_cmds.get_ids_from_db("Product", caches.product_ids_list)

    condition = False
    while True:
        print("\nProducts List:\n")
        sql_cmds.display_items("Product")
        frequent.display_add_order_product_list(temp_new_order_products_list)
        orders_add_product_index = input("\n\nWhich products, do you wish to add (Please ensure it's in the list above):\n")
        
        if int(orders_add_product_index) in caches.product_ids_list:
            temp_new_order_products_list.append(int(orders_add_product_index))
            frequent.clear()
            
        elif int(orders_add_product_index) not in caches.product_ids_list:
            frequent.clear()
            print("Error:\nInput not in products list input\n")
            
        try:   
            display_add_order_product_list(temp_new_order_products_list)
            print("\nEnter '1' to add more items to the order:\nEnter '0' to finalise order\n")
            end_of_item_selection = input().title()                   
            if end_of_item_selection == "0":
                selected_items = temp_new_order_products_list
                return selected_items
                False
            elif end_of_item_selection == "1":
                frequent.clear()
                continue
        except:
            frequent.clear()
            print("FINALISE Exception:\nInput Error\nPlease choose an option from this list:\n") 
            
def display_add_order_product_list(inputted_list):
    print("\nCurrent products in Order:\n")
    print("\n")
    print(inputted_list)

################## UPDATE ORDER STATUS SEPERATE ################

def update_order_status_seperate(new_status, order_index):
    clear()

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
    sql = "UPDATE Orders SET order_status = '{}' WHERE order_id = '{}'".format(new_status, order_index)
    
    cursor.execute(sql)

    connection.commit()
    cursor.close()
    connection.close()

    print("Status Update Done\n")
    
def update_orders_status_prompt():
    update_orders_selection_prompt = [
        "You are in the update orders menu\n",
        "Which order would you like to update the status for?",
        "Enter '0' to return to orders menu\n",
    ]
    
    print("\n".join(update_orders_selection_prompt))
    sql_cmds.display_items("Order")
    
def update_orders_status_choices():
    update_orders_status_choices = [
        "\nStatus Choices",
        "Which status would like for this order?:",
    ]
    print("\n".join(update_orders_status_choices))
    # display_available_items(order_status_options)

def update_orders_status_menu(menu_name, order_index):
    
    update_orders_status_choices()
    frequent.display_available_items(frequent.order_status_options)
    status_choice = input()
    
    chosen_status = frequent.order_status_options[int(status_choice)-1]
    try:
        frequent.clear()
        update_order_status_seperate(chosen_status, order_index)
        print("Order Status Updated!\n\n")
        display_item_at_index(menu_name, order_index)
        start_again()
        return 1
    except Exception as e:
        print(e)     

def update_orders_status_navigator():
    while update_orders_status_menu() != 1:
        pass



################# UPDATE ORDERS ######################

def update_orders_prompts():
    
    update_orders_prompts = [
        "\nWhich order would you like to Update?:",
        "Enter '0' to return to orders menu",
        "(Please ensure it is in the options above)\n",
    ]
    print("You are in the Update Orders menu\n")
    sql_cmds.display_items("Order")
    print("\n".join(update_orders_prompts))
    

def update_orders_navigator(menu_name, order_index):
    frequent.clear()
    sql_cmds.get_previous_attr("Order",order_index, caches.selected_order_info_dict)

    name = update_order_name()
    address = update_orders_address()
    phone = update_orders_number()
    courier = update_orders_courier()
    status = update_orders_status()
    items = updated_items_to_order()
    
    try:
        frequent.clear()
        sql_cmds.update_order_in_db(order_index, name, address, phone, courier, status, items)
        print("Order Updated:\n\n")
        sql_cmds.display_item_at_index(menu_name, order_index)
        start_again()
        return 1
    except Exception as e:
        print(e)

def update_order_name():
    while True:
        
        updated_name_for_order = input("\nWhat's the new Customer Name:\n(Leave blank to skip)\n")
        if updated_name_for_order == "":
            selected_name = caches.selected_order_info_dict[0]['order_name']
            return selected_name
            False
            
        elif updated_name_for_order != "":
            selected_name = updated_name_for_order.title()
            return selected_name
            False
            
        else:
            print("\nError!:\nPlease input one of the specified conditions outlined above\n")   

def update_orders_address():
    
    while True:
        
        updated_address_for_order = (input("\nWhat's the new Customer Address\n(Leave blank to skip)\n")).title()
        if updated_address_for_order == "":
            selected_address = caches.selected_order_info_dict[0]['order_add']
            return selected_address
            False
            
        
        elif updated_address_for_order != "":
            selected_address = updated_address_for_order
            return selected_address
            False
            
        else:
            print("\nError!:\nPlease input one of the specified conditions outlined above\n")  
    
def update_orders_number():
    
    while True:
        updated_number_for_order = (input("\nWhat's the new Phone Number\n(Leave blank to skip)\n")).title()
        if updated_number_for_order == "":
            selected_number = caches.selected_order_info_dict[0]['order_phone']
            return selected_number
            False
            
        elif updated_number_for_order != "":
            selected_number = updated_number_for_order
            return selected_number
            False
            
        else:
            print("\nError!:\nPlease input one of the specified conditions outlined above\n") 

def update_orders_courier():
    sql_cmds.get_ids_from_db("Courier", caches.courier_ids_list)
    
    while False:
        clear()
        print("\nCouriers List:\n")
        display_items("Courier")
        order_couriers_index = input("\n\nWhich courier you wish to use (Please ensure it's in the list above):\nLeave blank to skip\n")
        
        if order_couriers_index == "":
            selected_courier = caches.selected_order_info_dict[0]['order_courier']
            return selected_courier
            True
            

        if order_couriers_index != "" and int(order_couriers_index) in caches.courier_ids_list:
            selected_courier = int(order_couriers_index)
            return selected_courier
            True
            
        
        else:
            clear()
            print("Error: Choice not found\nPlease choose an existing Courier from this list:\n")    


def update_orders_status_choices():
    update_orders_status_choices = [
        "\nStatus Choices",
        "Which status would like for this order?:",
    ]
    print("\n".join(update_orders_status_choices))
    # display_available_items(order_status_options)

def update_orders_status():
    frequent.clear()
    while True:
            update_orders_status_choices()
            print("Please leave blank to skip\n")
            frequent.display_available_items(frequent.order_status_options)
            updated_status_for_order = input()
            
            if updated_status_for_order == "":
                selected_status = caches.selected_order_info_dict[0]['order_status']
                return selected_status
                False
                
            
            elif updated_status_for_order != "":
                selected_status = frequent.order_status_options[int(updated_status_for_order)-1]
                return selected_status
                False
                
            
            else:
                print("\nError!:\nPlease input one of the specified conditions outlined above\n")   

def display_order_product_list():
    print("\nCurrent products in Order:\n")
    print("\n")
    print(temp_updated_order_products_list)

temp_updated_order_products_list = []            
            

def display_order_product_list():
    print("\nCurrent products in Order:\n")
    print("\n")
    print(temp_updated_order_products_list)
    
    
def updated_items_to_order():
    temp_updated_order_products_list.clear()
    sql_cmds.get_ids_from_db("Product", caches.product_ids_list)
    while False:
        
        print("\nProducts List:\n")
        sql_cmds.display_items("Product")
        display_order_product_list()
        print(temp_updated_order_products_list)
        orders_add_product_index = input("\n\nWhich products, do you wish to add (Please ensure it's in the list above):\nLeave blank to keep existing products\n")
        
        if orders_add_product_index == "":
            selected_items = caches.selected_order_info_dict[0]['order_items']
            return selected_items
        
        if orders_add_product_index != "" and int(orders_add_product_index) in caches.product_ids_list:
            temp_updated_order_products_list.append(int(orders_add_product_index))
            clear()
            
        elif orders_add_product_index != "" and int(orders_add_product_index) not in caches.product_ids_list:
            clear()
            print("Error:\nYou didn't a valid input\n")
            
        try:   
            display_order_product_list()
            print(temp_updated_order_products_list)
            print("\nEnter '1' to add more items to the order:\nEnter '0' to finalise order\n")
            end_of_item_selection = input().title()                   
            if end_of_item_selection == "0":
                selected_items = temp_updated_order_products_list
                #FIGURE OUT HOW TO MAKE THIS A STRING
                return selected_items
                True
                
            elif end_of_item_selection == "1":
                clear()
                continue
        except:
            clear()
            print("FINALISE Exception: Input Error\nPlease choose an option from this list:\n") 
            
            
############## DELETE ORDERS ######################

def delete_orders_prompts():
    
    delete_orders_prompts = [
        "\nWhich order would you like to delete?:",
        "Enter '0' to return to orders menu",
        "(Please ensure it is in the options above)\n",
    ]
    print("You are in the Delete Orders menu\n")
    sql_cmds.display_items("Order")
    print("\n".join(delete_orders_prompts))

def delete_orders_navigator(selected_order_index):
    try:
        frequent.clear()
        sql_cmds.delete_item("Order", selected_order_index)
        print("Here are the remaining orders:\n")
        sql_cmds.display_items("Order")
        print("\n")
        start_again()
        
    except Exception as e:
        frequent.clear()
        print(e)    