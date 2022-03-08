from Item import Item
class Weapon(Item):
    #durability
    #damage
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
