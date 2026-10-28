"""
    project1.py
    Daniel Waughtel
    Ryan
    Andre


    A text adventure
"""


import colorama 
colorama.init()
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




#applying stats




enemy_1 = Enemy_1("Goblin", "The Green Machine." , health= e1_health, damage = e1_damage, weapon = Gob_Weapon)
enemy_2 = Enemy_2("Gremlin", "The Trash Eater", health= e2_health, damage = e2_damage, weapon = Grem_Weapon)

e1_total_damage= enemy_1.damage + enemy_1.weapon.damage
e2_total_damage= enemy_2.damage + enemy_2.weapon.damage


# #Pre-Game Loading Screen where player has inputs
chr_name: str = input("Hello! Please enter your name: ")      # Give your character a name
pre_q_name: str = input(f"Are you sure {chr_name} is right? (yes/no) ")    # Did you misspell your name?
while pre_q_name == "no":
    chr_name: str = input("Please pick a new name: ")
    pre_q_name: str = input(f"Are you sure {chr_name} is right? (yes/no) ")




n_name: str = input(f"Please give {chr_name} a nickname: ")     # Give yourself a nickname
pre_q_name: str = input(f"Are you sure {n_name} is correct? (yes/no) ") # Did you misspell the nickname?
while pre_q_name == "no":
    n_name: str = input("Please pick a new nickname: ")
    pre_q_name: str = input(f"Are you sure {n_name} is right? (yes/no) ")




agency: str = input(f"What agency does {n_name} aka {chr_name} works for? ")
pre_q_name: str = input(f"Are you sure {agency} is correct? (yes/no) ")
while pre_q_name == "no":
    agency: str = input("Please pick a new agency name: ")
    pre_q_name: str = input(f"Are you sure {agency} is right? (yes/no) ")

Hero = Protag(chr_name, n_name , health = p_health, damage = p_damage_1)
total_damage = Hero.damage + Hero.weapon.damage

print(f"Your character has {p_health} health!")
print(f"They do {p_damage_1} damage!")







# Start of game, intro to the story/lore


input()
print(f"Welcome to the Fantastical Beasts Extermination Team, {chr_name}!")
input()
print("This is a world with strange beasts and magical creatures.")
print("Throughout history these creatures have dominated humanity.")
print("Ever since the development of new technology and the mastery of magic,")
print("humans have been able to gain the advantage over these creatures and even contained them to certain regions.")
print("Thus, separating humans and monsters to their own realms.")
input()
print("However, even with this separation, the two groups could not coexist peacefully.")
print("Monsters have been leaving their habitats to invade human society,")
print("causing chaos and inhabiting our areas as their own.")
print("That's where the F.B.E.T. comes in.")
print("We are an association that specializes in dealing with these monster outbreaks.")
input()
print(f"{chr_name}, your role is to kill any beasts or pests wherever you get assigned to. Today you will be sent to a house for an extermination job.")

###### Boom main Game
input()

print("      November 7, 2000")
print("           7:02 AM")
print("      Madison, Wisconsin")
input()
print("You are walking down the sidewalk of a suburban neighborhood.")
print("A few houses still have their halloween decorations up,")
print("an unpleasant reminder of what you'll be encountering for your first job.")
input()
print(f"{chr_name}: It's my first mission, they wouldn't make me deal with...")
print("You glance towards one of the houses.")
print("A giant inflatable killer clown looms over the yard,")
print("a lion-sized spider hangs from a tree, and a horde of skeletons crowds the front porch.")
input()
print("*Gulp.*")
input()
print("You take a few deep breaths and manage to calm yourself, but as you look forward")
print("you spot a house with no props or decorations.")
print("The lawn is neatly trimmed. The windows are spotless. The porch is perfectly clean,")
print("but one detail sticks out: the front door is painted an unsettling, deep red.")
print("1313 is the house number. This is the one.")
print("You take a slow breath and reach for your communicator.")
input()
print(f"{chr_name}: Reporting to {agency} Headquarters. I'm going in.")
print()
print(f"{agency} Headquarters: Copy that. Stay alert. We'll monitor your signal.")
input()
print("CLICK.")

print("From the entryway everything seems normal, peaceful even,")
print("but the moment you step in fully-")
input()
print("SLAM.")
print("A muffled \"Keh-heh-heh!\"")
print("\"Buzzz. Buzzz.\"")
print("And a deep, reverberating laugh from below can be heard all at once.")
input()
print("You try for the door, but it wont open nor budge no matter how much you try. Even the window seems to be unbreakable.")
print("You check your communicator, but it has no signal.")
print("And your weapons, they've just vanished...")
input()
print("With one self-inflicted slap to the face, you remember the months of training and preparations")
print("you've gone through, especially for rare situations like this.")
print("\"Assess. Adapt. Act.\" The motto you've been taught repeats in your head.")
input()
print("From the entryway, there is a kitchen on your left,")
print("and a dining room to your right.")
print("You crack your knuckles and give the floor a solid stomp.")
input()
print(f"{chr_name}: Hey monsters, haven't any of you looked at a calendar? Halloween is over.")
print()
input("Press ENTER")
print()


print("You are standing in the entryway of a small house.")
print("From the entryway, there is a kitchen on your left,")
print("and a dining room to your right.")


choice: str = input("Do you want to go to the kitchen or to the dining room? ") # Gives player a choice where to go
while not choice == "kitchen": # Loop if you go the wrong way
    print("You entered the dining room.")
    input() # Using input() to break up the action for more suspense
    print("A gremlin starts running at you, and you run back to the entryway.")
    input() # Using input() to break up the action for more suspense
    choice: str = input("Do you want to go to the kitchen or to the dining room? ") # Gives player a choice where to go


print("You enter the kitchen to find a goblin the size of a dog drinking a cup of coffee.")
print("You found Chopsticks lying on the ground.")
input() # Using input() to break up the action for more suspense


#GAME START!
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


print("You killed the goblin with chopsticks (somehow), and found a comically large spoon?.")
Hero.equip(Comically_Large_Spoon)
input() # Using input() to break up the action for more suspense


choice: str = input("Now that the kitchen is safe, do you want to go to the dining room or to the sitting room? ") # Gives player a choice where to go
while choice == "sitting room": # Loop if you go the wrong way
    print("You entered the sitting room.")
    input() # Using input() to break up the action for more suspense
    print("A big Rat attacks, and you run back to the kitchen.")
    input() # Using input() to break up the action for more suspense
    choice: str = input("Do you want to go to the dining room or to the sitting room? ") # Gives player a choice where to go


print("You enter the dining room.")
print("This time you have your trusty comically large spoon. You charged towards the Gremlin without hesitation")
input() # Using input() to break up the action for more suspense

input("Get Ready to fight! Press Enter to fight")

# Combat gets entered here
#GAME START
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

print("You killed the gremlin, and now have a protective helmet.")



# Combat gets entered here

input()



##future update aka cliffhanger##



########### Conclusion


input()
print("You walk to the front door.")
print("You rummage past the comically large spoon and the goblin arm in your pocket to pull out the key.") # change items in pocket
input()
print("CLICK.")
input()
print("The door slowly swings open.")
print("Fresh air rushes past you.")
print("After everything you encountered inside,")
print("the outside world feels almost unreal.")
input()
print(f"{chr_name}: Finally... I'm out.")
print()
print("Your communicator suddenly crackles to life.")
input()
print(f"{agency} Headquarters: Agent {chr_name}, do you copy?")
print(f"{chr_name}: Loud and clear.")
print(f"{agency} Headquarters: Report.")
print(f"{chr_name}: The extermination is complete.")
print("All hostile creatures have been dealt with.")
print(f"{agency} Headquarters: Understood.")
print(f"{agency} Headquarters: Good work, {n_name}.")
input()
print("You turn away from the house and begin walking.")
print()
print(f"{agency} Headquarters: Get back here safely.")
print("We have another assignment waiting for you.")
print(f"{chr_name}: Another one already?")
input()
print("You sigh.")
print("Apparently, being an exterminator isn't going to be")
print("as easy as you thought.")
print("You disappear into the distance,")
print("leaving the mysterious house behind.")
input()
print("====================================")
print("           GAME COMPLETE")
print("====================================")
input()
print(f"Thank you for playing, {chr_name}!")
print("There will be more cool things in the future such as a health bar! - Ryan S. I procrastinated.")
None()
