
from room import Room
from door import Door
from item import Item, Portable, Playable

# THE CLASS THAT INTERPRETS THE CONFIGURATION TXT TO CREATE GAME
class House():
    def __init__(self, importConfig):
        self.rooms = {}
        self.doors = []
        self.items = {}
        self.startRoom = None
        with open(importConfig) as config:
            houseConfig = [line.rstrip("\n") for line in config]
            houseConfig = [line.split(" ") for line in houseConfig]
            for i in range(len(houseConfig)):
                if houseConfig[i][0] == "room":
                    self.rooms[houseConfig[i][1]] = None
                    self.items[houseConfig[i][1]] = []
                elif houseConfig[i][0] == "door":
                    self.doors.append(Door(houseConfig[i][1],houseConfig[i][2],\
                        (houseConfig[i][3], houseConfig[i][4])))
                elif houseConfig[i][0] == "item":
                    if houseConfig[i][3] == "STATIONARY":
                        self.items[houseConfig[i][2]].append(Item(houseConfig[i][1]))
                    elif houseConfig[i][3] == "MOVE":
                        self.items[houseConfig[i][2]].append(Portable(houseConfig[i][1]))
                    elif houseConfig[i][3] == "USE":
                        self.items[houseConfig[i][2]].append(Playable(houseConfig[i][1], \
                            houseConfig[i][4], houseConfig[i][5]))
                    elif houseConfig[i][3] == "READ":
                        self.items[houseConfig[i][2]].append(Playable(houseConfig[i][1], \
                            houseConfig[i][4], houseConfig[i][5]))
                elif houseConfig[i][0] == "start":
                    self.start = houseConfig[i][1]
        # SETTING THE HOUSE WITH DOORS IN POSITION AND ITEMS IN ROOMS
        for room in self.rooms:
            self.rooms[room] = []
            for door in self.doors:
                if str(door).startswith(room):
                    self.rooms[room].append((door, door.getWall()[0]))
                elif str(door).endswith(room):
                    self.rooms[room].append((door, door.getWall()[-1]))
            self.rooms[room] = Room(room, self.rooms[room], self.items[room])

    def getRooms(self):
        return self.rooms

    def getStart(self):
        return self.start