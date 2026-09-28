"""
    project1.py
    Daniel Waughtel
    Ryan
    Andre


    A text adventure
"""


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










########### Conclusion


input()
print("You walk to the front door.")
print("You rummage past the kitchen knife and zombie arm in your pocket to pull out the key.") # change items in pocket
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
done()
