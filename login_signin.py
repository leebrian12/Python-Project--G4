def save_users(users):
    with open('AccountList.txt', 'a') as file:
        for username, user_data in users.items():
            file.write(f"{username},{user_data['password']},{user_data['role']}\n")

def load_users():
    users = {}
    try:
        with open('AccountList.txt', 'r') as file:
            for line in file:
                username, password, role = line.strip().split(',')
                users[username] = {'password': password, 'role': role}
    except FileNotFoundError:
        pass
    return users

def customer_register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'password': password, 'role': 'User Account'}
    save_users(users)
    print("Registration successful!")

def admin_register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'password': password, 'role': 'Admin Account'}
    save_users(users)
    print("Registration successful!")

def customer_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password and users[username]['role'] == 'User Account':
        print("\n~~~ Welcome Back User ~~~")
        act = 1
        return act
    else:
        print("\nINVALID ACCOUNT or not a User account.")
        exit(0)

def admin_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password and users[username]['role'] == 'Admin Account':
        print("\n~~~ Welcome Back Admin ~~~")
        act = 2
        return act
    else:
        print("INVALID ACCOUNT or not an Admin account.")
        exit(0)

def part2():
    users = load_users()
    print("\n========= USER MENU =========\n")
    print("         1. Register")
    print("         2. Login")
    print("         3. Back to Main")

    choice = input("\nPlease enter your choice ('1' or '2' or '3'): ")


    if(choice == '1'):
        customer_register(users)
        main()
    elif(choice == '2'):
        suc = customer_login(users)
        if(suc == 1):
            type = 1
            return type 

    elif(choice == '3'):
        main()
    else:
        print("\nInvalid Choice! Please RE-RUN the program.")
        exit(0)


def part3():
    users = load_users()
    print("\n========== ADMIN MENU ==========\n")
    print("         1. Register")
    print("         2. Login")
    print("         3. Back to Main")

    choice = input("\nPlease enter your choice ('1' or '2' or '3'): ")

    if(choice == '1'):
        admin_register(users)
        main()
    elif(choice == '2'):
        suc = admin_login(users)
        if(suc == 2):
            type = 2
            return type
    elif(choice == '3'):
        main()
    else:
        print("\nInvalid Choice! Please RE-RUN the program.")
        exit(0)


def main():
    print("\n**********************************")
    print("||     Welcome to Fantastos\t||")
    print("\n**********************************")
    print("\n       TRAVEL AGENCY SYSTEM")
    print("=================================")
    print("            Main Menu\n   ")
    print("            1. User")
    print("            2. Admin")
    print("            3. Exit")

    choice = input("\nPlease enter your choice ('1' or '2' or '3'): ")
    if choice == '1':
        part2()
        type = 1
        return type
    elif choice == '2':
            part3()
            type = 2
            return type
    elif choice == '3':
            print("\nTHANK YOU FOR CHOOSING FANTASTOS!")
            exit(0)
    else:
            print("\nInvalid Choice! Please RE-RUN the program.")

def login():
 

    while True:
        print("\n===+ Welcome to Fantastos +===\n")
        print("         1. User")
        print("         2. Admin")
        print("         3. Exit")

        choice = input("\nPlease enter your choice ('1' or '2' or '3'): ")
        if choice == '1':
            part2()
            type = 1
            return type
        elif choice == '2':
            part3()
            type = 2
            return type
        elif choice == '3':
            print("\nTHANK YOU FOR CHOOSING FANTASTOS!")
            exit(0)
        else:
            print("\nInvalid Choice! Please try again.")
            

