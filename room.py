
# THE CLASS THAT CALLS THE ROOMS, AND INTERPRETS THE DOORS AND ITEMS IN SAID ROOMS
class Room():
    def __init__(self, name, doors, items):
        self.name = name
        self.doors = doors
        self.items = items

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def getDoors(self):
        return self.doors

    def getDetails(self):
        print("\n{}".format(self.name))
        print("--------------------")
        
        if self.name == "Anteroom":
            print("You are in the entrance hall to this beach estate.")

        elif self.name == "Dining_Hall":
            print("The table is set but no one has been sitting here for ages.")
            print("You smell a strange odor coming from somewhere.")
            print('''To try to guess the smell, type "smell room".''')

        elif self.name == "Attic":
            print("The room is dilapidated and damp, with squeaky floorboards.")

        elif self.name == "Library":
            print("There is literature from all over the world in here.")
            print("You notice a secret door behind the bookcase to the east.")

        elif self.name == "Ballroom":
            print("There are scuff marks from shoes all over the floor.")
            print("A lot of dancing must have gone on here.")

        elif self.name == "Atrium":
            print("A large panoramic window views back out to the beach.")
            print("You are surrounded by vegetation that crawls on the walls.")

        elif self.name == "Crawl_Space":
            print("You are in the cramped and sequestered room behind the bookcase.")

    def seeDetails(self):
        if len(self.doors) == 1:
            print("There is one door in the direction {}".format(self.doors[0][1]))
        else:
            doorScript = "There are doors in the direction "
            for door in self.doors:
                doorScript = doorScript + door[1] + ", "
            print(doorScript[:-2])
        if self.items != []:
            print("The items you can find here are:")
            for item in self.items:
                print(item.getName())

    def getItem(self, item, rucksack):
            for grab in self.items:
                if grab.getName() == item:
                    if grab.canMove() == False:
                        print("The {} cannot be taken.".format(item))
                        return rucksack
                    else:
                        if grab.canMove() == True:
                            rucksack.append(grab)
                            self.items.remove(grab)
                            print("The {} has been added to your rucksack. Pack wisely.".format(item))
                            return rucksack
            print("There is no item to take.")

    def setItem(self, item, rucksack):
        for held in rucksack:
            if held.getName() == item:
                self.items.append(held)
                rucksack.remove(held)
                print("The {} has been released.".format(item))
                return rucksack
        print("There is no item to release.")
