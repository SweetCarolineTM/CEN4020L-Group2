class Weapon: 
    def __init__(self, weaponName, damage): 
        self.weaponName = weaponName 
        self.damage = damage #figure out how to implement drawing later 
        #self.drawing = drawing 

    def displayInfo(self): 
        print(f"Weapon Type: {self.weaponName}") 
        print(f"Damage: {self.damage}") 
     
  

#Create instances - add in logic so that different weapon types can be added to the game ex below (needs some changing
# to compile and work)

    #bowAndArrow = Weapon("Bow and arrow", 30)

    #fireball = Weapon( 
    #weaponName="Fireball", 
    #damage=50 
    #)

    #sword = Weapon( 
    #weaponName="Sword", 
    #damage=40 
    #) 