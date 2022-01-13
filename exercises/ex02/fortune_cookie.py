"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730530362"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says...")
random_number = randint(1, 4)
if random_number == 1:
    print("You will see great success in the very near future.")
else:
    if random_number == 2:
        print("You are about to enter a chapter in your life full of happiness and blessings.")
    else:
        if random_number == 3:
            print("A life-changing something (or someone) is about to enter your life.")
        else:
            if random_number == 4:
                print("Everything will turn out just as it was meant to.")
            else:
                print("Error: I messed up the code")

print("Now, go spread positive vibes!")