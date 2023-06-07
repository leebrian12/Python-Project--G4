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
