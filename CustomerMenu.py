def customer_displayMenu():

    print("=== Customer Menu === ")
    print("1. Check Package")
    print("2. View Cart")
    print("3. Payment")
    print("4. Exit")

    choice=input("\nEnter your choice ('1' or '2' or '3' or '4'): ")

    if choice == '1':
        print(check_package())
    elif choice == '2':
       print(TravelCart())
    elif choice == '3':
        print(TravelOrder())


customer_displayMenu()

def check_package(package_name):
    # Assume we have a list of available packages
    available_packages = [
        TravelPackage("Package A", "Pulau Langkawi", 150.00),
        TravelPackage("Package B", "Pulau Redang", 120.00),
        TravelPackage("Package C", "Pulau Ketam", 100.00),
        TravelPackage("Package D","Genting Highlands",350.00),
        TravelPackage("Package E","Cameron Highlands",300.00),
    ]

    for package in available_packages:
        if package.package_name == package_name:
            return package

    return customer_displayMenu

package_name = input("Enter the package name: ")
package = check_package(package_name)

if package:
    print(f"Package: {package.package_name}")
    print(f"Destination: {package.destination}")
    print(f"Price: RM {package.price}")

else:
    print("Package not found!")

#view cart 
class TravelPackage:
    def __init__(self, package_name, destination, price):
        self.package_name = package_name
        self.destination = destination
        self.price = price

class TravelCart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, package):
        self.cart_items.append(package)

    def remove_from_cart(self, package):
        self.cart_items.remove(package)

    def view_cart(self):
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Your cart contains the following packages:")
            for item in self.cart_items:
                print(f"- {item.package_name} | Destination: {item.destination} | Price: RM{item.price}")

# Example usage
cart = TravelCart()

# Add packages to the cart
package1 = TravelPackage("Package A", "Pulau Langkawi", 150.00)
package2 = TravelPackage("Package B", "Pulau Redang", 120.00)
package3 = TravelPackage("Package C", "Pulau Ketam", 100.00)
package4 = TravelPackage("Package D","Genting Highlands",350.00)
package5 = TravelPackage("Package E","Cameron Highlands",300.00)

cart.add_to_cart(package1)
cart.add_to_cart(package2)
cart.add_to_cart(package3)
cart.add_to_cart(package4)
cart.add_to_cart(package5)

# View the cart
cart.view_cart()


# Calculate Bill function
class TravelOrder:
    def __init__(self, customer_name, destination, travel_date, num_travelers, rate):
        self.customer_name = customer_name
        self.destination = destination
        self.travel_date = travel_date
        self.num_travelers = num_travelers
        self.rate = rate

    def calculate_total_cost(self):
        return self.num_travelers * self.rate

    def calculate_bill(self):
        total_cost = self.calculate_total_cost()
        tax_rate = 0.1  # 10% tax rate
        tax_amount = total_cost * tax_rate
        bill_amount = total_cost + tax_amount
        return bill_amount

# Example usage
order = TravelOrder("Brian Lee", "Pulau Langkawi", "2023-08-20", 150.00)