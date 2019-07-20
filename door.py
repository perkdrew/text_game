
# THE CLASS THAT SETS THE DOORS AND DETERMINES STATUS OF THE DOORS
class Door():
    def __init__(self, wall, status, linkedRooms):
        self.wall = wall
        self.status = status
        self.linkedRooms = linkedRooms

    def __str__(self):
        string = "{} - {}".format(self.linkedRooms[0],self.linkedRooms[1])
        return string

    def __repr__(self):
        return str(self)

    def getWall(self):
        return self.wall

    def getStatus(self):
        return self.status

    def getLinked(self):
        return self.linkedRooms
    
    def openDoor(self):
        if self.status == "closed":
            self.status = "open"
            print("The door is now open.")
  
    def unlockDoor(self, rucksack):
        if self.status == "locked":
            for item in rucksack:
                if "key" in item.getName():
                    self.status = "open"
                    print("You have unlocked the crawl space!")
        if self.status == "locked":
            print("The door needs a key. Have you checked the attic?")

