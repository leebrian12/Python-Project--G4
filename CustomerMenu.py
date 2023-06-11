import os
import ast

PACKAGE_FILE = 'travel_packages.txt'

def load_packages():
    try:
        with open(PACKAGE_FILE, 'r') as file:
            content = file.read()
            if content:
                return ast.literal_eval(content)
    except FileNotFoundError:
        return []

def display_packages(packages):
    print("\n===== List of Travel Packages =====\n")
    if packages:
        for i, package in enumerate(packages, start=1):
            print(f"{i}. Name: {package['name']}, Destination: {package['destination']}, Price per Person(RM): {package['price']}")
        while True:
            choice = input("\nEnter the number of the package to add to cart ('1' or '0' to exit): ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    break
                elif choice <= len(packages):
                    package = packages[choice - 1]
                    package_name = package['name']
                    add_to_cart(package_name)
                    break
                else:
                    print("Invalid choice! Please try again.")
   
def view_cart():
    print("\nYour Cart:")
    with open("cart.txt", "r") as file:
        items = file.readlines()
        for item in items:
            print(item.strip())

def add_to_cart(package_name):
    with open("cart.txt", "a") as file:
        file.write(package_name + "\n")
    print("\n"+package_name + " added to cart.")

def remove_from_cart(index):
    with open("cart.txt", "r") as file:
        items = file.readlines()
    
    if 1 <= index <= len(items):
        removed_package = items[index - 1].strip()
        items.pop(index - 1)
        with open("cart.txt", "w") as file:
            file.write("\n".join(items))
        print(f"\nPackage '{removed_package}' removed from cart.")
    else:
        print("Invalid index. Please try again.")

def process_payment():
    with open("cart.txt", "r") as file:
        items = file.readlines()

    selected_packages = []
    total_price = 0

    with open("travel_packages.txt", "r") as file:
        packages = ast.literal_eval(file.read())

        for package in packages:
            package_name = package['name']
            package_price = float(package['price'])

            if package_name + "\n" in items:
                selected_packages.append(package)
                total_price += package_price

    num_persons = int(input("Enter the number of persons: "))
    total_price *= num_persons

    print("\n========== PAYMENT RECEIPT ==========")
    print(f"\nNumber of Persons: {num_persons}\n")

    print("Selected Packages:")
    for package in selected_packages:
        print(f"- {package['name']}: RM {package['price']} per person")

    print("\nTotal Price: RM", total_price)
    print("=====================================")

    print("\nPayment Successful. Thank you for your purchase!")


def run_cus():
    current_directory = os.getcwd()
    abs_package_file_path = os.path.join(current_directory, PACKAGE_FILE)
    print("Travel package file path:", abs_package_file_path)

    packages = load_packages()

    if not os.path.exists("cart.txt"):
        with open("cart.txt", "w") as file:
            file.write("")

    while True:
        print("\n====== FANTASTOS TRAVEL AGENCY SYSTEM ======")
        print("\n         1. View Packages")
        print("         2. View Cart")
        print("         3. Remove from Cart")
        print("         4. Make Payment")
        print("         5. Exit")

        choice = input("\nPlease enter your choice ('1' or '2' or '3' or '4' or '5'): ")

        if choice == "1":
            display_packages(packages)
        elif choice == "2":
            view_cart()
        elif choice == "3":
            index = int(input("\nEnter the index of the package to remove from cart: "))
            remove_from_cart(index)
        elif choice == "4": 
            process_payment()
            exit(0)
        elif choice == "5":
            break
        else:
            print("\nInvalid Choice! Please try again.")

    print("\nTHANK YOU FOR CHOOSING FANTASTOS! HAVE A NICE DAY! ^_^")

