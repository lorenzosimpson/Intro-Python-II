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

print('\n\n\n\n\n\n\n')
# Make a new player object that is currently in the 'outside' room.
player = Player(input("Hi! What's your name? "), room['outside'])
print(f'Hello, {player.name}')
sleep(2)

# Assign the player's starting inventory
player.inventory = [item['watch']]

# list of valid moves
valid_direction = ['n', 's', 'e', 'w']


# ------------------Game logic --------------------

while True:
    # set current room, description, inventory
    current_room = player.room
    desc = current_room.description
    inventory = player.inventory
    print('\n\n\n\n\n\n\n')
    sleep(1)
    print(f"You're in  \n\n\n           *** {current_room.name.upper()} ***\n\n\n")
    sleep(0.5)
    player.room.print_room_items()

    sleep(1)
    # input
    choice = input('~~ What do you want to do? You can:\n \n          Move (n, s, e, w)\n \n          See your inventory (i)\n \n          Take an item (take item_name)\n \n          Drop item (drop item_name)\n \n          Quit (q):\n          ').lower()
    no_item = '\nThat item is not in this room!\n'
   
    

    if choice in valid_direction:
        sleep(1)
        player.travel(choice)

    # elif the player supplies two cmd words [action] [item]
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
        player.show_inventory()
    
    # Quit the game
    elif choice == 'q':
        print('Exiting...')
        sleep(2)
        print('Goodbye!')
        sleep(0.5)
        exit()
    # invalid move
    else:
        print('Invalid move, expected n, s, e or w')
    
