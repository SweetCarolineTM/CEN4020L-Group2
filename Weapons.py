class Weapon:
    def __init__(self, weaponName, damage):
        self.weaponName = weaponName
        self.damage = damage
        #figure out how to implement drawing later
        #self.drawing = drawing

    def displayInfo(self):
        print(f"Weapon Type: {self.weaponName}")
        print(f"Damage: {self.damage}")
        

# Create instances
bowAndArrow = Weapon(
    weaponName="Bow and Arrow",
    damage=30
)

fireball = Weapon(
    weaponName="Fireball",
    damage=50
)

sword = Weapon(
    weaponName="Sword",
    damage=40
)
