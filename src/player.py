# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def getInventoryItem(self,name):
        for i in range(0, len(self.inventory)):
            if(self.inventory[i].name == name):
                return self.inventory[i]

    def addInventoryItem(self,item):
        self.inventory.append(item)

    def removeInventoryItem(self, item):
        index = None
        for i in range(0, len(self.inventory)):
            if(self.inventory[i].name == item.name):
                index = i
        if(index != None):
            self.inventory.pop(index)
