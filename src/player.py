# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, currentRoom, name, inventory=[]) :
    self.currentRoom = currentRoom
    self.name = name
    self.inventory = inventory
  
  def move(self, user_input):
    print("You chose:", user_input)
    if user_input == 'north' and self.currentRoom.n_to != None:
      self.currentRoom = self.currentRoom.n_to

    elif user_input == 'south' and self.currentRoom.s_to != None:
      self.currentRoom = self.currentRoom.s_to

    elif user_input == 'east' and self.currentRoom.e_to != None:
      self.currentRoom = self.currentRoom.e_to

    elif user_input == 'west' and self.currentRoom.w_to != None:
      self.currentRoom = self.currentRoom.w_to

    else:
        print('Error message')