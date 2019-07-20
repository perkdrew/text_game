################
#    Casa      #
#     da       #
#   Saudade    #
################

import sys
import time
import random

from house import House
from player import Player

##############################

# THE CLASS THAT INTERPRETS THE GAME COMMANDS AND STARTS THE GAME
class Game():
    def __init__(self, house, player):
        self.player = player
        self.rooms = house.getRooms()
        self._curr = house.getStart()

    def init(self):
        while True:
            visitedRoom = False
            self.rooms[self._curr].getDetails()

            while visitedRoom == False:
                command = input(">>  ")
                
                # IMMUTABLE COMMANDS WITH NONSELECTIVE INPUT
                if command == "show":
                    self.rooms[self._curr].seeDetails()

                elif command == "holding":
                    print('The items in your rucksack are:\n {}'\
                        .format(self.player.getRucksack()))

                elif command == "commands":
                    print("go DIR, " "take ITEM, " "release ITEM, " "read ITEM, " \
                        "show, " "holding, " "smell room, " "commands, " "quit")

                elif command == "quit":
                    raise SystemExit

                elif command == "smell room":
                    if self._curr == "Dining_Hall":
                        randSmells = ["teen spirit??", "dirty shoes?!", "burnt hair?!", "spoiled sushi?!",\
                        "pickled herring??", "a dead rat?!", "rotten eggs?!", "cigarettes??", "a wet dog?"]
                        print("It smells like...")
                        time.sleep(1)
                        print(random.choice(randSmells))
                    else:
                        print("Quit trying to smell this room, you freak!")

                # MUTABLE COMMANDS WITH SELECTIVE INPUT
                elif len(command) >= 2:
                    command = command.split(" ", 1)
                    
                    if command[0] in ["go", "open", "unlock"]:
                        if len(command) >= 2:
                            if command[1] not in [door[1] for door in self.rooms[self._curr].getDoors()]:
                                print("You can't move in this direction.")
                            else:
                                # PASSING THROUGH ROOMS AS A LINKED LIST
                                for door in self.rooms[self._curr].getDoors():
                                    if command[1] == door[1] and door[0].getStatus() == "open":
                                        if command[0] == "go":
                                            for link in door[0].getLinked():
                                                if link != self._curr:
                                                    self._curr = link
                                                    visitedRoom = True
                                                    break
                                    elif command[1] == door[1] and door[0].getStatus() == "closed":
                                        if command[0] == "go":
                                            print("This door is closed.")
                                            break
                                        elif command[0] == "open":
                                            door[0].openDoor()
                                            break
                                    elif command [1] == door[1] and door[0].getStatus() == "locked":
                                        if command[0] == "go" or command[0] == "open":
                                            print("A key is required to unlock this door.")
                                            break
                                        elif command[0] == "unlock":
                                            door[0].unlockDoor(self.player.getRucksack())
                                            break
                        else:
                            print("You need to specify a direction.")

                    elif command[0] == "take":
                        if len(command) >= 2:
                            self.rooms[self._curr].getItem(command[1], self.player.getRucksack())
                        else:
                            print("What item would you like to take?")

                    elif command[0] == "release":
                        if len(command) >= 2:
                            self.rooms[self._curr].setItem(command[1], self.player.getRucksack())
                        else:
                            print("What item would you like to release?")

                    elif command[0] == "read":
                        if len(command) >= 2:

                            if command[1] == "scroll":
                                scroll = False
                                for item in self.player.getRucksack():
                                    if "scroll" in item.getName():
                                        print("First, you must finish this sentence:")
                                        print("'All those moments will be lost in time...'")
                                        answer = input(">> ")
                                        if answer == "like tears in rain" or answer == "like tears in rain.":
                                            time.sleep(0.5)
                                            print("The scroll reads:")
                                            time.sleep(1)
                                            print("'It hurts to set you free,")
                                            time.sleep(1)
                                            print("but you'll never follow me,")
                                            time.sleep(1)
                                            print("the end of laughter and soft lies")
                                            time.sleep(1)
                                            print("the end of nights we tried to die,")
                                            time.sleep(1)
                                            print("this is the end.'")
                                            time.sleep(3)
                                            raise SystemExit
                                        else:
                                            scroll = True
                                            print("Sorry, you are not worthy.")
                                if not scroll:
                                    print("You don't have a scroll in your rucksack.")


                            elif command[1] == "novel":
                                novel = False
                                for item in self.player.getRucksack():
                                    if "novel" in item.getName():
                                        randSent = ["'I took a deep breath and listened to the old brag of my heart; I am, I am, I am.'",\
                                        "'Sometimes I can feel my bones straining under the weight of all the lives I'm not living.'",\
                                        "'He stepped down trying not to look at her, as if she were the sun, yet he saw her like the sun without even looking.'",
                                        "'The curves of your lips rewrite history.'",\
                                        "'A dream, all a dream, that ends in nothing, and leaves the sleeper where he lay down, but I wish you to know that you inspired it.'",\
                                        "'So we beat on, boats against the current, borne back ceaselessly into the past.'",\
                                        "'I could hear the human noise we sat there making, not one of us moving, not even when the room went dark.'",\
                                        "'Journeys end in lovers meeting.'",\
                                        "'What is hell? I maintain that it is the suffering of being unable to love.'",\
                                        "'When the heart speaks, the mind finds it indecent to object.'"]
                                        print("You read a sentence from the novel:")
                                        time.sleep(1)
                                        print(random.choice(randSent))
                                        novel = True
                                        break
                                if not novel:
                                    print("You don't have a novel in your rucksack.")                             
                        else:
                            print("What would you like to read?")


                # COMMAND FOR NO PROPER INPUT
                else:
                    print("Invalid command.")

##############################

#INTRO PRINT
print("\nBem-vindo à Casa da Saudade!")
print("You have stumbled upon this beach house on the shores of Portugal.")
print('''There is a sign at the front door that reads,\n 
               "For I will shelter you.
                And I will comfort you.
                And even when we are nothing left,
                not even in death,
                I will remember you."\n''')     
print("You decide to enter the house and explore its many mysteries.")
time.sleep(1)

#START GAME
game = Game(House(sys.argv[1]), Player())
game.init()

