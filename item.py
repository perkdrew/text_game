
# THE CLASS THAT CALLS THE ITEMS AND THE PORTABILITY OF THE ITEMS
class Item():
    def __init__(self, name):
        self.name = name
        self.move = False
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def canMove(self):
        return self.move


#ITEM INHERITANCE 

class Portable(Item):
    def __init__(self, name):
        Item.__init__(self, name)
        self.move = True

class Playable(Item):
    def __init__(self, name, tool, text):
        Item.__init__(self, name)
        self._tool = tool
        self._text = text
        self.move = True

