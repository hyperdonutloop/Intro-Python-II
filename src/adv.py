from room import Room
from player import Player
from item import Item
import os

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

room['outside'].n_to = room['foyer'] ## done
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items = [Item('Key', 'This opens the door to the cave'), Item('Gold', 'bag of 100 gold')]


# options

movement_options = [
    'n',
    's',
    'e',
    'w',
    'i',
    'q'
]

action_options = [
    'take',
    'drop'
]
# Main
## Functions
def show_welcome_message():
    welcome_message = (f'Welcome {player.name} You are in the room: {player.currentRoom}')
    print(welcome_message)

def display_messages():
    # 
    print(f'{player.currentRoom.description}')
    print(f"{player.currentRoom.name}")
    player.currentRoom.display_items_list()

def get_user_choice():
    return input('Go explore. Choose: north, south, east, west, or quit\n')
    

def gameActions(input):
    split = input.split(' ')
    print(split)

    if len(split) == 2:
        action = split[0]
        item = split[1].capitalize()
        
        print(f'Performing action: {split[0]}')
        if action == action_options[0]: #take
            for i in player.currentRoom.items:
                if i.name == item:
                    print(f'FOUND {item} in {player.currentRoom}')
                    player.getItem(i)
                    player.currentRoom.removeItem(i)
                    
    elif len(split) == 1:
        if input in movement_options:
            player.move(input)
        else:
            print('Invalid Choice def')
    else:
        print('Invalid Choice abc')
        return
    # player.move(choice)
    
player = Player(room['outside'], 'Ryan')


## Start of the game
show_welcome_message()
display_messages()
user_choice = get_user_choice()


## Game Loop
while user_choice != 'q':
    #take action
    gameActions(user_choice)
    display_messages()
    user_choice = get_user_choice()

## Quit Game
exit()