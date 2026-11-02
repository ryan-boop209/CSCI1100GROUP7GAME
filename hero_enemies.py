from weapons_destruction import nothing, chopsticks, Comically_Large_Spoon, Kantana, Gun, Grem_Weapon, Gob_Weapon, Rat_weapon, Roach_weapon
from random import randint
from health_bar import HealthBar

class Character:
    
    """
    
    
    
    
    
    
    """
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int) -> None:
        self.name = chr_name
        self.n_name = n_name
        self.health = health
        self.max_health = health
        self.damage = damage

        self.is_dodging = False
        self.is_guarding = False

    def attack(self, target) -> None: #scales hero's damage with current equiped weapon
        total_damage = self.damage + self.weapon.damage 
        target.health -=total_damage #how damage works
        target.health = max(target.health, 0)
        target.health_bar.update()
        
        if target.is_dodging:
            total_damage = 0
            print(f"{self.name} successfully dodged")
        
        if target.is_guarding:
            total_damage = int(total_damage * 0.5)
            print(f"{self.name} braced for your attack")

    def reset_health(self) -> None: #Resets health
        self.health = self.max_health
        print(f"Your health has been restored to {self.health}! (I dont wanna make a heal system.)")
        
    def guard(self) -> None: #This blocks most of the incoming damage but not all
       #= (self.damage + self.weapon.damage) * 0.75
        self.is_dodging = False
        self.is_guarding = True
    
    def dodge(self) -> None: 
        import random
        if random.random() > 0.5:
            
            self.is_dodging = True
            self.is_guarding = False
        else: 
            self.is_dodging = False
            self.is_guarding = False

class Protag(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int):
        super().__init__(chr_name, n_name, health, damage)
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped the {self.weapon.name}!")
        self.health_bar = HealthBar(self, color ="green")

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