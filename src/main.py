from frequent import clear
from frequent import quit_app
from frequent import error_message
import menus
import frequent
import sql_cmds
import caches
import functions


def home_menu():
    # clear()
    
    print("Welcome to Limited Products, Limited Choice!\n\nHere are your (limited) options:\n")
    home_menu_choices = [
        "Show Product Menu: '1'", 
        "Show Courier Menu: '2'", 
        "Show Orders Menu: '3'\n",
        "Save Files & Exit: '0'"
    ]
    print("\n".join(home_menu_choices))
    

    home_input = input()
    exit_app = home_input == "0"
    product_menu = home_input == "1"
    courier_menu = home_input == "2"
    order_menu = home_input == "3"
    
    if exit_app:
        quit_app()
    
    elif product_menu:
        clear()
        functions.multi_menu("Product")
        home_menu()
        
    elif courier_menu:
        clear()
        functions.multi_menu("Courier")
        home_menu()
        
    elif order_menu:
        clear()
        functions.orders_menu()
        home_menu()
        
    else:
        clear()
        print(home_input, error_message)
    
def main():
    home_menu()


main()