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
def fight(hero, enemy) -> None:
    print(f"Will {Hero.name} win or will they fall?")
    
    while hero.health > 0 and enemy.health >0:
        hero.is_dodging:bool = False
        hero.is_guarding: bool = False
        enemy.is_dodging: bool = False
        enemy.is_guarding: bool = False
        
        print("\n" + "=" * 40)
        hero.health_bar.draw()
        enemy.health_bar.draw()
        print("=" * 40)
        
        print("Attack [1] \n Guard [2] \n Dodge [3]")
        player_choice: int = int(input(">>>>>>  "))
        
        try:
            if player_choice == 1:
                print(f"{Hero.Name} attacks {Enemy.name}!")
                hero.attack(enemy)
                valid_turn = True
            elif player_choice == 2:
                print(f"{Hero.name} chose to brace the incoming attack.")
                hero.guard()
                valid_turn = True
            elif player_choice == 3:
                print(f"{Hero.name} choose to gamble their odds.")
                hero.dodge
                if hero.is_dodging:
                    print(f"{Hero.name} became Neo from the matrix!")
                else:
                    print(f"{Hero.name} fell to the ground and got hit, and have back pain.")
                valid_turn = True
        except ValueError:
                print("Invalid input! Please type a number, not letters or symbols. You goober.")
                
        if enemy.health <= 0:
            print("You showed them whos boss.")
            break
        
        print(f"Now its {enemy.name} turn to decide what to do.")
        enemy_action = randint(1,3)
        
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
                print(f"{enemy.name} attempts to dodge, but misses the timing!)

        if hero.health <= 0:
            print(f"\n{hero.name} has been defeated...")
            print("====================================")
            print("           GAME OVER")
            print("====================================")
            print("Please try again.")
            exit()