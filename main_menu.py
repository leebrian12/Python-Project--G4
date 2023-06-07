import login_signin

def user_displayMenu():#这边是改user menu 的
    print("\n1.Pulau Langkawi		3D2N  	RM 150.00 RM 105.00")
    print("2.Pulau Redang		3D2N	RM 120.00 RM 84.00")
    print("3.Pulau Ketam		3D2N	RM 100.00 RM 70.00")
    print("4.Genting Highlands	4D3N	RM 350.00 RM 245.00")
    print("5.Cameron Highlands	4D3N	RM 300.00 RM 210.00")

def display_menu():
    print("==== Customer Menu ====")
    print("1. Add Customer")
    print("2. Remove Customer")
    print("3. View Customers")
    print("4. Exit")

customers = []

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter customer name: ")
        customers.append(name)
        print("Customer added successfully!")
    elif choice == "2":
        name = input("Enter customer name to remove: ")
        if name in customers:
            customers.remove(name)
            print("Customer removed successfully!")
        else:
            print("Customer not found!")
    elif choice == "3":
        print("Customer List:")
        for customer in customers:
            print(customer)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 4.")

def admin_displayMenu():#这边是改admin menu 的
    print("\nhahahah admin")

def main(choice): #这里是main 咯
    
    if(choice == 1):
        user_displayMenu()
    elif(choice == 2):
        admin_displayMenu()
    else:
        print("Thank You for choosing Fantastos")



choose = login_signin.login()
