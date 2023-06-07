def save_users(users):
    with open('Acc.txt', 'w') as file:
        for username, user_data in users.items():
            file.write(f"{username},{user_data['password']},{user_data['role']}\n")

def load_users():
    users = {}
    try:
        with open('Account.txt', 'r') as file:
            for line in file:
                username, password, role = line.strip().split(',')
                users[username] = {'password': password, 'role': role}
    except FileNotFoundError:
        pass
    return users

def customer_register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'password': password, 'role': 'Customer'}
    save_users(users)
    print("\nCustomer Registration Successful!")

def admin_register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'password': password, 'role': 'Admin'}
    save_users(users)
    print("\nAdmin Registration Successful!")

def customer_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password and users[username]['role'] == 'user':
        print("Welcome User,Login successful!")
        act = 1
        return act
    else:
        print("Invalid Account or is not a User account.")

def admin_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password and users[username]['role'] == 'Admin':
        print("Welcome Admin Login successful!")
        act = 2
        return act
    else:
        print("Invalid Account or is not Admin account.")

def login():
    users = load_users()

    while True:
        print("\n==== +Fantastos Travel Agency System +====\n")
        print("1. Customer Registration")
        print("2. Admin Registration")
        print("3. Customer Login")
        print("4. Admin Login")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            customer_register(users)
        elif choice == '2':
            admin_register(users)
        elif choice == '3':
            suc = customer_login(users)
            if(suc == 1):
                type = 1
                return type 
                break
            else:
                continue
        elif choice == '4':
            suc = admin_login(users)
            if(suc == 2):
                type = 2
                return type 
                break
            else:
                continue
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


