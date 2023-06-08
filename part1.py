#add order function#
class TravelOrder:
    def __init__(self, customer_name, destination, travel_date, num_travelers):
        self.customer_name = customer_name
        self.destination = destination
        self.travel_date = travel_date
        self.num_travelers = num_travelers

orders = []

def add_order():
    customer_name = input("Enter customer name: ")
    destination = input("Enter destination: ")
    travel_date = input("Enter travel date: ")
    num_travelers = int(input("Enter the number of travelers: "))

    order = TravelOrder(customer_name, destination, travel_date, num_travelers)
    orders.append(order)

    print("Order added successfully!")

# Example usage
add_order()

#getdiscount function#

class TravelOrder:
    def __init__(self, customer_name, destination, travel_date, num_travelers):
        self.customer_name = customer_name
        self.destination = destination
        self.travel_date = travel_date
        self.num_travelers = num_travelers

    def calculate_total_cost(self):
        # Add your logic to calculate the total cost here
        # This is just a placeholder example
        base_cost = 1000
        return base_cost * self.num_travelers

    def get_discount(self):
        total_cost = self.calculate_total_cost()
        if self.num_travelers >= 5:
            discount = 0.1  # 10% discount for 5 or more travelers
        else:
            discount = 0.0

        discount_amount = total_cost * discount
        return discount_amount

# Example usage
order = TravelOrder("John Doe", "Paris", "2023-08-20", 6)
discount = order.get_discount()
print(f"The discount amount is: RM{discount:.2f}")

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
order = TravelOrder("John Doe", "Paris", "2023-08-20", 6, 1000)
bill = order.calculate_bill()
print(f"The bill amount is: RM {bill:.2f}")


#check package
class TravelPackage:
    def __init__(self, package_name, destination, price, availability):
        self.package_name = package_name
        self.destination = destination
        self.price = price
        self.availability = availability

def check_package(package_name):
    # Assume we have a list of available packages
    available_packages = [
        TravelPackage("Package A", "Paris", 2000, 5),
        TravelPackage("Package B", "Tokyo", 2500, 3),
        TravelPackage("Package C", "New York", 1800, 8),
    ]

    for package in available_packages:
        if package.package_name == package_name:
            return package

    return None

# Example usage
package_name = input("Enter the package name: ")
package = check_package(package_name)

if package:
    print(f"Package: {package.package_name}")
    print(f"Destination: {package.destination}")
    print(f"Price: ${package.price}")
    print(f"Availability: {package.availability} spots")
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
                print(f"- {item.package_name} | Destination: {item.destination} | Price: ${item.price}")

# Example usage
cart = TravelCart()

# Add packages to the cart
package1 = TravelPackage("Package A", "Paris", 2000)
package2 = TravelPackage("Package B", "Tokyo", 2500)
package3 = TravelPackage("Package C", "New York", 1800)

cart.add_to_cart(package1)
cart.add_to_cart(package2)
cart.add_to_cart(package3)

# View the cart
cart.view_cart()
