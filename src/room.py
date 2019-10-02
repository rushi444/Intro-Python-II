# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
    def __repr__(self):
        return f'Room Name: {self.room_name}, Description: {self.description}'
    def get_directions(self, direction):
        if direction == "n":
            return self.n_to
        if direction == "s":
            return self.s_to
        if direction == "e":
            return self.e_to
        if direction == "w":
            return self.w_to