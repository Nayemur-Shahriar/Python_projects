
class Menu:
    def __init__(self):
        self.Items=[]

    def add_menu_item(self, item):
        self.Items.append(item)
        print(f"Item {item.name} added to the menu.")

    def find_item(self, item_name):
        for item in self.Items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.Items.remove(item)
            print(f"Item {item_name} removed from the menu.")
        else:
            print(f"Item {item_name} not found in the menu.")

    def show_menu(self):
        if not self.Items:
            print("Menu is empty.")
            return
        
        print("******Menu Items:******")
        print("-------------------------")
        print("Name\tPrice\tQuantity")
        for item in self.Items:
            print(f"{item.name}   {item.price}    {item.quantity}")
