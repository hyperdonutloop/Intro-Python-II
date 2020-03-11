# Implement a class to hold room information. This should have name and
# description attributes.
# setting values to None so that if there is no attribute given, there won't be an error. If a room doesn't have an exit in one direction, then no error.

class Room:
  def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
    self.name = name
    self.description = description
    self.n_to = n_to
    self.s_to = s_to
    self.e_to = e_to
    self.w_to = w_to
  def __str__(self):
    return f"{self.name}"
