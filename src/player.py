# Write a class to hold player information, e.g. what room they are in
# currently.
from time import sleep

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"\nName: {self.name} \n{self.room}"

    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def remove_from_inventory(self, item):
        self.inventory.remove(item)
    
    def player_inventory(self):
        print('Loading inventory...')
        sleep(0.5)
        print('-- Your inventory --')
        for i in self.inventory:
            print(f' - {i}')