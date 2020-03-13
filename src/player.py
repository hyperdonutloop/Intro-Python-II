# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, currentRoom, name, inventory=[]) :
    self.currentRoom = currentRoom
    self.name = name
    self.inventory = inventory
  
  def move(self, cmd):
    # print("You chose:", cmd)
    if cmd == 'n' and self.currentRoom.n_to != None:
      self.currentRoom = self.currentRoom.n_to

    elif cmd == 's' and self.currentRoom.s_to != None:
      self.currentRoom = self.currentRoom.s_to

    elif cmd == 'e' and self.currentRoom.e_to != None:
      self.currentRoom = self.currentRoom.e_to

    elif cmd == 'w' and self.currentRoom.w_to != None:
      self.currentRoom = self.currentRoom.w_to

    elif cmd == 'i':
      self.display_inventory()

    else:
        print('Error message')
        return
  
  def display_inventory(self):
    if len(self.inventory) <= 0:
      print('\nYou have nothing in your inventory!\n')
    else:
      output = ','.join(map(str, self.inventory))
      print(f"\nYou have: {output}\n")


  def getItem(self, item):
    self.inventory.append(item)

  def dropItem(self, item):
    self.inventory.remove(item)