from food_item import FoodItem
from menu import Menu
from user import User, Customer, Employee, Admin
from orders import Order
from restaurant import Restaurant


mamar_dokan = Restaurant("Mamar Dokan")


def customer_menu():

    name= input("Enter your name: ")
    email = input("Enter your email: ") 
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    customer= Customer(name=name, email=email, phone=phone, address=address)
    

    while True:
    
        print("..........................................")
        print("Welcome to Mamar Dokan!")
        print(f"Dear {customer.name}, what would you like to do?")
        print("1. View Menu")
        print("2. Add Item to cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer.view_menu(mamar_dokan)

        elif choice == '2':
            item_name = input("Enter the name of the food item you want to order: ")
            item_quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(mamar_dokan, item_name, item_quantity)
            

        elif choice == '3':
             customer.view_cart()
        elif choice == '4':
            customer.pay_bill(mamar_dokan)

        elif choice == '5':
            print("Thank you for visiting Mamar Dokan!")
            break

        else:
            print("Invalid choice. Please try again.")



            # this part is for ADMIN section


def admin_menu():

    name= input("Enter your name: ")
    email = input("Enter your email: ") 
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    admin= Admin(name=name, email=email, phone=phone, address=address)
    

    while True:
    
        print("..........................................")
        print("Welcome to Mamar Dokan!")
        print(f"Dear {name}, what would you like to do?")
        print("1. Add new Item")
        print("2. Add new Employee")
        print("3. View Employees")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter the name of the food item: ")
            item_price = float(input("Enter the price of the food item: "))
            item_quantity = int(input("Enter the quantity of the food item: "))
            new_item = FoodItem(name=item_name, price=item_price, quantity=item_quantity)
            admin.add_new_item(mamar_dokan, new_item)

        elif choice == '2':
            emp_name = input("Enter the name of the employee: ")
            emp_email = input("Enter the email of the employee: ")
            emp_phone = input("Enter the phone number of the employee: ")
            emp_address = input("Enter the address of the employee: ")
            emp_age = int(input("Enter the age of the employee: "))
            emp_designation = input("Enter the designation of the employee: ")
            emp_salary = float(input("Enter the salary of the employee: "))

            new_employee = Employee(name=emp_name, email=emp_email, phone=emp_phone, address=emp_address, age=emp_age, designation=emp_designation, salary=emp_salary)
            admin.add_employee(mamar_dokan, new_employee)
            

        elif choice == '3':
             admin.view_employees(mamar_dokan)

        elif choice == '4':
            admin.view_menu(mamar_dokan)

        elif choice == '5':
            
            item_name = input("Enter the name of the food item to delete: ")
            admin.remove_item(mamar_dokan, item_name)
        
        elif choice == '6':
            print("Thank you for managing Mamar Dokan!")
            break

        else:
            print("Invalid choice. Please try again.")




while True:

    print("..........................................")
    print("Welcome  to Mamar Dokan!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        customer_menu()

    elif choice == '2':
        admin_menu()

    elif choice == '3':
        print("Thank you for visiting Mamar Dokan!")
        break
    else:
        print("Invalid choice. Please try again.")  
