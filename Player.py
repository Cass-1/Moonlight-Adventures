from Entity import Entity
from Room import Room

class Player:

    CurrentRoom: Room

    def __init__(self, name, CurrentRoom, ItemList):
        self.name = name
        self.CurrentRoom = CurrentRoom
        self.ItemList = ItemList
