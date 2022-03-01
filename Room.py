class Room:

    north: 'Room'
    south: 'Room'
    east: 'Room'
    west: 'Room'
    name: str
    lightLevel: int

    #TODO entities: EntityList
    #TODO items: ItemList
    #? descriptions: DiscriptionList


    def __init__(self, name = None, north = None, south = None, east = None, west = None, lightLevel = 0):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.lightLevel = lightLevel

        # if direction is not entered, make that direction point to self
        # else make sure the rooms point at each other
        if north == None:
            self.north = self
        else:
            north.south = self

        if south == None:
            self.south = self
        else:
            south.north = self

        if east == None:
            self.east = self
        else:
            east.west = self

        if west == None:
            self.west = self
        else:
            west.east = self


    