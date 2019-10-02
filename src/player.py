# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def _init_(self, name, room):
        self.name = name
        self.room = room
    def _repr_(self):
        return f'Name: {self.name}, Currently in : {self.room}'