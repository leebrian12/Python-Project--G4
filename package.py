import ast
import os

PACKAGE_FILE = 'travel_packages.txt'

def save_packages(packages):
    with open(PACKAGE_FILE, 'w') as file:
        file.write(str(packages))

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
            print(f"{i}. Name: {package['name']}, Destination: {package['destination']}, Price:RM {package['price']}")
    else:
        print("\nTravel Package not Found!")
        
def add_package(packages):
    name = input("\nEnter package code (EXP: Package A): ")
    destination = input("Enter destination: ")
    price = input("Enter price per person (RM): ")
    package = {"Package Code": name, "Destination": destination, "Price per person (RM)": price}
    packages.append(package)
    save_packages(packages)
    print("\nPackage added successfully!")

def display_packages(packages):
    print("\n===== List of Travel Packages =====\n")
    for i, package in enumerate(packages, start=1):
        print(f"{i}. Name: {package['name']}, Destination: {package['destination']}, Price per person:RM {package['price']}")

def edit_package(packages):
    display_packages(packages)
    index = int(input("\nEnter the index of the package to edit (EXP: '1'): ")) - 1
    if 0 <= index < len(packages):
        package = packages[index]
        print("\nEnter new information (Leave blank to keep the existing info):")
        new_name = input(f"Name ({package['name']}): ") or package['name']
        new_destination = input(f"Destination ({package['destination']}): ") or package['destination']
        new_price = input(f"Price per person ({package['price']}): ") or package['price']
        package['name'] = new_name
        package['destination'] = new_destination
        package['price'] = new_price
        save_packages(packages)
        print("\nPackage edited successfully!")
    else:
        print("\nInvalid package index.Please try again!")

def delete_package(packages):
    display_packages(packages)
    index = int(input("\nEnter the index of the package to delete (EXP: '1'): ")) - 1
    if 0 <= index < len(packages):
        package = packages[index]
        packages.remove(package)
        save_packages(packages)
        print("\nPackage deleted successfully!")
    else:
        print("Invalid package index.Please try again!")

def main():
    current_directory = os.getcwd()
    abs_package_file_path = os.path.join(current_directory, PACKAGE_FILE)
    print("Travel package file path:", abs_package_file_path)

    packages = load_packages()
    while True:
        print("\n====== Travel Package Management ======")
        print("\n         1. Add Package")
        print("         2. Edit Package")
        print("         3. Delete Package")
        print("         4. View Packages")
        print("         5. Exit")
        choice = input("\nPlease enter your choice ('1' or '2' or '3' or '4' or '5'): ")
        if choice == "1":
            add_package(packages)
        elif choice == "2":
            edit_package(packages)
        elif choice == "3":
            delete_package(packages)
        elif choice == "4":
            display_packages(packages)
        elif choice == "5":
            break
        else:
            print("\nInvalid Choice! Please try again.")

def run_admin():
    if __name__ == '__main__':
        # Check if the package file exists, otherwise create it
        if not os.path.isfile(PACKAGE_FILE):
            save_packages([])
        main()
