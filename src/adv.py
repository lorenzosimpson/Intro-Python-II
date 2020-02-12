import sys
from room import Room
from player import Player
from item import Item
from time import sleep

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


# declare items

item = {
    'coin': Item('coin', 'money money money'),
    'sword': Item('sword', 'the sword in the stone'),
    'watch': Item('watch', 'tells the time'),
    'chest': Item('chest', 'a treasure chest'),
    'binoculars': Item('binoculars', 'to see far and wide'),
    'flashlight': Item('flashlight', 'to brighten the darkness')
}

# link items to rooms

room['outside'].room_items = [item['coin'], item['sword']]
room['foyer'].room_items = [item['watch']]
room['overlook'].room_items = [item['binoculars']]
room['narrow'].room_items = [item['flashlight']]


# Make a new player object that is currently in the 'outside' room.

player_1 = Player('Lorenzo', room['outside'])

# Assign the player's starting inventory

player_1.inventory = [item['watch']]






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

# list of valid moves

valid_cmd = ['n', 's', 'e', 'w', 'q']

while True:
    # set current room and description
    current_room = player_1.room
    desc = current_room.description
    inventory = player_1.inventory

    def player_inventory():
        for i in inventory:
            print(i)
    # print each item in the room
    def room_items():
        for i in current_room.room_items:
            print(i)
    
    print(f"Hey, {player_1.name}. You're currently in \n *** {current_room.name.upper()} *** \n")
    print('You currently have the following items in your inventory:')
    player_inventory()
    print('This room has the following items:')
    room_items()

    # input
    choice = input('~~ What do you want to do? You can: \nMove: (n, s, e, w) ')
    error = f'\n*** Aww shucks! *** \n*** Nothing there! ***\n'
    no_item = 'That item is not in this room!'
   
    print('-----------------------------------------------')

    if choice in valid_cmd:
        # NORTH
        sleep(1)
        if choice == 'n':
            if current_room.n_to == None:
                print(error)
            else:
                player_1.room = current_room.n_to
        # SOUTH
        elif choice == 's':
            if current_room.s_to == None:
                print(error)
            else:
                player_1.room = current_room.s_to
        # EAST
        elif choice == 'e':
            if current_room.e_to == None:
                print(error)
            else:
                player_1.room = current_room.e_to
        # WEST
        elif choice == 'w':
            if current_room.w_to == None:
                print(error)
            else:
                player_1.room = current_room.w_to    
    #if user enters q, quit game
        elif choice == 'q':
            print('Exiting...')
            sleep(2)
            print('Goodbye!')
            sleep(0.5)
            exit()
    #elif choice has 3 args
        # if arg 2 is take:
            # call remove method on room
            # add to player inventory 
        # else:
            # call add method on room
            # remove from inventory
    elif len(choice.split(' ')) == 2:
        action = choice.split(' ')[0]
        chosen_item = choice.split(' ')[1]

        if action == 'take':
            if item[chosen_item] in current_room.room_items:
                current_room.remove_item(item[chosen_item])
                player_1.add_to_inventory(item[chosen_item])
            else:
                print(no_item)
    
        elif action == 'drop':
            if item[chosen_item] in player_1.inventory:
                current_room.add_item(item[chosen_item])
                player_1.remove_from_inventory(item[chosen_item])
            else:
                print(no_item)
    # invalid move
    else:
        print('Invalid move, expected n, s, e or w')
    
