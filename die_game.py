import os
import random

def die_tuple():
    rolls = []  # Initialize an empty list to store results
    for _ in range(3):  # Loop three times for three die rolls
        this_roll = random.choice(die_faces)  
        rolls.append(this_roll)  
    return rolls  # Return the list of roll results

die_faces = (1, 2, 3, 4, 5, 6)
rolls = die_tuple()

print("Rolls:", rolls)

# Check if all rolls are the same
if all(roll == rolls[0] for roll in rolls):
    print("You TUPLED OUT, better luck next time.")
    print("GAME OVER")
