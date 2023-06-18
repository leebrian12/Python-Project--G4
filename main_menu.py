import login_signin
import admin
import CustomerMenu

def user_displayMenu(): 
    CustomerMenu.run_cus()


def admin_displayMenu():
    admin.main()

def main(choice): 
    
    if(choice == 1):
        user_displayMenu()
    elif(choice == 2):
        admin_displayMenu()
    else:
        print("\nTHANK YOU FOR CHOOSING FANTASTOS!")

choice = login_signin.main()

main(choice)
 
 
 