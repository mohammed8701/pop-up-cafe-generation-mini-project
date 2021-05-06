from frequent import clear
from frequent import quit_app
from frequent import error_message
import menus

def home_menu():
    is_open = True
    while is_open:

        home_menu_prompt()
        home_menu_choices()
    
        home_input = input()
        exit_app = home_input == "0"
        product_menu = home_input == "1"
        courier_menu = home_input == "2"
        order_menu = home_input == "3"
        
        if exit_app:
            return quit_app()
        
        elif product_menu:
            # clear()
            return menus.multi_menu("Product")
            
        elif courier_menu:
            # clear()
            return menus.multi_menu("Courier")
            
        elif order_menu:
            # clear()
            return menus.orders_menu()
        else:
            # clear()
            print(home_input, error_message)

def home_menu_prompt():
    print("Welcome to Limited Products, Limited Choice!\n\nHere are your (limited) options:\n")

def home_menu_choices():
    home_menu_choices = [
        "Show Product Menu: '1'", 
        "Show Courier Menu: '2'", 
        "Show Orders Menu: '3'\n",
        "Save Files & Exit: '0'"
    ]
    print("\n".join(home_menu_choices))    
    
def main():
    home_menu()

main()