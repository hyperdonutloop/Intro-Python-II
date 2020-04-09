from room import Room
from player import Player
from item import Item
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east, and west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'large cave': Room("Large Cave", """You've found a large cave. There is a 
strange fog in the cave. You hear strange sounds. 
Passages run east and south"""),

    'small cave': Room("Small Cave", """You've found a smaller cave. There are 
skeletons and old armor everywhere. The fog is heavy and seems to be emanating 
from somewhere inside this room. In the corner, there is a chest. The only way
out is north""")
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
room['foyer'].w_to = room['large cave']
room['large cave'].s_to = room['small cave']
room['large cave'].e_to = room['foyer']
room['small cave'].n_to = room['large cave']

# treasure chest
treasure_chest = ["silver", "gold", "diamonds", "daedric armor"]

# items in rooms
room['outside'].items = [Item('Sword', '\nYou may need this for what lies ahead\n'), Item('Potion', '100 health')]
room['foyer'].items = [Item('Stamina_Potion', '100 Stamina')]
room['small cave'].items = [Item('Daedric_Armor', 'Very powerful armor')]



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
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome_message():
    # welcome_message = (Fore.LIGHTBLUE_EX + f'\nWelcome to the game: Palace of Winterhold, {player.name}. You are currently in the room: {player.currentRoom}\n' + Style.RESET_ALL + f'this is a test')
    welcome_message = (Back.LIGHTWHITE_EX + Fore.BLACK + f'  Palace of WinterHold  \n' + Style.RESET_ALL + f'\nWelcome to the game, {player.name}. You are in the room ' + Back.LIGHTBLUE_EX + f'{player.currentRoom}\n' + Style.RESET_ALL)
    print(welcome_message)

def display_messages():
    # 
    print(f'{player.currentRoom.description}')
    # print(f"{player.currentRoom.name}")
    player.currentRoom.display_items_list()

def get_user_choice():
    return input('Go explore. Choose: [n]:north, [s]:south, [e]:east, [w]:west, or [q]:quit\n\nTo check items in your inventory choose [i]:inventory\n')

def treasure_choice():
    print_chest()
    print("You see a wooden treasure chest on the left")

    action = input("What do you want to do? > ")

    if action.lower() in ["treasure", "chest", "left"]:
        print("Open it? Press '1'")
        print("Leave it alone. Press '2")
        choice = input(">")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open")
            print('You find some:')

            for treasure in treasure_chest:
                print(treasure)
            
            print("What do you want to do?")

            # get number of items in treasure chest
            items_in_chest = len(treasure_chest)

            print(f"Take all {items_in_chest} treasure, press '1")
            print("Leave it, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == '1':
                print('\tRejoice! You have recieved some treasures and daedric armor.')
                print('\tYou just recieved [{}]'.format(', '.join(treasure_chest)))
            elif treasure_choice == '2':
                print('I hope this treasure will be here later. I may need them.')

def gameActions(input):
    split = input.split(' ')
    print(split)

    if len(split) == 2:
        action = split[0]
        item = split[1].capitalize()

        # print(f'Performing action: {split[0]}')

        if action == action_options[0]: #take
            foundItem = False
            for i in player.currentRoom.items:
                if i.name == item:
                    print(f'\n~~~ Found: {item} in {player.currentRoom} ~~~')
                    player.getItem(i)
                    print(Fore.LIGHTMAGENTA_EX + f'{i.description}' + Style.RESET_ALL)
                    player.currentRoom.removeItem(i)
                    foundItem = True
            if foundItem == False:
                clear()
                print(f'There is no {item} here\n')
        
        elif action == action_options[1]:
            foundItem= False
            for i in player.inventory:
                if i.name == item:
                    player.dropItem(i)
                    player.currentRoom.addItem(i)
                    foundItem == True
            if foundItem == False:
                clear()
                print(f'There is no {item} in your inventory.\n')
        else:
            clear()
            print('Invalid Choice!\n')
                    
    elif len(split) == 1:
        if input in movement_options:
            player.move(input)
        else:
            clear()
            print('Invalid Choice')
    else:
        clear()
        print('Invalid Choice')
        return
    # player.move(choice)
    
player = Player(room['outside'], 'Ryan')



# ascii
def print_chest():
    print()
    print("                      _.--. ")
    print("                  _.-'_:-'|| ")
    print("              _.-'_.-::::'|| ")
    print("         _.-:'_.-::::::'  || ")
    print("       .'`-.-:::::::'     || ")
    print("      /.'`;|:::::::'      ||_ ")
    print("     ||   ||::::::'     _.;._'-._ ")
    print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
    print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
    print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
    print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
    print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
    print("         ||=[ '-._.-+U/.-'    o |'|| ")
    print("         || '-.]=|| |'|      o  |'|| ")
    print("         ||      || |'|        _| '; ")
    print("         ||      || |'|    _.-'_.-' ")
    print("         |'-._   || |'|_.-'_.-' ")
    print("          '-._'-.|| |' `_.-' ")
    print("              '-.||_/.-' ")
    print()

## Start of the game
clear()
show_welcome_message()
display_messages()


## First user choice
user_choice = get_user_choice()

## Game Loop
while user_choice != 'q':
    gameActions(user_choice)
    display_messages()
    user_choice = get_user_choice()

## Quit Game
exit()