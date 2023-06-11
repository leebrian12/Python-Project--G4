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
    print("Travel Packages:")
    if packages:
        for i, package in enumerate(packages, start=1):
            print(f"{i}. Name: {package['name']}, Destination: {package['destination']}, Price: {package['price']}")
    else:
        print("No travel packages found.")


def view_cart():
    print("\nYour Cart:")
    with open("cart.txt", "r") as file:
        items = file.readlines()
        for item in items:
            print(item.strip())

def add_to_cart(package_name):
    with open("cart.txt", "a") as file:
        file.write(package_name + "\n")
    print(package_name + " added to cart.")

def remove_from_cart(package_name):
    with open("cart.txt", "r") as file:
        items = file.readlines()
    items = [item.strip() for item in items if item.strip() != package_name]
    with open("cart.txt", "w") as file:
        file.write("\n".join(items))
    print(package_name + " removed from cart.")

def process_payment():
    with open("cart.txt", "r") as file:
        items = file.readlines()

    total_price = 0
    with open("bill.txt", "r") as file:
        packages = file.readlines()
        for package in packages:
            package_details = package.split(",")
            package_name = package_details[0].strip()
            package_price = float(package_details[1].strip())
            if package_name + "\n" in items:
                total_price += package_price

    print("Total Price:", total_price)

    with open("bill.txt", "w") as file:
        file.write("")

    print("Payment Successful. Thank you for your purchase!")


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
        print("         3. Add to Cart")
        print("         4. Remove from Cart")
        print("         5. Make Payment")
        print("         6. Exit")

        choice = input("\nPlease enter your choice ('1' or '2' or '3' or '4' or '5' or '6'): ")

        if choice == "1":
            display_packages(packages)
        elif choice == "2":
            view_cart()
        elif choice == "3":
            package_name = input("\nEnter the package name to add to cart: ")
            add_to_cart(package_name)
        elif choice == "4":
            package_name = input("\nEnter the package name to remove from cart: ")
            remove_from_cart(package_name)
        elif choice == "5":
            cart_items = []
            with open("cart.txt", "r") as file:
                cart_items = file.readlines()
            if len(cart_items) == 0:
                print("\nYOUR CART IS EMPTY !")
            else: 
                process_payment()
                exit(0)
        elif choice == "6":
            break
        else:
            print("\nInvalid Choice! Please try again.")

    print("\nTHANK YOU FOR CHOOSING FANTASTOS! HAVE A NICE DAY! ^_^")

