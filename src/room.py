# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to= None

    def addItem(self,item):
        self.items.append(item)

    def getItem(self,name):
        for i in range(0, len(self.items)):
            if(self.items[i].name == name):
                return self.items[i]


    def removeItem(self,item):
        index = None
        for i in range(0, len(self.items)):
            if(self.items[i].name == item.name):
                index = i
        if(index != None):
            self.items.pop(index)
