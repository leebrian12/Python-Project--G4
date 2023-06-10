import ast

def main():

    display_menu()

    # Create an empty cart for the customer
    cart = []

    # Prompt the user for input and process their choice
    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            check_package()
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            add_to_cart(cart)
        elif choice == "4":
            remove_from_cart(cart)
        elif choice == "5":
           calculate_bill(cart)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    cleanup_system()

def display_menu():
    print("===== Travel Management System =====")
    print("1. Check Package")
    print("2. View Cart")
    print("3. Add Item to Cart")
    print("4. Remove Item from Cart")
    print("5. Payment")
    print("6. Exit")

def check_package(package_name):
    # Assume we have a list of available packages
    available_packages = [
    package1 = TravelPackage("Package A", "Pulau Langkawi", 150.00)
    package2 = TravelPackage("Package B", "Pulau Redang", 120.00)
    package3 = TravelPackage("Package C", "Pulau Ketam", 100.00)
    package4 = TravelPackage("Package D","Genting Highlands",350.00)
    package5 = TravelPackage("Package E","Cameron Highlands",300.00)
    ]
   
def view_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Your cart contains the following packages:")
            for item in self.cart_items:
                print(f"- {item.package_name} | Destination: {item.destination} | Price: RM{item.price}")

def add_to_cart(self, package):
        self.cart_items.append(package)

def remove_from_cart(self, package):
        self.cart_items.remove(package)

def calculate_total_cost(self):
        return self.num_travelers * self.rate

def calculate_bill(cart):
        total_cost = self.calculate_total_cost()
        tax_rate = 0.1  # 10% tax rate
        tax_amount = total_cost * tax_rate
        bill_amount = total_cost + tax_amount
        return bill_amount

def cleanup_system():
    print("Cleaning up travel management system...")

# Entry point of the program
if __name__ == "__main__":
    main()