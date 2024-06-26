class Inventory:

    def __init__(self, __capacity: int, left_capacity=0):
        self.__capacity = __capacity
        self.items = []
        self.left_capacity = __capacity

    def add_item(self, item: str):
        if self.left_capacity > 0:
            self.items.append(item)
            self.left_capacity -= 1
        return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)