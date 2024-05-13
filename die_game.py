# rand
import random
import os

die_faces = (1,2,3,4,5,6)

random.choice(die_faces)
# create a function (.choice) then use () to choose from the prefered function
while True:
    rolls = 0
    roll_counts =  {1:0 
                   ,2:0
                   ,3:0
                   ,4:0
                   ,5:0
                   ,6:0} 
    roll_results = [] # mutable list
    #roll_results keeps track of # in a list 
    while rolls <3:
        this_roll = random.choice(die_faces)
        roll_results.append(this_roll)
        roll_counts[this_roll] += 1
        rolls += 1
        break
    if not



print(roll_results)

print(roll_counts)