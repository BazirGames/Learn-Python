class ItemToPurchase:
    def __init__(self, name = 'none', price = 0, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")
        
if __name__ == "__main__":
    # Type main section of code here
    print("Item 1")
    item1 = ItemToPurchase( input("Enter the item name:\n"),int(input("Enter the item price:\n")) , int(input("Enter the item quantity:\n")))
    

    print("\nItem 2")
    item2 = ItemToPurchase( input("Enter the item name:\n"),int(input("Enter the item price:\n")) , int(input("Enter the item quantity:\n")))
    


    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()


    total_cost = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
    print(f"\nTotal: ${total_cost}")
