"""
Turn_base.py
Ryan S

Making turn base mechanics for battles

"""

from random import randint

#PusedoCode
"""

input("Get Ready to fight!)
input("Press Enter to start!)


Menu Option:

    Protag starts the battle and goes first
    
    Input for Attack:
        leads to Attack
    Input for Guard:
        Guards 3/4 of the incoming attack
    Input for Dodge:
        Chance of Dodge to happen:
            Successful = dodge 100% of incoming damage
            Unsuccessful = gets hit.
    Input for Run away?
    
    SHOWS CURRENT HEALTH STATUS FOR ALL
    
    Enemy turn:
        Choose either Attack, Guard or Dodge
        Attack:
            Leads to attacking hero
        Guard:
            Guards 3/4 of the incoming attack
        Dodge:
        Chance of Dodge to happen:
                    Successful = dodge 100% of incoming damage
                    Unsuccessful = gets hit.

    
        Repeats until Player or Enemy health == 0
            breaks
    Goes to story

"""
print("What is protag going to do?")
print("Attack [1] \n Guard [2] \n Dodge [3]")
# player_choice: str = input(">>>>>>  ")

# choice: int = int(player_choice)
# try:
#     if choice == 1:
#         print("You attacked.")
#         pass
#     elif choice == 2:
#         print("You choose to guard the incoming attack.")
#         pass
#     elif choice == 3:
#         print("You took a gamble to dodge. Lets hope it goes well")
#         pass
# except ValueError:
#     print("Put a number.")
    
# enemy_choice: int = randint(1:4)
# if choice == 1:
#     print("You attacked.")
#     pass
# elif choice == 2:
#     print("You choose to guard the incoming attack.")
#     pass
# elif choice == 3:
#     print("You took a gamble to dodge. Lets hope it goes well")
