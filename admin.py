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
    print("Travel Packages:")
    if packages:
        for i, package in enumerate(packages, start=1):
            print(f"{i}. Name: {package['name']}, Destination: {package['destination']}, Price: {package['price']}")
    else:
        print("No travel packages found.")
        
def add_package(packages):
    name = input("Enter package name: ")
    destination = input("Enter destination: ")
    price = input("Enter price: ")
    package = {"name": name, "destination": destination, "price": price}
    packages.append(package)
    save_packages(packages)
    print("Package added successfully!")

def display_packages(packages):
    print("Travel Packages:")
    for i, package in enumerate(packages, start=1):
        print(f"{i}. Name: {package['name']}, Destination: {package['destination']}, Price: {package['price']}")

def edit_package(packages):
    display_packages(packages)
    index = int(input("Enter the index of the package to edit: ")) - 1
    if 0 <= index < len(packages):
        package = packages[index]
        print("Enter new values (leave blank to keep the existing value):")
        new_name = input(f"Name ({package['name']}): ") or package['name']
        new_destination = input(f"Destination ({package['destination']}): ") or package['destination']
        new_price = input(f"Price ({package['price']}): ") or package['price']
        package['name'] = new_name
        package['destination'] = new_destination
        package['price'] = new_price
        save_packages(packages)
        print("Package edited successfully!")
    else:
        print("Invalid package index!")

def delete_package(packages):
    display_packages(packages)
    index = int(input("Enter the index of the package to delete: ")) - 1
    if 0 <= index < len(packages):
        package = packages[index]
        packages.remove(package)
        save_packages(packages)
        print("Package deleted successfully!")
    else:
        print("Invalid package index!")

def main():
    current_directory = os.getcwd()
    abs_package_file_path = os.path.join(current_directory, PACKAGE_FILE)
    print("Travel package file path:", abs_package_file_path)

    packages = load_packages()
    while True:
        print("\n------ Travel Package Management ------")
        print("1. Add Package")
        print("2. Edit Package")
        print("3. Delete Package")
        print("4. View Packages")
        print("5. Exit")
        choice = input("Enter your choice: ")
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
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    # Check if the package file exists, otherwise create it
    if not os.path.isfile(PACKAGE_FILE):
        save_packages([])
    main()

