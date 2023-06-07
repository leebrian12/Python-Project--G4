import Register_SignIn

def user_displayMenu():#这边是改user menu 的
    print("\n1.Pulau Langkawi		3D2N  	RM 150.00 RM 105.00")
    print("2.Pulau Redang		3D2N	RM 120.00 RM 84.00")
    print("3.Pulau Ketam		3D2N	RM 100.00 RM 70.00")
    print("4.Genting Highlands	4D3N	RM 350.00 RM 245.00")
    print("5.Cameron Highlands	4D3N	RM 300.00 RM 210.00")

def admin_displayMenu():#这边是改admin menu 的
    print("\nhahahah admin")

def main(choice): #这里是main 咯
    
    if(choice == 1):
        user_displayMenu()
    elif(choice == 2):
        admin_displayMenu()
    else:
        print("Thank You for choosing Fantastos")



choose = Register_SignIn.login()
