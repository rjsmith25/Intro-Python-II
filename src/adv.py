from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to room
room['foyer'].addItem(Item("potion", "A healing potion, to restore health"))
room['foyer'].addItem(Item("key", "A rusted old key, looks badly damaged"))

room['overlook'].addItem(Item("sword", "A long sword, a sturdy sword fit for battle"))
room['overlook'].addItem(Item("shield", "A Shield, good for defense"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('frank', 'Outside Cave Entrance')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

user_input = None

def getRoomNameDictKey(room_name):
    if room_name == 'Outside Cave Entrance':
        return 'outside'
    if room_name == 'Foyer':
        return 'foyer'
    if room_name == 'Grand Overlook':
        return 'overlook'
    if room_name == 'Narrow Passage':
        return 'narrow'
    if room_name == 'Treasure Chamber':
        return 'treasure'

def printRoomItems(room):
    print(f"Current Items in {room.name}:", end=" ")
    for item in room.items:
        print(f"{item.name}", end=" ")
    print("\n")




while user_input != "q":
    print("")
    print(player.current_room)
    print(room[getRoomNameDictKey(player.current_room)].description)
    print("")
    if room[getRoomNameDictKey(player.current_room)].items:
        printRoomItems(room[getRoomNameDictKey(player.current_room)])

    user_input = input("Enter direction or q to quit: ")

    #handle case to bring up inventory
    if user_input == "i":
        player.printInventoryItems()

    # handle case for geting and droping items as a player
    parse_input = user_input.split()
    if len(parse_input) == 2:
        if parse_input[0] == "get" or parse_input[0] == "take":
            selected_Item = room[getRoomNameDictKey(player.current_room)].getItem(parse_input[1])
            if(selected_Item):
                player.addInventoryItem(selected_Item)
                room[getRoomNameDictKey(player.current_room)].removeItem(selected_Item)
                selected_Item.on_take()
            else:
                print("")
                print("Item is not there")
        if parse_input[0] == "drop" or parse_input[0] == "remove":
            selected_Item = player.getInventoryItem(parse_input[1]);
            if(selected_Item):
                player.removeInventoryItem(selected_Item)
                selected_Item.on_drop()
            else:
                print("")
                print("Item is not there")

    # handle case for navigating the rooms as a player
    if user_input == "n" or user_input == "s" or user_input == "e" or user_input == "w":
        if user_input == "n":
            if room[getRoomNameDictKey(player.current_room)].n_to != None:
                player.current_room = room[getRoomNameDictKey(player.current_room)].n_to.name
            else:
                print("Movement isn't allowed.")
        if user_input == "s":
            if room[getRoomNameDictKey(player.current_room)].s_to != None:
                player.current_room = room[getRoomNameDictKey(player.current_room)].s_to.name
            else:
                print("Movement isn't allowed.")
        if user_input == "e":
            if room[getRoomNameDictKey(player.current_room)].e_to != None:
                player.current_room = room[getRoomNameDictKey(player.current_room)].e_to.name
            else:
                print("Movement isn't allowed.")
        if user_input == "w":
            if room[getRoomNameDictKey(player.current_room)].w_to != None:
                player.current_room = room[getRoomNameDictKey(player.current_room)].w_to.name
            else:
                print("Movement isn't allowed.")
