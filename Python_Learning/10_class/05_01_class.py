class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to be received arguments
        assert price >= 0, f"Price {price} is not greater than or equal zero"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal  zero"
            
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
         
    def cal_total_price(self):
        return self.price * self.quantity
        

item1 = Item("HP Laptop", 1000, 2)
item2 =Item("Tecno Phone", 300, 1)
# print(item1.name)
# print(item2.name)
# print(item2.quantity)

print(item1.cal_total_price())
print(item2.cal_total_price())