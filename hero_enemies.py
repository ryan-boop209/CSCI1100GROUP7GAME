"""
Hero_enemies.py
Ryan S

Class system for the characters to interact with the game



"""



from weapons_destruction import nothing, chopsticks, Comically_Large_Spoon, Kantana, Gun, Grem_Weapon, Gob_Weapon, Rat_weapon, Roach_weapon
from random import randint
from health_bar import HealthBar

class Character:

    """
Using this class allows us to help auto set health, damage, and etc without having to make life diffcult




    """
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int) -> None:


        """
        chr: name = The name of the character
        n_name: The nick name of the character
        health = the health value assigned to the object which updates
        max_health = the max value health assigned to the object (doesnt update)
        damage= the base damage value of object

        dodging = false due to user input needing to confirm
        guarding= ^
        """
        self.name = chr_name
        self.n_name = n_name
        self.health = health
        self.max_health = health
        self.damage = damage

        self.is_dodging: bool = False
        self.is_guarding: bool = False

    def attack(self, target) -> None: #scales hero's damage with current equiped weapon

        """
        total damage = takes base object value with current wielded weapon attack value
        target.health = subtracts objects health with total damage
        update = making sure that the health value is updated until 0


        """
        total_damage = self.damage + self.weapon.damage 
        target.health -=total_damage #how damage works
        target.health = max(target.health, 0)
        target.health_bar.update()
        
        if target.is_dodging:
            total_damage = 0
            print(f"{self.name} successfully dodged")

        """
        if target is dodging: true  = if object dodges it can negate all damage
        """

        
        if target.is_guarding:
            total_damage = int(total_damage * 0.5)
            print(f"{self.name} braced for your attack")

        """
        target is dodging : true = half of the damage is inflicted
        """

    def reset_health(self) -> None: #Resets health
        self.health = self.max_health
        print(f"Your health has been restored to {self.health}! (I dont wanna make a heal system.)")
        
    def guard(self) -> None: #This blocks most of the incoming damage but not all
       #= (self.damage + self.weapon.damage) * 0.75
        self.is_dodging = False
        self.is_guarding = True
        """
        On and off system. Cant have both be true

        """
    
    def dodge(self) -> None: 

        """
        
        To make dodging not as op. A random value is set and if greater than 0.5 the dodge is successful. If not you take all damage
        """
        import random
        if random.random() > 0.5:
            
            self.is_dodging = True
            self.is_guarding = False
        else: 
            self.is_dodging = False
            self.is_guarding = False

class Protag(Character):

    """
    inhertience of the class and this will be used for the main protag which is given by the user
    """
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int):
        super().__init__(chr_name, n_name, health, damage)
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped the {self.weapon.name}!") 
        self.health_bar = HealthBar(self, color ="green") #I dont know how to make this neat.

""""
All enemy class is inherited by the character class and they all have a set weapon and the same health bar color.
These are just filler for the weapon =

"""


class Enemy_1(Character):
    def __init__ (self, chr_name: str, n_name: str, health: int, damage: int, weapon =Gob_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color = "red")

class Enemy_2(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int, weapon =Grem_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")

class Enemy_3(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int,weapon =Rat_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")

class Boss(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int, weapon=Roach_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")