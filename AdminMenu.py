def admin_displayMenu():

    print("\n\t\t\t=== Admin Menu === ")
    print("1. Add Package")
    print("2. Edit Package")
    print("3. Delete Package")
    print("4. Back to Main Menu")

def add():

    print("\nAdding a Package...")

def edit():

    print("\nEditing a Package...")

def delete():

    print("\nDeleting a Package...")

def main(choice):

    choice=input("\nEnter your choice ('1' or '2' or '3' or '4'): ")

    if(choice == 1):
        add()
    elif(choice == 2):
        edit()
    elif(choice == 3):
        delete()
    else:
        print("Wrong Input!")
        




