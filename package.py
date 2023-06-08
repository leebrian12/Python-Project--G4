class TravelPackage:
    def __init__(self, name, destinations, price):
        self.name = name
        self.destinations = destinations
        self.price = price


class TravelPackageManager:
    def __init__(self):
        self.packages = []

    def add_package(self):
        name = input("Enter the package name: ")
        destinations = input("Enter the destinations (comma-separated): ").split(",")
        price = float(input("Enter the package price: "))
        package = TravelPackage(name, destinations, price)
        self.packages.append(package)
        print(f"Package '{name}' added successfully.")

    def edit_package(self):
        name = input("Enter the package name to edit: ")
        for package in self.packages:
            if package.name == name:
                new_name = input("Enter the new package name: ")
                new_destinations = input("Enter the new destinations (comma-separated): ").split(",")
                new_price = float(input("Enter the new package price: "))
                package.name = new_name
                package.destinations = new_destinations
                package.price = new_price
                print(f"Package '{name}' updated successfully.")
                return
        print(f"Package '{name}' not found.")

    def delete_package(self):
        name = input("Enter the package name to delete: ")
        for package in self.packages:
            if package.name == name:
                self.packages.remove(package)
                print(f"Package '{name}' deleted successfully.")
                return
        print(f"Package '{name}' not found.")

    def display_packages(self):
        if self.packages:
            print("Travel Packages:")
            for package in self.packages:
                print(f"- {package.name}: Destinations: {', '.join(package.destinations)}, Price: {package.price}")
        else:
            print("No travel packages found.")


# Example usage
manager = TravelPackageManager()

while True:
    print("\nMenu:")
    print("1. Add Travel Package")
    print("2. Edit Travel Package")
    print("3. Delete Travel Package")
    print("4. Display Travel Packages")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        manager.add_package()
    elif choice == "2":
        manager.edit_package()
    elif choice == "3":
        manager.delete_package()
    elif choice == "4":
        manager.display_packages()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")
