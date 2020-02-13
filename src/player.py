# Write a class to hold player information, e.g. what room they are in
# currently.
from time import sleep

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.room = starting_room
        self.inventory = []

    def __str__(self):
        return f"\nName: {self.name} \n{self.room}"

    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def remove_from_inventory(self, item):
        self.inventory.remove(item)
    
    def show_inventory(self):
        print('Loading inventory...')
        sleep(0.5)
        print('-- Your inventory --')
        for i in self.inventory:
            print(f' - {i}')

    def print_travel_err(self):
        print('                XXXXXXXXXXXX         ')
        sleep(0.05)
    
    def print_travel_success(self):
        print('\nNavigating...')
        sleep(0.5)

    def travel(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room == None:
            self.print_travel_err()
            self.print_travel_err()
            self.print_travel_err()
            self.print_travel_err()
            self.print_travel_err()
            self.print_travel_err()
            self.print_travel_err()
            print("\nAww shucks! You cannot move in that direction")
        else:
            self.room = next_room
            self.print_travel_success()
    
            