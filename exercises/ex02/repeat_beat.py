"""Repeating a beat in a loop."""

__author__ = "730530326"

beat = str(input("What beat do you want to repeat?"))
repeats = int(input("How many times do you want to repeat it? "))

if repeats > 0:
    print((beat + " ") * (repeats - 1) + beat)
else:
    print("No beat...")