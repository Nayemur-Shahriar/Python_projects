class Product:
    id_counter = 1

    def __init__(self, name, price, stock):
        self.id = Product.id_counter
        Product.id_counter += 1
        self.name = name
        self.price = price
        self.stock = stock


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.orders = []

    def view_products(self, product_list):
        print("\n--- Available Products ---")
        found = False
        for product in product_list:
            if product.stock > 0:
                print(f"{product.id}. {product.name} - Price: {product.price}, Quantity: {product.stock}")
                found = True
        if not found:
            print("No products available at the moment.")

    def buy_product(self, product_list):
        self.view_products(product_list)
        try:
            product_id = int(input("Enter Product ID to buy: "))
            quantity = int(input("Enter Quantity: "))
            for product in product_list:
                if product.id == product_id:
                    if product.stock >= quantity:
                        product.stock -= quantity
                        self.orders.append((product.name, quantity))
                        print(f"Order placed for {quantity} of {product.name}")
                        return
                    else:
                        print("Not enough stock available.")
                        return
            print("Product ID not found.")
        except:
            print("Invalid input. Please enter numbers only.")


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def add_product(self, product_list):
        try:
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            stock = int(input("Enter Product Quantity: "))
            new_product = Product(name, price, stock)
            product_list.append(new_product)
            self.products.append(new_product)
            print(f"Product '{name}' added successfully.")
        except:
            print("Invalid input. Please enter correct values.")


class EShoppingApp:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def signup_customer(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")
        self.customers.append(Customer(email, password))
        print("Customer Sign Up Successful.\n")

    def signup_seller(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")
        self.sellers.append(Seller(email, password))
        print("Seller Sign Up Successful.\n")

    def login(self):
        email = input("Enter Your Email: ")
        password = input("Enter Your Password: ")

        print("Please Login:\nPress 1 for Customer\nPress 2 for Seller")
        role = input("-> ")

        if role == '1':
            for customer in self.customers:
                if customer.email == email and customer.password == password:
                    self.customer_menu(customer)
                    return
            print("Customer credentials incorrect.\n")

        elif role == '2':
            for seller in self.sellers:
                if seller.email == email and seller.password == password:
                    self.seller_menu(seller)
                    return
            print("Seller credentials incorrect.\n")
        else:
            print("Invalid role selection.\n")

    def customer_menu(self, customer):
        while True:
            print("\n--- Customer Dashboard ---")
            print("Press 1 to View and Buy Products")
            print("Press 2 to Return to Main Page")
            choice = input("-> ")
            if choice == '1':
                customer.buy_product(self.products)
            elif choice == '2':
                break
            else:
                print("Invalid input.")

    def seller_menu(self, seller):
        while True:
            print("\n--- Seller Dashboard ---")
            print("Press 1 to Add Product")
            print("Press 2 to Return to Main Page")
            choice = input("-> ")
            if choice == '1':
                seller.add_product(self.products)
            elif choice == '2':
                break
            else:
                print("Invalid input.")

    def run(self):
        while True:
            print("\n--> Main Page:")
            print("Press 1 for Sign Up as a Customer")
            print("Press 2 for Sign Up as a Seller")
            print("Press 3 for Login")
            print("Press 4 to Exit")
            choice = input("-> ")

            if choice == '1':
                self.signup_customer()
            elif choice == '2':
                self.signup_seller()
            elif choice == '3':
                self.login()
            elif choice == '4':
                print("Exiting Application.")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = EShoppingApp()
    app.run()
