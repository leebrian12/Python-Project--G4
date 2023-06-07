#Admin Menu Page

import os

# Function to display the admin main page menu

def display_admin_menu():
    print("====++ Admin Main Page ++====")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

# Function to validate the admin credentials

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Read the admin credentials from the file

    Success = read_admin()
    if username == Success["username"] and password == Success["password"]:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Function to read the admin credentials from a file

def read_admin():

    Success = {}
    file_path = "AdminAcc.txt"
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                Success[key] = value
    return Success

# Function to write the admin credentials to a file
def write_admin_acc(username, password):

    file_path = "AdminAcc.txt"
    with open(file_path, "w") as file:
        file.write(f"username={username}\n")
        file.write(f"password={password}\n")
    print("Account registered successfully.")

# Main program
while True:
    display_admin_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        if login():
            # Implement the admin actions here
            print("Implementing admin actions...")
        else:
            print("Login failed. Please try again.")
    elif choice == "2":
        username = input("Enter a new admin username: ")
        password = input("Enter a new admin password: ")
        write_admin_acc(username, password)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")