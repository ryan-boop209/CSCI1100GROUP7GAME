class Weapon:
    def __init__(self, name, weapon_type, damage, value) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

nothing = Weapon("Nothing", "Nothing", 0 ,0)

chopsticks = Weapon("Chopsticks", "Blunt", 2, 0)

Comically_Large_Spoon = Weapon("Comically Large Spoon", "Ranged", 4, 1)

Kantana= Weapon("Kantana", "Magical", 5, 2)

Gun = Weapon("Gun.", "Overpowered", 10, 3)

Gob_Weapon = Weapon("Fists", "Blunt", 1, 0)

Grem_Weapon = Weapon("Spiked Club", "Blunt", 3,1)

Rat_weapon = Weapon("Cheese Stick", "Ranged", 4,2)

Roach_weapon= Weapon("Infection", "Magical", 5, 3)
