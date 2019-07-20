# THE CLASS THAT CONTAINS THE INVENTORY FOR THE ITEMS TO TAKE AND RELEASE WITH THE PLAYER.
class Player():
    def __init__(self):
        self.rucksack = []
    
    def getRucksack(self):
        return self.rucksack