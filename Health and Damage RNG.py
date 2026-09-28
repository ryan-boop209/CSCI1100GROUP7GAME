from random import randint
from hero_enemies import Protag, Enemy_1, Enemy_2 , Enemy_3, Boss
from weapons_destruction import nothing, chopsticks, Comically_Large_Spoon, Kantana, Gun, Gob_Weapon, Rat_weapon, Roach_weapon, Grem_Weapon



#Health
p_health : int = randint(50,75)
e1_health : int = randint(20,25)
e2_health : int = randint (30,50)
e3_health : int = randint (50,75)
boss_health : int = randint (80,100)

#Weapons for players that will add to the current set damage



#damage 
p_damage_1: int = randint(15,25)
# p_damage_backup_1 : list[float] = [3,5,7,2]
e1_damage: int = randint(1,5)
e2_damage: int = randint(4,8)
e3_damage: int = randint (6,10)
boss_damange : int = randint(10,20)

#test v 



#applying stats

chr_name: str = input("Hello! Please enter your name: ")
n_name: str = input(f"Please give {chr_name} a nickname: ") 

Hero = Protag(chr_name, n_name , health = p_health, damage = p_damage_1)
enemy_1 = Enemy_1("Goblin", "The Green Machine." , health= e1_health, damage = e1_damage, weapon = Gob_Weapon)
enemy_2 = Enemy_2("Gremlin", "The Trash Eater", health= e2_health, damage = e2_damage, weapon = Grem_Weapon)
enemy_3 = Enemy_3("Rat", "Swiss Cheese", health = e3_health, damage= e3_damage, weapon = Rat_weapon)
boss = Boss("Roach", "Juggernaut", health= boss_health, damage= boss_damange, weapon = Roach_weapon)




total_damage = Hero.damage + Hero.weapon.damage
e1_total_damage= enemy_1.damage + enemy_1.weapon.damage
e2_total_damage= enemy_2.damage + enemy_2.weapon.damage
e3_total_damage= enemy_3.damage + enemy_3.weapon.damage
boss_total_damage = boss.damage + boss.weapon.damage
print(f"Your character has {p_health} health!")
print(f"They do {p_damage_1} damage!")

Hero.equip(chopsticks)
input("Get Ready to fight! Press Enter to fight")
input()

# Battle mechanics
while True:
    Hero.attack(enemy_1)
    enemy_1.attack(Hero)

    print(f"You have {Hero.health} Health Remaining!\n {enemy_1.name} has {enemy_1.health} Health Remaining!")
    print(f"You attacked the {enemy_1.name} with {Hero.weapon.name} for {total_damage}!\n {enemy_1.name} has dealed {enemy_1.damage} damage to you with the {enemy_1.weapon.name}!")
    input()
    if enemy_1.health <= 0:
        print(f"You defeated the {enemy_1.name} aka the '{enemy_1.n_name}'")
        break

Hero.reset_health()

#Lore
print("BLAH BLAH BLAH")
input()
print("Blah Blah")
input()
print("Something that tells you got a Comically large spoon")
Hero.equip(Comically_Large_Spoon)



while True:
    Hero.attack(enemy_2)
    enemy_2.attack(Hero)

    print(f"You have {Hero.health} Health Remaining!\n {enemy_2.name} has {enemy_2.health} Health Remaining!")
    print(f"You attacked the {enemy_2.name} with {Hero.weapon.name} for {total_damage}!\n {enemy_2.name} has dealed {enemy_2.damage} damage to you with the {enemy_2.weapon.name}!")
    input()
    if enemy_2.health <= 0:
        print(f"You defeated the {enemy_2.name} aka the '{enemy_2.n_name}'")
        break

Hero.reset_health()

#Lore
print("BLAH BLAH BLAH")
input()
print("Blah Blah")
input()
print("Something that tells you got a Kantana")
Hero.equip(Kantana)



while True:
    Hero.attack(enemy_3)
    enemy_3.attack(Hero)

    print(f"You have {Hero.health} Health Remaining!\n {enemy_3.name} has {enemy_3.health} Health Remaining!")
    print(f"You attacked the {enemy_3.name} with {Hero.weapon.name} for {total_damage}!\n {enemy_3.name} has dealed {enemy_3.damage} damage to you with the {enemy_3.weapon.name}!")
    input()
    if enemy_3.health <= 0:
        print(f"You defeated the {enemy_3.name} aka the '{enemy_3.n_name}'")
        break

Hero.reset_health()

#Lore
print("BLAH BLAH BLAH")
input()
print("Blah Blah")
input()
print("Something that tells you got a Gun?!")
Hero.equip(Gun)



while True:
    Hero.attack(boss)
    boss.attack(Hero)

    print(f"You have {Hero.health} Health Remaining!\n {boss.name} has {boss.health} Health Remaining!")
    print(f"You attacked the {boss.name} with {Hero.weapon.name} for {total_damage}!\n {boss.name} has dealed {boss.damage} damage to you! with the {boss.weapon.name}")
    input()
    if enemy_3.health <= 0:
        print(f"You defeated the {boss.name} aka the '{boss.n_name}'")
        break