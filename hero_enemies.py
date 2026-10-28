from weapons_destruction import nothing, chopsticks, Comically_Large_Spoon, Kantana, Gun, Grem_Weapon, Gob_Weapon, Rat_weapon, Roach_weapon
from random import randint

class Character:
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int) -> None:
        self.name = chr_name
        self.n_name = n_name
        self.health = health
        self.max_health = health
        self.damage = damage

        self.weapon = nothing

    def attack(self, target) -> None: #scales hero's damage with current equiped weapon
        total_damage = self.damage + self.weapon.damage 
        target.health -=total_damage #how damage works
        target.health = max(target.health, 0)

    def reset_health(self) -> None: #Resets health
        self.health = self.max_health
        print(f"Your health has been restored to {self.health}! (I dont wanna make a heal system.)")
        
    def guard(self) -> None: #This blocks most of the incoming damage but not all
       #= (self.damage + self.weapon.damage) * 0.75
        pass
    
    def dodge(self) -> None: #This blocks all damage but a chance you wont.
        #if dodgevalue == n: #N should be a constant updating value if the user chooses. 
                             #N compares to object value
            #total_damage = 0 #Recieves 0 incoming damage
        #else:
            #total_damage = self.damage + self.weapon.damage 
        pass

class Protag(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int):
        super().__init__(chr_name, n_name, health, damage)
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped the {self.weapon.name}!")

class Enemy_1(Character):
    def __init__ (self, chr_name: str, n_name: str, health: int, damage: int, weapon =Gob_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon

class Enemy_2(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int, weapon =Grem_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon

class Enemy_3(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int,weapon =Rat_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon

class Boss(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int, weapon=Roach_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon