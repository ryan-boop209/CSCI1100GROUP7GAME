"""
Dan W
Ryan S
Andre G

"Extermaintors"
Text Adventure
"""

import colorama 
from colorama import Fore, Style, init
colorama.init()
from random import randint
import os
os.system("")


class Weapon:
    """
    This is the general class system for weapons
    Assigning values in the following order below helps automatically keep track of the damage value and the "Random" mulitplier value. Im too lazy to make one.
    The weapons below are examples.
    """
    def __init__(self, name, weapon_type, damage, value) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value
        
    #Weapons

fists = Weapon("Fists", "Short", 4,0)

Knife = Weapon("Knife", "Short", 5, 1)

Baseball_Bat = Weapon("Baseball Bat", "Blunt", 8, 2)

Fly = Weapon("Annoying Buzz", "Magical", 2, 0)

Grem_Weapon = Weapon("Fists", "Blunt", 4, 1)

Gob_Weapon = Weapon("Wooden Baseball bat", "Blunt", 7,2)

Zombie_weapon = Weapon("hands", "Ranged", 4,3)

Orc_weapon= Weapon("Spiked Club", "blunt", 8, 4)

class HealthBar():
    """
    This how we visualize the health bar


    """
    symbol_remaining: str = "♡"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {
            "red": Fore.LIGHTRED_EX,
            "green": Fore.LIGHTGREEN_EX,
            "default": Style.RESET_ALL
        
        }
    
    def __init__(self, entity, length: int = 20, is_colored:bool = True, color:str = "default"):
        """
        

        Args:
            entity (_type_): _description_
            length (int, optional): _description_. Defaults to 20.
            is_colored (bool, optional): _description_. Defaults to True. 
            color (str, optional): _description_. Defaults to "default".
            
        """
        self.entity = entity
        self.length = length
        self.is_colored = is_colored
        self.max_health = entity.max_health
        self.current_value = entity.health
        
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]
    
    def update(self) -> None:
        self.current_value = self.entity.health
    
    def draw(self) -> None:
        """ 
        THIS IS BASICALL HOW THE MATH WORKS TO CALCULATE HOW MUCH HEALTH TO DISPLAY
        I WILL PROBABLY GO INTO DETAILS IM TIRED.
        """
        
        remaining_bars = round(self.current_value / self.max_health * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s Health: {self.entity.health} / {self.entity.max_health}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")


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
        target.health -=total_damage #how damage works
        target.health = max(target.health, 0)
        target.health_bar.update()
        
        
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
        self.health_bar = HealthBar(self, color ="green") #I dont know how to make this neat.

""""
All enemy class is inherited by the character class and they all have a set weapon and the same health bar color.
These are just filler for the weapon =

"""


class Enemy_1(Character):
    def __init__ (self, chr_name: str, n_name: str, health: int, damage: int, weapon =Fly):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color = "red")

class Enemy_2(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int, weapon = Grem_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")

class Enemy_3(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int,weapon = Gob_Weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")
        
class Enemy_4(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int,weapon = Zombie_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")


class Boss(Character):
    def __init__(self, chr_name: str, n_name: str, health: int, damage: int, weapon=Orc_weapon):
        super().__init__(chr_name, n_name, health, damage)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color ="red")

# Yes/No Functions
def check_yes_no(answer: str) -> bool:                                          # Returns True for yes, False for no. Raises ValueError for anything else
    if answer not in ("yes", "no"):                                                                              
        raise ValueError("Answer must be yes or no.")
    return answer == "yes"


def ask_yes_no() -> bool:                                                       # Keeps asking until the player types yes or no
    attempts: int = 0
    while True:
        try:
            return check_yes_no(input())
        except ValueError:
            attempts = attempts + 1
            if attempts == 1:
                print("Please type yes or no.")
            else:
                print("Pretty please? (yes/no) ")


# Heal Function


def heal(health: int, amount: int, max_health: int = 100) -> int:               # Returns health after healing, never going above max_health
    return min(health + amount, max_health)


#Battle Mechanic

def fight_club(hero, enemy) -> None:
    """
    THIS IS HOW THE FIGHTING MECHANICS WORK!!!
    A menu system for players to do attack, guard, and dodge
    If = 1: player attacks
    If = 2: player guards
    If = 3: player dodges (chance-based)
    """
    while hero.health > 0 and enemy.health > 0:
        
        print("\n" + "=" * 40)
        hero.health_bar.draw()
        enemy.health_bar.draw()
        print("=" * 40)
        
        print("Attack [1] \nGuard [2] \nDodge [3]")
        
        valid_turn = False
        while not valid_turn:
            try:
                player_choice = int(input(">>>>>> "))
                
                if player_choice == 1:
                    print(f"{hero.name} attacks {enemy.name}!")
                    hero.attack(enemy)
                    valid_turn = True
                elif player_choice == 2:
                    print(f"{hero.name} chose to brace the incoming attack.")
                    hero.guard()
                    valid_turn = True
                elif player_choice == 3:
                    print(f"{hero.name} chose to gamble their odds.")
                    hero.dodge()  
                    if hero.is_dodging:
                        print(f"{hero.name} became Neo from the matrix!")
                    else:
                        print(f"{hero.name} fell to the ground and got hit, and has back pain.")
                    valid_turn = True
                else:
                    print("Please pick 1, 2, or 3.")
            except ValueError:
                print("Invalid input! Please type a number, not letters or symbols. You goober.")
        
        # Check if enemy is defeated
        if enemy.health <= 0:
            print("You showed them whos boss.")
            break
            
        print(f"\nNow its {enemy.name}'s turn to decide what to do.")
        enemy_action = randint(1, 3)
        
        if enemy_action == 1:
            print(f"{enemy.name} launches an attack!")
            enemy.attack(hero)
        elif enemy_action == 2:
            enemy.guard()
            print(f"{enemy.name} braces and guards against incoming attacks!")
        elif enemy_action == 3:
            enemy.dodge()
            if enemy.is_dodging:
                print(f"{enemy.name} nimbly steps back to dodge!")
            else:
                print(f"{enemy.name} attempts to dodge, but misses the timing!")
                
        # Check if hero is defeated 
        if hero.health <= 0:
            print(f"\n{hero.name} has been defeated... by a bug? HOW? \nYou know what you deserved it.")
            print("====================================")
            print("           GAME OVER")
            print("====================================")
            print("Please try again.")
            exit()
#Health
p_health : int = randint(50,75)
e1_health : int = randint(20,25)
e2_health : int = randint (30,50)
e3_health : int = randint (50,75)
e4_health: int = randint (65,79)
boss_health : int = randint (80,100)

#Weapons for players that will add to the current set damage



#damage 
p_damage_1: int = randint(15,25)
# p_damage_backup_1 : list[float] = [3,5,7,2]
e1_damage: int = randint(1,5)
e2_damage: int = randint(4,8)
e3_damage: int = randint (6,10)
e4_damage: int = randint (9,14)
boss_damange : int = randint(10,20)




enemy_1 = Enemy_1("Bug", "Gross." , health= e1_health, damage = e1_damage, weapon = Fly)
enemy_2 = Enemy_2("Gremlin", "The Trash Eater", health= e2_health, damage = e2_damage, weapon = Grem_Weapon)
enemy_3 = Enemy_3("Goblin", "Green Machine", health = e3_health, damage= e3_damage, weapon = Gob_Weapon)
enemy_4 = Enemy_4("Zombie", "Brain Eater", health = e4_health, damage= e4_damage, weapon = Zombie_weapon)
boss = Boss("Orc", "Juggernaut", health= boss_health, damage= boss_damange, weapon = Orc_weapon)





e1_total_damage= enemy_1.damage + enemy_1.weapon.damage
e2_total_damage= enemy_2.damage + enemy_2.weapon.damage
e3_total_damage= enemy_3.damage + enemy_3.weapon.damage
e4_total_damage = enemy_4.damage + enemy_4.weapon.damage
boss_total_damage = boss.damage + boss.weapon.damage

# Pre-Game Loading Screen where player has inputs
chr_name: str = input("Hello! Please enter your name: ")                        # Give your character a name
print(f"Are you sure {chr_name} is right? (yes/no)")                            # Did you misspell your name?
while not ask_yes_no():                                                         # Loop to make sure your name is correct                                                      
    chr_name = input("Please pick a new name: ")
    print(f"Are you sure {chr_name} is right? (yes/no)")      

# Make sure your name is spelled correctly

n_name:str = "rookie"

Hero = Protag(chr_name,n_name, health = p_health, damage = p_damage_1,)
Hero.equip(fists)
total_damage = Hero.damage + Hero.weapon.damage

print()
print(f"Welcome to the Fantastical Beasts Extermination Team, {chr_name}!")
print()
input("Press ENTER to continue")                                                # Using input() to break up the action for more suspense
print()
print("This is a world with strange beasts and magical creatures.")
print("Throughout history these creatures have dominated humanity.")
print("Ever since the development of new technology and the mastery of magic,")
print("humans have been able to gain the advantage over these creatures")
print("and even contained them to certain regions.")
print("Thus, separating humans and monsters to their own realms.")
input()
print("However, even with this separation, "
    "the two groups could not coexist peacefully.")
print("Monsters have been leaving their habitats to invade human society,")
print("causing chaos and inhabiting our areas as their own.")
print("That's where the FBET comes in.")
print("We are an association that specializes "
    "in dealing with these monster outbreaks.")
input()
print(f"{chr_name}, your role is to kill any beasts "
    "or pests wherever you get assigned to.")
print("Today you will be sent to a house for an extermination job.")
print()
input("Press ENTER to begin your first mission")
print()
print("====================================")
print()
print("         November 7, 2000")
print("              7:02 AM")
print("         Madison, Wisconsin")
print()
print("====================================")
input()
print("You are walking down the sidewalk of a suburban neighborhood.")
print("A few houses still have their Halloween decorations up,")
print("some being an unpleasant reminder of "
    "what you might encounter on your first job.")
input()
print(f"{chr_name}: It's my first mission, they wouldn't make me deal with...")
print("You glance towards one of the houses.")
print("A giant inflatable killer clown looms over the yard,")
print("a lion-sized spider hangs from a tree, "
    "and a horde of skeletons crowds the front porch.")
input()
print("*Gulp.*")
input()
print("You take a few deep breaths and manage "
    "to calm yourself, but as you look forward")
print("you spot a house with no props or decorations.")
print("The lawn is neatly trimmed. The windows "
    "are spotless. The porch is perfectly clean,")
print("but one detail sticks out: "
    "the front door is painted an unsettling, deep red.")
print("1313 is the house number. The house you were assigned to.")
print("You take a slow, deep breath and reach for your communicator.")
input()
print(f"{chr_name}: Reporting to FBET Headquarters. I'm going in.")
input()
print("FBET Agent: Copy that. Stay alert. We'll monitor your signal.")
input()
print("CLICK.")
print()
print("From the entryway everything seems normal, peaceful even,")
print("but the moment you step in fully-")
input()
print("SLAM.")
print("A muffled \"Keh-heh-heh!\"")
print("\"Buzzz. Buzzz.\"")
print("And a deep, reverberating laugh from below can be heard all at once.")
input()
print("You try for the door, but it won't open "
    "or budge no matter how much you try.")
print("Even the window seems to be unbreakable.")
print("You check your communicator, but it has no signal.")
print("And your weapons, they've just vanished...")
input()
print("With one self-inflicted slap to the face, "
    "you remember the months of training and preparations")
print("you've gone through, especially for rare situations like this.")
print("\"Assess. Adapt. Act.\" You mentally repeat the motto "
    "your instructor drilled into your head.")
print("You crack your knuckles..")
print(f"{chr_name}: Hey monsters, haven't any "
      "of you looked at a calendar? Halloween is over.")
print()
input("Press ENTER to begin gameplay")
print()
print("From the entryway, there is a kitchen on "
    "your left and a dining room to your right.")
print()


choice: str = str(input("Where do you want to go?"
                        "\n1. Kitchen\n2. Dining Room\n"))          # Variable for where you want to go
while choice != "1":                # Loops if you don't go to the kitchen
   
    if choice == "2":               # Determines whether or not you went to the dining room
        print()
        print("You take a right and enter the dining room and spot a gremlin chewing on a candle.")
        print("You freeze. You're completely empty-handed.")
        input()
        print("The gremlin spits out the candlestick right onto your face,")
        print("leaving a large gloop of saliva dripping down your cheek.")
        print("It continues gnawing at the candle, disinterested in your presence.")
        print("You wipe the saliva off your face and notice the tough skin of the gremlin")
        print("and slowly back away into the entryway.")
        input()
        print(f"{chr_name}: Bare hands won't hurt it. I need something sharp.")
        print(f"{chr_name}: Something like a knife. Where could I find a knife...")
        input()                                                                     # Using input() to break up the action for more suspense
   
    choice: str = str(input("Where do you want to go? \n1. Kitchen\n2. Dining Room\n"))


print()
print("You enter the kitchen and it's oddly clean and normal,")
print("but then you look up.")
input()
print("An insect the size of a dog clings to the ceiling, rubbing its")
print("front legs together like a diner ready to eat.")
print("As if the monster couldn't get any more terrifying, it reveals that it has wings with a sudden flutter.")
input()                                                                         # Using input() to break up the action for more suspense

fight_club(Hero, enemy_1) #Goes to the def fight_club)



print()
print("        ~     ~")
print("         ~   ~")
print("       .-------.")
print("       | X   X |")
print("       |  ___  |")
print("  ~~~~ '-------' ~~~~")
print("  ~~~~ (=======) ~~~~")
print("   ~~  ( ||||| )  ~~")
print("      (_)(_)(_)(_)")
input()
print("You killed the insect and spot a knife on the counter behind its body.")  # knife increases attack damage by about x1.5
print("You reach past the insect corpse, take the knife, and store it snugly in your pocket.")
input()
Hero.equip(Knife)
print("*Knife equipped*")
input()                                                                         # Using input() to break up the action for more suspense


choice: str = input("The kitchen is now safe.\nWhich area do you want to enter? \n1. Sitting Room\n2. Dining Room\n") # Gives player a choice where to go
while choice != "2":                # Loops if you don't go to the kitchen
   
    if choice == "1":               # Determines whether or not you went to the dining room
        print()
        print("You entered the sitting room.")
        print("The sitting room is quiet. Dusty armchairs, a cold fireplace,")
        print("and shelves lined with tiny porcelain teacups.")
        input()
        print("A chittering laugh echoes from above.")
        print("A goblin is perched on the mantel, a teacup in each hand.")
        input()
        print("It throws one. You duck, and it explodes against the wall.")
        print("It throws another. This one cracks right off your skull.")
        input()
        print("The room spins. Another teacup whistles past your ear.")
        print("You stagger back into the kitchen as china shatters on the doorframe.")
        input()
        print(f"{chr_name}: Ow... my head. I need something to cover it.")
        input()                                                                     # Using input() to break up the action for more suspense
   
    choice: str = str(input("Where do you want to go?\n1. Sitting Room\n2. Dining Room\n"))


print("You enter the dining room and see a gremlin shaped like")
print("a slice of toast on a table gnawing on a candle.")
print("The gremlin notices the sharp edge of the knife you pull out your pocket.")
print("and scrambles back from the table, hissing.")
print("You spot it as it raises an arm: under it, the thick hide thins")
print("to bare, pale skin.")
input()                                                                         # Using input() to break up the action for more suspense
fight_club(Hero, enemy_2)





print()
print("        .---------.")
print("      .'  =======  '.")
print("     (_______________)")
print("   <  (  X       X  )  >")
print("      |      v      |")
print("      | VVVVVVVVVVV |")
print("       (___________)")
print("         |_|   |_|")
input()
print("You kill the gremlin and crouch beside it. You notice a shiny metal helmet")
print("strapped to its head.")
input()
print("   .-------------.")
print("  (   X       X   )")
print("  |       v       |")
print("  |  VVVVVVVVVVV  |")
print("   (_____________)")
print("      |_|   |_|")
input()
print("*Protective helmet equipped*")                                          # Protective helmet increases your dodge
input()                                                                         # Using input() to break up the action for more suspense


choice: str = input("The dining room is now safe.\nWhich area do you want to enter? \n1. Kitchen\n2. Living Room\n") # Gives player a choice where to go
while choice != "1":                # Loops if you don't go to the kitchen
   
    if choice == "2":               # Determines whether or not you went to the dining room
        print("You entered the living room.")
        print()
        print("The room is dark, lit only by the static screen of a TV.")
        print("In front of the TV is a zombie, attracted by the sharp crackle of the static")
        input()
        print("You slowly step forward and the floorboard groans loudly, catching the undead's attention.")
        print("It rises and shambles across the room, arms outstretched.")
        print("You raise the knife and aim for its chest.")
        input()
        print("SQUELCH")
        input()
        print("The blade sinks in. The zombie doesn't even slow down.")
        print("It grabs your arm with both hands, and its jaws snap")
        print("an inch from your skin.")
        input()
        print("You wrench free and tumble back into the dining room.")
        print("The zombie stands in the doorway for a moment, then")
        print("shuffles back to the TV and goes on to scratch at its screen.")
        input()
        print(f"{chr_name}: Stabbing it did nothing. And it went straight for my flesh...")
        print(f"{chr_name}: I need something to protect myself before I try that again.")
        print()
        input("...")                                                                     # Using input() to break up the action for more suspense
        print()
   
    choice: str = str(input("Where do you want to go?\n1. Kitchen\n2. Living Room\n"))


print("You are safe in the kitchen.")
input()
print("You see a slice of red velvet cake on the counter.")
print("Do you want to eat the cake? (yes/no)")


if ask_yes_no():
    p_health = heal(p_health, 15)
    print()
    print(f"Your health is restored to {p_health}")
else:
    print("You put the slice of cake back down and it magically disappears...")


choice: str = input("Which area do you want to enter?\n1. Dining Room\n2. Sitting Room\n") # Gives player a choice where to go
while choice != "2":                # Loops if you don't go to the kitchen
   
    if choice == "1":               # Determines whether or not you went to the dining room
        print("You are safe in the dining room.")
        choice: str = input("Which area do you want to enter?\n1. Kitchen\n2. Living Room\n") # Gives player a choice where to go
   
        while choice != "1":
   
            if choice == "2":
                print("You entered the living room.")
                input()                                                                 # Using input() to break up the action for more suspense
                print("The room is dark, lit only by the static screen of a TV.")
                print("In front of the TV is a zombie, attracted by the sharp crackle of the static")
                input()
                print("You slow step forward and the floorboard groans loudly, catching the undead's attention.")
                print("It rises and shambles across the room, arms outstretched.")
                print("You raise the knife and aim for its chest.")
                print()
                print("SQUELCH")
                input()
                print("The blade sinks in. The zombie doesn't even slow down.")
                print("It grabs your arm with both hands, and its jaws snap")
                print("an inch from your skin.")
                input()
                print("You wrench free and tumble back into the dining room.")
                print("The zombie stands in the doorway for a moment, then")
                print("shuffles back to the screen and goes on to scratch at the screen.")
                input()
                print(f"{chr_name}: Stabbing it did nothing. And it went straight for my flesh...")
                print(f"{chr_name}: I need something to protect myself before I try that again.")
                print()
                input("...")                                                                     # Using input() to break up the action for more suspense
                # choice: str = input("Which area do you want to enter?\n1. Kitchen\n2. Living Room") # Gives player a choice where to go
   
            print("You are safe in the dining room.")
            choice: str = input("Which area do you want to enter?\n1. Kitchen\n2. Living Room\n") # Gives player a choice where to go
   
    print("You are safely in the kitchen.")
    choice: str = str(input("Which area do you want to enter?\n1. Dining Room\n2. Sitting Room\n"))


print("You enter the sitting room.")
input()
print("It's quiet. Dusty armchairs, a cold fireplace,")
print("and shelves lined with tiny porcelain teacups.")
input()
print("A chittering laugh echoes from above.")
print("A goblin is perched on the mantel, wearing shiny armor that looks exactly your size...")
input()
print("The goblin wields a teacup in each hand.")
print("It throws one. It bounces off your helmet with a CLANG.")
print("Another throw, another CLANG.")
input()
print("The goblin's grin slips as it reaches for the shelf and finds it empty.")
input()
print(f"{chr_name}: Out of ammo?")
input()                                                                         # Using input() to break up the action for more suspense


fight_club(Hero, enemy_3)



print()
print("      .-------.")
print(" <===|  X   X  |===>")
print("     |    >    |")
print("     |  _____  |")
print("     | |^^^^^| |")
print("      (_______)")
print("        |   |")
input()
print("You killed the goblin, and steal the shiny armor right off its corpse.")  
input()  
print("*Protective armor equipped*")                                            # Protective armor has several benefits
input()                                                                         # Using input() to break up the action for more suspense


choice: str = input("The sitting room is now safe. Which area do you want to enter?\n1. Kitchen\n2. Living Room\n") # Gives player a choice where to go
while choice != "2":
   
    if choice == "1":
        print("You are safe in the kitchen.")
        choice: str = input("Which area do you want to enter?\n1. Dining Room\n2. Sitting Room\n")
       
        while choice not in ("1","2"):
            print("You are safe in the kitchen.")
            choice: str = input("Which area do you want to enter?\n1. Dining Room\n2. Sitting Room\n")
       
        if choice == "1":
            print("You are in the dining room.")
        else:
            print("You are in the sitting room.")
   
    choice: str = input("Which area do you want to enter?\n1. Kitchen\n2. Living Room\n")


print("You enter the living room.")
print("A zombie is at the TV screen, swaying in time with the static,")
print("nails dragging down the glass.")
print()
print("Screeeeech.")
input()
print("You step forward, and a floorboard groans under your boot.")
print("The scratching stops.")
print("Slowly, the zombie peels itself off the glass and turns toward you.")
input()
print("It lunges, and its jaws clamp down on your protected arm with a loud CLANG.")
print("Its teeth skid off the metal.")
input()
print("The zombie reels back, dazed, and you tighten your grip on the knife.")
input()                                                                         # Using input() to break up the action for more suspense


fight_club(Hero, enemy_4)                                  


print()
print("         .-------.")
print("       /  ~ ~ ~ ~  \\")
print("      |  X       X  |")
print("      |      ^      |")
print("      |   _______   |")
print("      |  |VVVVVVV|  |")
print("       \\  \\_____/  /")
print("        \\_________/")
print("          |     |")
input()
print("Your final strike hits the zombie dead center. Its mouth opens wide,")
print("there's a deep THOOM, and a baseball bat rockets out of its throat")
print("and slams into the wall beside your head.")
print()
print("You don't question it and pull the bat from the wall and stuff it")
print("into your pocket, somehow.")
input()
Hero.equip(Baseball_Bat)
print("*Baseball bat equipped*")
input()
print("The zombie also dropped a bottle of liquid that has a smiley face on it.")
print("There's no way that can be bad, right?")
print("You chug the whole bottle.  It tastes nasty, but you feel refreshed.")
p_health = 100
print(f"Your health is restored to {p_health}")
input()                                                                         # Using input() to break up the action for more suspense
print("A stairway magically appears leading to the basement.")                  # No more free roaming.  No choice, you have to go to the basement
print("You hurry down the stairs.")
input()                                                                         # Using input() to break up the action for more suspense
print("Before you stands a fierce orc.  He watches as you descend the stairs.")
print("You glance at the knife, then at the orc, then back at the knife.")
print("\"Assess. Adapt. Act.\"")
input()
print("Assess: the knife is bent and the orc is huge.")
print("Adapt: you slide the knife back into your pocket.")
print("Act: you pull out the bat.")
input()
print("However the orc isn't intimidated at all and roars.")
print("The bulb shatters, dust rains from the ceiling,")
print("and every bone in your body tells you to run.")
input()
print("You don't.")
print("You slide your back foot out, bend your knees, and drop your shoulders.")
print("You wrap both hands around the bat and raise it over your shoulder.")
input()
print("Your eyes lock onto the orc. Your breathing slows.")
print("You've done this before. Sort of. In Little League.")
input()
print(f"{chr_name}: Son of a pitch...")
print()


fight_club(Hero, boss)                                    # Should end the game prematurely


input()
print("The orc falls and the key drops onto the floor.")
print("You pick it up and it feels... magical.")
input()
print("*Key equipped*")
input()
print("You remember the front door, still sealed by magic.")
print("You climb the stairs and walk to the front door")
print("that has a keyhole from the inside for some reason.")
input()
print("You rummage past the kitchen knife and baseball bat in your pocket to pull out the key.")
input()
print("CLICK.")
input()
print("The door slowly swings open.")
print("Fresh air rushes past you.")
print("After everything you encountered inside,")
print("the outside world feels almost unreal.")
input()
print(f"{chr_name}: Finally... I'm out.")
input()
print("Your communicator suddenly crackles to life.")
input()
print(f"FBET Headquarters: Agent {chr_name}, do you copy?")
input()
print(f"{chr_name}: Loud and clear.")
input()
print(f"FBET Headquarters: Report.")
input()
print(f"{chr_name}: The extermination is complete.")
print(f"{chr_name}: All hostile creatures have been dealt with.")
input()
print(f"FBET Headquarters: Understood.")
print(f"FBET Headquarters: Good work, {chr_name}.")
input()
print("You turn away from the house and begin walking.")
input()
print(f"FBET Headquarters: Get back here safely.")
print("We have another assignment waiting for you.")
input()
print(f"{chr_name}: Another one already?")
input()
print("You sigh.")
print()
print("Apparently, being an exterminator isn't going to be")
print("as easy as you thought.")
print("You disappear into the distance,")
print("leaving the mysterious house behind.")
input()
print("====================================")
print("           GAME COMPLETE")
print("====================================")
print()
print(f"Thank you for playing, {chr_name}!")



