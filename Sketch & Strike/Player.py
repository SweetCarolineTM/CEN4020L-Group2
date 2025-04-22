import pygame
from Weapons import *

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x,y,width,height)
        self.vel = 3
        self.Weapon = Weapon

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    def check_collision(self, other):
        return self.rect.colliderect(other.rect)
    
    def move(self, other=None):
        keys = pygame.key.get_pressed()
        old_x, old_y = self.x, self.y

        if keys[pygame.K_LEFT] and self.x - self.vel >= 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x + self.vel + self.width <= 800:
            self.x += self.vel

        if keys[pygame.K_UP] and self.y - self.vel >= 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y + self.vel + self.height <= 600:
            self.y += self.vel

        self.update()
        
        if other and self.check_collision(other):
            self.x, self.y = old_x, old_y
            self.update()

    def update(self):
        self.rect.topleft = (self.x, self.y)
        
    def chooseWeapon(self):
        #this function will need to be updated to work with the UI in the game, ideally the player
        #will select a weapon from a list of choices,and that will be their weapon for the turn
        #store the weapons in a dictionary (open to change, example right now)
        bowAndArrow = Weapon("Bow and arrow", 30)
        fireball = Weapon("fireball", 50)
        sword = Weapon("sword", 50)
        weapons = {
            "1": bowAndArrow,
            "2": fireball,
            "3": sword
            }
        #show the choices 
        print("Choose your weapon:") 
        for key, weapon in weapons.items(): 
            print(f"{key} - {weapon.weapon_type}") 
 
        choice = input("Enter the number of your weapon: ") 
 
        # Get weapon choice 
        chosenWeapon = weapons.get(choice) 
 
        if chosenWeapon: 
            print(f"\nYou chose {chosenWeapon.weapon_type}!") 
            self.weapon = chosenWeapon  # Directly equip the weapon 
        else: 
            print("Invalid choice \n")
            
    def turn (self): 
        self.chooseWeapon(self) 
        #move(self) 
        #drawTerrain(self) 
        #useItem(self) 
        #attack(self) 
 
        #update the terrain based on the players attack (if the attack removed some terrain for ex.) 
        #updateTerrain(self) 
        #calculate if a player got hit by an attack 
        #playerDamageCalc(self)