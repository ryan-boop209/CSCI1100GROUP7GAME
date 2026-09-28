from weapons_destruction import nothing, chopsticks, Comically_Large_Spoon, Kantana, Gun, Grem_Weapon, Gob_Weapon, Rat_weapon, Roach_weapon

class Character:
    def __init__(self, chr_name, n_name, health, damage) -> None:
        self.name = chr_name
        self.n_name = n_name
        self.health = health
        self.max_health = health
        self.damage = damage

        self.weapon = nothing

    def attack(self, target) -> None:
        total_damage = self.damage + self.weapon.damage
        target.health -=total_damage
        target.health = max(target.health, 0)

    def reset_health(self) -> None:
        self.health = self.max_health
        print(f"Your health has been restored to {self.health}! (I dont wanna make a heal system.)")

class Protag(Character):
    def __init__(self, chr_name, n_name, health, damage):
        super().__init__(chr_name, n_name, health, damage)
    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped the {self.weapon.name}!")

class Enemy_1(Character):
    def __init__ (self, chr_name, n_name, health, damage, weapon=Gob_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon

class Enemy_2(Character):
    def __init__(self, chr_name, n_name, health, damage, weapon=Grem_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon

class Enemy_3(Character):
    def __init__(self, chr_name, n_name, health, damage, weapon=Rat_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon

class Boss(Character):
    def __init__(self, chr_name, n_name, health, damage, weapon=Roach_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon