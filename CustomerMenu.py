import os

def display_packages():
    print("Available Travel Packages:")
    with open("travel_packages.txt", "r") as file:
        packages = file.readlines()
        for package in packages:
            print(package.strip())

def view_cart():
    print("Your Cart:")
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

    print("Payment processed. Thank you for your purchase!")

if not os.path.exists("cart.txt"):
    with open("cart.txt", "w") as file:
        file.write("")

while True:
    print("\n--- Travel Package Store ---")
    print("1. View Packages")
    print("2. View Cart")
    print("3. Add to Cart")
    print("4. Remove from Cart")
    print("5. Make Payment")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        display_packages()
    elif choice == "2":
        view_cart()
    elif choice == "3":
        package_name = input("Enter the package name to add to cart: ")
        add_to_cart(package_name)
    elif choice == "4":
        package_name = input("Enter the package name to remove from cart: ")
        remove_from_cart(package_name)
    elif choice == "5":
        cart_items = []
        with open("cart.txt", "r") as file:
            cart_items = file.readlines()
        if len(cart_items) == 0:
            print("Your cart is empty.")
        else:
            process_payment()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for visiting our travel package store!")