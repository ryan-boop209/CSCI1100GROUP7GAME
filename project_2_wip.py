"""
    project1.py
    Daniel Waughtel
    Ryan Saysongkham
    Andre Garcia


    A Text Adventure
"""
# Health - declaring initial health values
p_health: int = 100
e1_health: int = 20
e2_health: int = 40
e3_health: int = 60
e4_health: int = 80
boss_health: int = 100


# Dodge - declaring variables to make it easier to remember
p_dodge: int
e1_dodge: int
e2_dodge: int
e3_dodge: int
e4_dodge: int
boss_dodge: int


# Damage - declaring variables to make it easier to remember
p_damage: int
e1_damage: int
e2_damage: int
e3_damage: int
e4_damage: int
boss_damage: int


from random import randint


# Yes/No Functions
def check_yes_no(answer: str) -> bool:                                           # Returns True for yes, False for no. Raises ValueError for anything else
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


# Pre-Game Loading Screen where player has inputs
chr_name: str = input("Hello! Please enter your name: ")                        # Give your character a name
print(f"Are you sure {chr_name} is right? (yes/no)")                            # Did you misspell your name?
while not ask_yes_no():                                                         # Loop to make sure your name is correct                                                      
    chr_name = input("Please pick a new name: ")
    print(f"Are you sure {chr_name} is right? (yes/no)")                        # Make sure your name is spelled correctly


print()
print(f"Welcome to the Fantastical Beasts Extermination Team, {chr_name}!")
print()
input("Press ENTER to continue")
print()
print("This is a world with strange beasts and magical creatures.")
print("Throughout history these creatures have dominated humanity.")
print("Ever since the development of new technology and the mastery of magic,")
print("humans have been able to gain the advantage over these creatures")
print("and even contained them to certain regions.")
print("Thus, separating humans and monsters to their own realms.")
input()
print("However, even with this separation, the two groups could not coexist peacefully.")
print("Monsters have been leaving their habitats to invade human society,")
print("causing chaos and inhabiting our areas as their own.")
print("That's where the FBET comes in.")
print("We are an association that specializes in dealing with these monster outbreaks.")
input()
print(f"{chr_name}, your role is to kill any beasts or pests wherever you get assigned to.")
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
print("some being an unpleasant reminder of what you might encounter on your first job.")
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
print("You try for the door, but it won't open or budge no matter how much you try.")
print("Even the window seems to be unbreakable.")
print("You check your communicator, but it has no signal.")
print("And your weapons, they've just vanished...")
input()
print("With one self-inflicted slap to the face, you remember the months of training and preparations")
print("you've gone through, especially for rare situations like this.")
print("\"Assess. Adapt. Act.\" You mentally repeat the motto your instructor drilled into your head.")
print("You crack your knuckles..")
print(f"{chr_name}: Hey monsters, haven't any of you looked at a calendar? Halloween is over.")
print()
input("Press ENTER to begin gameplay")
print()
print("From the entryway, there is a kitchen on your left and a dining room to your right.")
print()


choice: str = input("Which area do you want to enter? (kitchen/dining room) ") # Gives player a choice where to go
while choice == "dining room":                                                 # Loop if you go the wrong way
    print()
    print("You take a right and enter the dining room and spot a gremlin chewing on a candle.")
    print("You freeze. You're completely empty-handed.")
    input()
    print("The gremlin spits out the candlestick right onto your face,")
    print("leaving a large gloop of saliva dripping down your cheek.")
    print("It continues gnawing at the candle, disinterested in your presence.")
    print("You wipe the saliva off your face and notice the tough skin of the gremlin")
    print("and slowly back away into the hallway.")
    input()
    print(f"{chr_name}: Bare hands won't hurt it. I need something sharp.")
    print(f"{chr_name}: Something like a knife. Where could I find a knife...")
    input()                                                                     # Using input() to break up the action for more suspense
    choice: str = input("Which area do you want to enter? (kitchen/dining room) ") # Gives player a choice where to go


print()
print("You enter the kitchen and it's oddly clean and normal,")
print("but then you look up.")
input()
print("An insect the size of a dog clings to the ceiling, rubbing its")
print("front legs together like a diner ready to eat.")
print("As if the monster couldn't get any more terrifying, it reveals that it has wings with a sudden flutter.")
input()                                                                         # Using input() to break up the action for more suspense




while e1_health > 0 and p_health > 0:
    choice: str = input("Do you want to attack or dodge? (attack/dodge) ")                     # Choice of whether to attack or dodge
   
    if choice == "attack":                                                      # You chose to attack
        print("You attack!")
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 8:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The insect attacks!")
            p_damage = randint(5,15)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e1_damage = randint(5,8)                                            # The enemy attack damage range
            print(f"The insect attacks with {e1_damage} damage points.")
   
            if p_damage >= e1_damage:                                           # If your attack is greater than the enemy's, your attack wins
                e1_health = e1_health - p_damage                                # The enemy loses HP
                print(f"The insect has {e1_health} health points.")
   
            elif p_damage < e1_damage:                                          # If your attack is less than the enemy's, the enemy wins
                p_health = p_health - e1_damage                                 # You lose HP
                print(f"You have {p_health} health points.")
   
        elif e_choice < 8:                                                      # If enemy RNG is low enough, the enemy dodges
            print("The insect dodges!")
            p_damage = randint(5,15)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e1_dodge = randint(10,20)                                           # The enemy dodge range
            print(f"The insect has {e1_dodge} dodge points.")
   
            if p_damage >= e1_dodge:                                            # If your attack is >= enemy's dodge, you win
                e1_health = e1_health - (p_damage // 2)                           # Enemy loses health equal to the floor of half of your damage points
                print(f"The insect has {e1_health} health points.")
   
            elif p_damage < e1_dodge:
                print("The insect successfully dodged your attack.")
   
    elif choice == "dodge":                                                     # You chose to dodge
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
        print(e_choice)
   
        if e_choice >= 2:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The insect attacks!")
            p_dodge = randint(5,15)                                             # Your dodge point range
            print(f"You have {p_dodge} dodge points.")
            e1_damage = randint(5,8)                                            # The enemy attack damage range
            print(f"The insect attacks with {e1_damage} damage points.")
   
            if p_dodge >= e1_damage:                                            # If your dodge points >= enemy attack, you dodge without taking damage
                print("You dodged the attack.")
   
            elif p_dodge < e1_damage:                                           # If your dodge points < enemy attack, you dodge but take damage
                p_health = p_health - (e1_damage // 2)                            # You take the floor or half enemy damage
                print(f"You now have {p_health} health points.")
   
        elif e_choice < 2:                                                      # If enemy RNG is low enough, the enemy dodges
            print("You and the insect both dodged.")
            print("You both look like you were scared of each other's shadows.")# Ha ha ha ha
   
    if e1_health <= 0:                                                          # If enemy loses all their HP, they die
        print(f"You have {p_health} health points.")
   
    elif p_health <= 0:                                                         # If you lose all your HP, you die
        print("You have been defeated.")
        print("By. A. Bug.  Really?  A bug?")
        print("====================================")
        print("           GAME OVER")
        print("====================================")
        print("Please try again.")
        exit()                                                                  # Should end the game prematurely


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
print("*Knife equipped*")
input()                                                                         # Using input() to break up the action for more suspense


choice: str = input("The kitchen is now safe. Which area do you want to enter? (sitting room/dining room) ") # Gives player a choice where to go
while choice == "sitting room":                                                 # Loop if you go the wrong way
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
    print("You stagger back into the hallway as china shatters on the doorframe.")
    input()
    print(f"{chr_name}: Ow... my head. I need something to cover it.")
    input()                                                                     # Using input() to break up the action for more suspense
    choice: str = input("Which area do you want to enter? (sitting room/dining room) ") # Gives player a choice where to go


print("You enter the dining room and see a gremlin shaped like")
print("a slice of toast on a table gnawing on a candle.")
print("The gremlin notices the sharp edge of the knife you pull out your pocket.")
print("and scrambles back from the table, hissing.")
print("You spot it as it raises an arm: under it, the thick hide thins")
print("to bare, pale skin.")
input()                                                                         # Using input() to break up the action for more suspense




while e2_health > 0 and p_health > 0:
    print()
    choice: str = input("Do you want to attack or dodge? (attack/dodge) ")                     # Choice of whether to attack or dodge
   
    if choice == "attack":                                                      # You chose to attack
        print("You attack!")
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 4:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The gremlin attacks!")
            p_damage = randint(7,22)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e2_damage = randint(8,15)                                           # The enemy attack damage range
            print(f"The gremlin attacks with {e2_damage} damage points.")
   
            if p_damage >= e2_damage:                                           # If your attack is greater than the enemy's, your attack wins
                e2_health = e2_health - p_damage                                # The enemy loses HP
                print(f"The gremlin has {e2_health} health points.")
   
            elif p_damage < e2_damage:                                          # If your attack is less than the enemy's, the enemy wins
                p_health = p_health - e2_damage                                 # You lose HP
                print(f"You have {p_health} health points.")
   
        elif e_choice < 4:                                                      # If enemy RNG is low enough, the enemy dodges
            print("The gremlin dodges!")
            p_damage = randint(7,22)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e2_dodge = randint(5,15)                                            # The enemy dodge range
            print(f"The gremlin has {e2_dodge} dodge points.")
   
            if p_damage >= e2_dodge:                                            # If your attack is >= enemy's dodge, you win
                e2_health = e2_health - (p_damage // 2)                           # Enemy loses health equal to the floor of half of your damage points
                print(f"The gremlin has {e2_health} health points.")
   
            elif p_damage < e2_dodge:
                print("The gremlin successfully dodged your attack.")
   
    elif choice == "dodge":                                                     # You chose to dodge
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 1:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The gremlin attacks!")
            p_dodge = randint(5,15)                                             # Your dodge point range
            print(f"You have {p_dodge} dodge points.")
            e2_damage = randint(8,15)                                           # The enemy attack damage range
            print(f"The gremlin attacks with {e2_damage} damage points.")
   
            if p_dodge >= e2_damage:                                            # If your dodge points >= enemy attack, you dodge without taking damage
                print("You dodged the attack.")
   
            elif p_dodge < e2_damage:                                           # If your dodge points < enemy attack, you dodge but take damage
                p_health = p_health - (e2_damage // 2)                            # You take the floor or half enemy damage
                print(f"You have {p_health} health points.")
   
        elif e_choice < 1:                                                      # If enemy RNG is low enough, the enemy dodges
            print("You and the gremlin both dodged.")
            print("You both look like you were scared of each other's shadows.")# Ha ha ha ha
   
    if e2_health <= 0:                                                          # If enemy loses all their HP, they die
        print(f"You have {p_health} health points.")
   
    elif p_health <= 0:                                                         # If you lose all your HP, you die
        print("You have been defeated.")
        print("====================================")
        print("           GAME OVER")
        print("====================================")
        print("Please try again.")
        exit()                                                                  # Should end the game prematurely


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


choice: str = input("The dining room is now safe. Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go
while choice == "living room":                                                  # Loop if you go the wrong way
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
    print("You wrench free and tumble back into the hallway.")
    print("The zombie stands in the doorway for a moment, then")
    print("shuffles back to the TV and goes on to scratch at its screen.")
    input()
    print(f"{chr_name}: Stabbing it did nothing. And it went straight for my flesh...")
    print(f"{chr_name}: I need something to protect myself before I try that again.")
    print()
    input("...")                                                                     # Using input() to break up the action for more suspense
    print()
    choice: str = input("Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go


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




choice: str = input("Which area do you want to enter? (dining room/sitting room) ") # Gives player a choice where to go
while choice == "dining room":                                                  # Loop to help you go the right way
    print("You are safe in the dining room.")
    choice: str = input("Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go




choice: str = input("Which area do you want to enter? (dining room/sitting room) ") # Gives player a choice where to go
while choice == "dining room":                                                  # Loop to help you go the right way
    print("You are safe in the dining room.")
    choice: str = input("Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go
   
    while choice == "living room":                                              # Loop if you go the wrong way
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
        print("You wrench free and tumble back into the hallway.")
        print("The zombie stands in the doorway for a moment, then")
        print("shuffles back to the screen and goes on to scratch at the screen.")
        input()
        print(f"{chr_name}: Stabbing it did nothing. And it went straight for my flesh...")
        print(f"{chr_name}: I need something to protect myself before I try that again.")
        print()
        input("...")                                                                     # Using input() to break up the action for more suspense
        choice: str = input("Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go
    print("You are safe in the kitchen.")
    choice: str = input("Which area do you want to enter? (dining room/sitting room) ") # Gives player a choice where to go


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


while e3_health > 0 and p_health > 0:
    print()
    choice: str = input("Do you want to attack or dodge? (attack/dodge) ")                     # Choice of whether to attack or dodge
   
    if choice == "attack":                                                      # You chose to attack
        print("You attack!")
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 7:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The goblin attacks!")
            p_damage = randint(7,22)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e3_damage = randint(5,18)                                           # The enemy attack damage range
            print(f"The goblin attacks with {e3_damage} damage points.")
   
            if p_damage >= e3_damage:                                           # If your attack is greater than the enemy's, your attack wins
                e3_health = e3_health - p_damage                                # The enemy loses HP
                print(f"The goblin has {e3_health} health points.")
   
            elif p_damage < e3_damage:                                          # If your attack is less than the enemy's, the enemy wins
                p_health = p_health - e3_damage                                 # You lose HP
                print(f"You have {p_health} health points.")
   
        elif e_choice < 7:                                                      # If enemy RNG is low enough, the enemy dodges
            print("The goblin dodges!")
            p_damage = randint(7,22)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e3_dodge = randint(10,25)                                           # The enemy dodge range
            print(f"The goblin has {e3_dodge} dodge points.")
   
            if p_damage >= e3_dodge:                                            # If your attack is >= enemy's dodge, you win
                e3_health = e3_health - (p_damage // 2)                           # Enemy loses health equal to the floor of half of your damage points
                print(f"The goblin has {e3_health} health points.")
   
            elif p_damage < e3_dodge:
                print("The goblin successfully dodged your attack.")
   
    elif choice == "dodge":                                                     # You chose to dodge
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 3:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The goblin attacks!")
            p_dodge = randint(10,20)                                            # Your dodge point range
            print(f"You have {p_dodge} dodge points.")
            e3_damage = randint(5,18)                                           # The enemy attack damage range
            print(f"The goblin attacks with {e3_damage} damage points.")
   
            if p_dodge >= e3_damage:                                            # If your dodge points >= enemy attack, you dodge without taking damage
                print("You dodged the attack.")
   
            elif p_dodge < e3_damage:                                           # If your dodge points < enemy attack, you dodge but take damage
                p_health = p_health - (e3_damage // 2)                            # You take the floor or half enemy damage
                print(f"You have {p_health} health points.")
   
        elif e_choice < 3:                                                      # If enemy RNG is low enough, the enemy dodges
            print("You and the goblin both dodged.")
            print("You both look like you were scared of each other's shadows.")# Ha ha ha ha
   
    if e3_health <= 0:                                                          # If enemy loses all their HP, they die
        print(f"You have {p_health} health points.")
   
    elif p_health <= 0:                                                         # If you lose all your HP, you die
        print("You have been defeated.")
        print("====================================")
        print("           GAME OVER")
        print("====================================")
        print("Please try again.")
        exit()                                                                  # Should end the game prematurely


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


choice: str = input("The sitting room is now safe. Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go
while choice == "kitchen":                                                      # Loop to help you go the right way
    print("You are safe in the kitchen.")
    choice: str = input("Which area do you want to enter? (dining room/sitting room) ") # Gives player a choice where to go
   
    if choice == "dining room":                                                 # If statement depends on which room you go to
        print("You are safe in the dining room.")
   
    else:
        print("You are safe in the sitting room.")
    choice: str = input("Which area do you want to enter? (kitchen/living room) ") # Gives player a choice where to go


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


while e4_health > 0 and p_health > 0:
    print()
    choice: str = input("Do you want to attack or dodge? (attack/dodge) ")                     # Choice of whether to attack or dodge
   
    if choice == "attack":                                                      # You chose to attack
        print("You attack!")
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 0:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The zombie attacks!")
            p_damage = randint(7,22)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e4_damage = randint(8,25)                                           # The enemy attack damage range
            print(f"The zombie attacks with {e4_damage} damage points.")
   
            if p_damage >= e4_damage:                                           # If your attack is greater than the enemy's, your attack wins
                e4_health = e4_health - p_damage                                # The enemy loses HP
                print(f"The zombie has {e4_health} health points.")
   
            elif p_damage < e4_damage:                                          # If your attack is less than the enemy's, the enemy wins
                p_health = p_health - (e4_damage // 1.5)                        # You lose HP
                print(f"You have {p_health} health points.")
   
        elif e_choice < 0:                                                      # If enemy RNG is low enough, the enemy dodges
            print("The zombie dodges!")
            p_damage = randint(7,22)                                            # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            e4_dodge = randint(0,1)                                             # The enemy dodge range
            print(f"The zombie has {e4_dodge} dodge points.")
   
            if p_damage >= e4_dodge:                                            # If your attack is >= enemy's dodge, you win
                e4_health = e4_health - p_damage // 2                           # Enemy loses health equal to the floor of half of your damage points
                print(f"The zombie has {e4_health} health points.")
   
            elif p_damage < e4_dodge:
                print("The zombie successfully dodged your attack.")
   
    elif choice == "dodge":                                                     # You chose to dodge
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 0:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The zombie attacks!")
            p_dodge = randint(10,20)                                            # Your dodge point range
            print(f"You have {p_dodge} dodge points.")
            e4_damage = randint(10,15) // 2                                     # The enemy attack damage range
            print(f"The zombie attacks with {e4_damage} damage points.")
   
            if p_dodge >= e4_damage:                                            # If your dodge points >= enemy attack, you dodge without taking damage
                e4_health = e4_health - ((p_dodge - e4_damage) // 2)
                print("You blocked the attack.")
                print("Your armor reflected some damage back to the zombie!")
                print(f"The zombie has {e4_health} health points")
   
            elif p_dodge < e4_damage:                                           # If your dodge points < enemy attack, you dodge but take damage
                p_health = p_health - (e4_damage // 5)                            # You take the floor or half enemy damage
                print(f"You have {p_health} health points.")
   
        elif e_choice < 0:                                                      # If enemy RNG is low enough, the enemy dodges
            print("You and the zombie both dodged.")
            print("You both look like you were scared of each other's shadows.")# Ha ha ha ha
   
    if e4_health <= 0:                                                          # If enemy loses all their HP, they die
        print(f"You have {p_health} health points.")
   
    elif p_health <= 0:                                                         # If you lose all your HP, you die
        print("You have been defeated.")
        print("====================================")
        print("           GAME OVER")
        print("====================================")
        print("Please try again.")
        exit()                                                                  # Should end the game prematurely


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


while boss_health > 0 and p_health > 0:
    print()
    choice: str = input("Do you want to attack or dodge? (attack/dodge) ")                     # Choice of whether to attack or dodge
   
    if choice == "attack":                                                      # You chose to attack
        print("You attack!")
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 7:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The orc attacks!")
            p_damage = randint(15,25)                                           # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            boss_damage = randint(15,25)                                        # The enemy attack damage range
            print(f"The orc attacks with {boss_damage} damage points.")
   
            if p_damage >= boss_damage:                                         # If your attack is greater than the enemy's, your attack wins
                boss_health = boss_health - p_damage                            # The enemy loses HP
                print(f"The orc has {boss_health} health points.")
   
            elif p_damage < boss_damage:                                        # If your attack is less than the enemy's, the enemy wins
                p_health = p_health - (boss_damage // 1.5)                      # You lose HP
                print(f"You have {p_health} health points.")
   
        elif e_choice < 7:                                                      # If enemy RNG is low enough, the enemy dodges
            print("The orc dodges!")
            p_damage = randint(15,25)                                           # Your attack damage range
            print(f"You attack with {p_damage} damage points.")
            boss_dodge = randint(20,30)                                         # The enemy dodge range
            print(f"The orc has {boss_dodge} dodge points.")
   
            if p_damage >= boss_dodge:                                          # If your attack is >= enemy's dodge, you win
                boss_health = boss_health - (p_damage // 2)                       # Enemy loses health equal to the floor of half of your damage points
                print(f"The orc has {boss_health} health points.")
   
            elif p_damage < boss_dodge:
                print("The orc successfully dodged your attack.")
   
    elif choice == "dodge":                                                     # You chose to dodge
        e_choice: int = randint(1, 10)                                          # Random number generator for the enemy
   
        if e_choice >= 5:                                                       # If enemy RNG is high enough, the enemy attacks
            print("The orc attacks!")
            p_dodge = randint(10,20)                                            # Your dodge point range
            print(f"You have {p_dodge} dodge points.")
            boss_damage = randint(15,25)                                        # The enemy attack damage range
            print(f"The orc attacks with {boss_damage} damage points.")
   
            if p_dodge >= boss_damage:                                          # If your dodge points >= enemy attack, you dodge without taking damage
                boss_health = boss_health - ((p_dodge - boss_damage) // 2)
                print("You blocked the attack.")
                print("Your armor reflected some damage back to the orc!")
                print(f"The orc has {boss_health} health points")
   
            elif p_dodge < boss_damage:                                         # If your dodge points < enemy attack, you dodge but take damage
                p_health = p_health - (boss_damage // 5)                          # You take the floor or half enemy damage
                print(f"You have {p_health} health points.")
   
        elif e_choice < 5:                                                      # If enemy RNG is low enough, the enemy dodges
            print("You and the orc both dodged.")
            print("You both look like you were scared of each other's shadows.") # Ha ha ha ha
   
    if boss_health <= 0:                                                          # If enemy loses all their HP, they die
        print("You defeated the orc!")
        print(f"You have {p_health} health points.")
   
    elif p_health <= 0:                                                         # If you lose all your HP, you die
        print("You have been defeated.")
        print("You were so close.")
        print("====================================")
        print("           GAME OVER")
        print("====================================")
        print("Please try again.")
        exit()                                                                  # Should end the game prematurely


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


