#this is an idea for the player class that will be used to calculate
#player attributes (basically the functionality of a player), just
#an idea for now- subject to change

class PlayerAttributes:
    def __init__(self, name: str, x: int, y: int, health: int, weapon: str, item: str):
        
        #could store a user inputted name in the future, could also just be named player1 and player2
        self.name = name
        
        #the player position will be from the Player class code miles already created in Gamefunctions.py
        #right now player_position is just a placeholder until that part gets implemented
        #self.player_position = PlayerPosition(x, y)

        #health for a player
        self.health = health 
        
        #current players weapon, may need to change this to a class type instead of a string based on future
        #implementation of the weapon (for example if we want different weapons to store different value types for damage calculations
        #to terrain and other players)
        self.weapon = weapon 
        
        #any items we may add in the future (for example potions), may be removed, may also need to be changed to a class type
        self.item = item 

    def __str__(self):
        return f"{self.name} - {self.player_position}, Health: {self.health}, Weapon: {self.weapon}, Item: {self.item}"
