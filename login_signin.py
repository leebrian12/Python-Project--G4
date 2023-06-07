

def save_users(users):
    with open('users_acount.txt', 'w') as file:
        for username, user_data in users.items():
            file.write(f"{username},{user_data['password']},{user_data['role']}\n")

def load_users():
    users = {}
    try:
        with open('users_acount.txt', 'r') as file:
            for line in file:
                username, password, role = line.strip().split(',')
                users[username] = {'password': password, 'role': role}
    except FileNotFoundError:
        pass
    return users

def customer_register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'password': password, 'role': 'customer'}
    save_users(users)
    print("Registration successful!")

def admin_register(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = {'password': password, 'role': 'admin'}
    save_users(users)
    print("Registration successful!")

def customer_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password and users[username]['role'] == 'customer':
        print("Welcome Customer login successful!")
        act = 1
        return act
    else:
        print("Invalid credentials or user is not a customer.")

def admin_login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]['password'] == password and users[username]['role'] == 'admin':
        print("Welcome Admin login successful!")
        act = 2
        return act
    else:
        print("Invalid credentials or user is not an admin.")

def login():
    users = load_users()


    while True:
        print("1. Customer Registration")
        print("2. Admin Registration")
        print("3. Customer Login")
        print("4. Admin Login")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

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


