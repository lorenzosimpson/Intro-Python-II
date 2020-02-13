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
player = Player('Lorenzo', room['outside'])

# Assign the player's starting inventory
player.inventory = [item['watch']]


# list of valid moves
valid_cmd = ['n', 's', 'e', 'w', 'q']



def greet_player():
    print(f'Welcome, {player.name}!\nLoading game...\n\n')
greet_player() # invoke upon loading the game, not in every loop




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


# ------------------Game logic --------------------
sleep(2)
while True:
    # set current room and description
    current_room = player.room
    desc = current_room.description
    inventory = player.inventory
    
    print(f"You're currently in *** {current_room.name.upper()} ***\n\n\n")
    current_room.print_room_items()
    # input
    choice = input('~~ What do you want to do? You can: \nMove (n, s, e, w), See your inventory (i), take an item (take item_name), drop item (drop item_name) or quit (q): ')
    error = f'\n*** Aww shucks! *** \n*** Nothing there! ***\n'
    no_item = 'That item is not in this room!'
   
    print('-----------------------------------------------')

    if choice in valid_cmd:
        # player chooses NORTH
        sleep(1)
        if choice == 'n':
            # if the room has nowhere to go in that direction
            if current_room.n_to == None:
                print(error)
            else:
                player.room = current_room.n_to
        # player chooses SOUTH
        elif choice == 's':
            if current_room.s_to == None:
                print(error)
            else:
                player.room = current_room.s_to
        # player chooses EAST
        elif choice == 'e':
            if current_room.e_to == None:
                print(error)
            else:
                player.room = current_room.e_to
        # player chooses WEST
        elif choice == 'w':
            if current_room.w_to == None:
                print(error)
            else:
                player.room = current_room.w_to    
    #if user enters q, quit game
        elif choice == 'q':
            print('Exiting...')
            sleep(2)
            print('Goodbye!')
            sleep(0.5)
            exit()

    # if the player supplies two cmd words [action] [item]
    elif len(choice.split(' ')) == 2:
        sleep(1)
        action = choice.split(' ')[0]
        chosen_item = choice.split(' ')[1]

        if action == 'take' or action == 'get':
            # if the room has that item
            if item[chosen_item] in current_room.room_items:
                current_room.remove_item(item[chosen_item])
                player.add_to_inventory(item[chosen_item])
                item[chosen_item].on_take()
            else:
                print(no_item)
    
        elif action == 'drop':
            # if the player has that item
            if item[chosen_item] in player.inventory:
                current_room.add_item(item[chosen_item])
                player.remove_from_inventory(item[chosen_item])
                item[chosen_item].on_drop()
            else:
                print(no_item)
    # print player inventory
    elif choice == 'i' or choice == 'inventory':
        player.player_inventory()
    # invalid move
    else:
        print('Invalid move, expected n, s, e or w')
    
