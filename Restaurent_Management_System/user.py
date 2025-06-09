from abc import ABC
from restaurant import Restaurant
from orders import Order
from food_item import FoodItem

class User(ABC):
    def __init__(self, name, email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:

            if quantity> item.quantity:
                print("Sorry, Item quantity exceeded.")

            else:
                new_item = FoodItem(item.name, item.price, quantity)  
                self.cart.add_item(new_item)
                item.quantity -= quantity 
                print(f"{quantity} {item.name}(s) added to cart.")
        else:
            print(f"Item {item_name} not found in the menu.")

    def view_cart(self):
        if not self.cart.items:
            print("Cart is empty.")
            return
        
        print("Cart Items:")
        print("-------------------------")
        print("Name\tPrice\tQuantity")

        for item, quantity in self.cart.items.items():
            print(f"{item.name}   {item.price}     {quantity}")

        print(f"Total Price: $ {self.cart.total_price}")

    def pay_bill(self,restaurant):
        print(f"Total {self.cart.total_price} paid successfully")
        self.cart.clear()



class Employee(User):

    def __init__( self,name, email,phone, address, age,designation, salary):
        super().__init__(name, email, phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
    

    def add_employee(self,Restaurent,employee):
        Restaurent.add_employee(employee)

    def view_employees(self,restaurent):
         restaurent.view_employees()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
       



