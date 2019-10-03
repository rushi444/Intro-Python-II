from room import Room
from player import Player
from item import Item

# Declare all the rooms and items

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

items = {
    'iphone': Item('iphone', 'A cell phone'),
    'ps4': Item('ps4', 'A gaming console'),
    'sunglasses': (Item('sunglasses', 'Protects eyes from sunlight')),
    'gun': (Item('gun', 'Use to kill zombies')),
    'laptop': (Item('laptop', 'Portable computer')),
    'headphones': (Item('headphones', 'Keep the slaps coming')),
    'flashlight': (Item('flashlight', 'Used to see in the dark'))
}

room['outside'].itemList = items['sunglasses']
room['foyer'].itemList = items['ps4'], items['gun']
room['overlook'].itemList = items['sunglasses']
room['narrow'].itemList = items['flashlight']
room['treasure'].itemList = items['laptop'], items['iphone'], items['headphones']


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Justin', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.

valid = ('n', 's', 'e', 'w')



if __name__ == '__main__':
    while True:
        print(player)
        direction = input("\nIf you would like to go to a different room: n(north), w(west), s(south), e(east):\nIf you would like to take/drop an item type take or drop:")
        if direction in valid:
            if player.room.get_directions(direction) is None:
                print('Invalid Direction, you cannot go that way')
            else:
                player.travel(direction)
                print(player)
        elif direction == 'q':
            break
        elif direction == 'take':
            takeItem = input('What item do you want?') 
            player.addItems(takeItem)
            print(player)
        else:
            print("Not a valid command!!")
        




#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
