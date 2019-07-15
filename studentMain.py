# Write code for the function random_verb, which takes in no inputs but outputs 
# one of two verbs randomly. Use the randint function to generate a number from 0-1 
# and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

from random import randint

def random_verb():
    n = randint(0,1)
    if(n == 0):
        print("run")
    else:
        print("kayak")

random_verb()