import os, sys


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

order_status_options = [
    "Preparing",
    "Ready For Collection",
    "Out for Delivery",
    "Delivered",   
    ]

def quit_app():
    print("\n")
    clear()
    print("\nPlease come again!")
    sys.exit()
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def start_again():
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
            

error_message = "is not an available option"

def display_add_order_product_list(inputted_list):
    print("\nCurrent products in Order:\n")
    print("\n")
    print(inputted_list)
    
def display_available_items(menu_list_items):
    if menu_list_items == order_status_options:
        print("Order Status Options:\n")
        for (
            index,
            item,
        ) in enumerate(menu_list_items):
            print(f"Option {index+1} - {item}")

