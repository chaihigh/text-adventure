class House:
    """it's a house yay.

    attributes: list of Rooms"""
    
    def __init__(self, rooms):
        """Store a list of the House's Rooms.

        House, list of Rooms -> None"""
        
        self.rooms = rooms

class Room:
    """It's a room.

    attributes: name (string), list of adjacent Rooms, \
    list of Objects"""


    def __init__(self, name, adj=[], obj=[]):
        """Store the attributes.

        Room, string, list of Rooms, list of Objects"""

        self.name = name
        self.adj = adj
        self.obj = obj

    def list_obj(self):
        """List the Objects in the Room.

        Room -> string"""

        obj_list = ""
        for obj in self.obj:
            if obj_list == "":
                obj_list = obj.name
            else:
                obj_list = obj_list+", "+obj.name
                
        return "Objects in this room: "+obj_list

    def list_adj(self):
        """List the Room adjacent to this one.

        Room -> string"""

        adj_list = ""
        for room in self.adj:
            if adj_list == "":
                adj_list = room.name
            else:
                adj_list = adj_list+", "+room.name
                
        return "Rooms you can go to from here: "+adj_list

class Object:
    """It's an Object.

    attributes: name (string), description (string)"""

    def __init__(self, name, desc):
        """Store the name and description of the Object.

        string, string -> None"""

        self.name = name
        self.desc = desc

coat = Object("coat", "a light rain coat")
sunglasses = Object("sunglasses", "a pair of heavy-framed sunglasses")

knife = Object("knife", "a sharp blade for preparing food")
toaster = Object("toaster", "a somewhat battered toaster oven")

remote = Object("remote", "a rectangular, black remote control")
change = Object("loose change", "a pile of loose change")
key = Object("small key", "a little brass key")

pen = Object("pen", "a slender, black, ballpoint pen")
paper = Object("paper", "a piece of note paper with something scrawled across it")

glasses = Object("reading glasses", "a sturdy pair of reading glasses")
magazine = Object("magazine", "a magazine with a scholarly woman on the cover")

entryway = Room("entryway", [], [coat, sunglasses])
living_room = Room("living room", [], [remote, change, key])
kitchen = Room("kitchen", [], [knife, toaster])
office = Room("office", [], [pen, paper])
sun_room = Room("sun room", [], [glasses, magazine])

entryway.adj = [living_room, kitchen]
living_room.adj = [kitchen, entryway, office]
kitchen.adj = [entryway, living_room, sun_room]
office.adj = [living_room]
sun_room.adj = [kitchen]

class Player:
    """It's a person hurrah.

    attributes: location (Room)"""

    def __init__(self, loc, inven=[]):
        """Store the Player's location and inventory.

        Player, Room, list of Objects -> None"""

        self.loc = loc
        self.inven = inven

player1 = Player(entryway)

print("Welcome to the test adventure game!\n\nYou are standing in the entryway of a small house.\n")

office_open = False

val = True
while val == True:
    
    #Options:
    print(player1.loc.list_adj()+' [type "go to ROOM"]')
    if player1.loc.obj == []:
        print("There are no objects in this room.")
    else:
        print(player1.loc.list_obj()+' [type "take OBJECT" or "examine OBJECT"]')
    print('[type "check inventory"]')
    print("")

    inp = input()
    print("")

    if inp.lower().startswith("go to"):
        if inp[6:] == "office" and office_open == False:
            if key in player1.inven:
                player1.loc = office
                office_open = True
                print("You slip the small key into the lock and enter the office.\n")
            else:
                print("You try to turn the handle, but the door is locked.\n")
        else:
            valid_loc = False
            for room in player1.loc.adj:
                if room.name == inp[6:]:
                    valid_loc = True
                    player1.loc = room
                    print("You are standing in the "+player1.loc.name+".\n")
            if valid_loc == False:
                print("[invalid location, please try again]\n")
                    
    elif inp.lower().startswith("take"):
        if inp[5:] == "paper":
            print("It's pinned into the desk.\n")
        else:
            for obj in player1.loc.obj:
                if obj.name == inp[5:]:
                    player1.inven.append(obj)
                    player1.loc.obj.remove(obj)
                    print("You slip the "+obj.name+" into your bag.\n")
    elif inp.lower().startswith("examine"):
        if inp[8:] == "paper":
            if glasses in player1.inven:
                print('You tilt your head to read the scrawl. It says, "This is the point where I ran out of immediate goal ideas and also got very tired. Congratulations, you beat the game."')
                print("\nA small confetti canon explodes overhead and showers you with colorful scraps of paper.")
                val = "congrats"
            else:
                print("It has something scrawled accros it, but you can't read it without your glasses.\n")
        else:
            for obj in player1.loc.obj:
                if obj.name == inp[8:]:
                    print("It's "+obj.desc+".\n")
    elif inp.lower() == "check inventory":
        if player1.inven == []:
            print("There is nothing in your inventory.\n")
        else:
            inven_str = ""
            for obj in player1.inven:
                if inven_str == "":
                    inven_str = obj.name
                else:
                    inven_str = inven_str+", "+obj.name
            print("You have these items: "+inven_str+"\n")
    
    else:
        print("[invalid command, please try again]"+"\n")
