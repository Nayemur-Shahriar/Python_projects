class Order:

    def __init__(self):
        self.items = {}

    def add_item(self, item):

        for existing_item in self.items:
            if existing_item.name == item.name:   
             self.items[existing_item] += item.quantity
             return
        else:
            self.items[item] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Item {item.name} not found in the order.")

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items= {}