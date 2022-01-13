"""An exercise in remainders and boolean logic."""

__author__ = "730530326"

number = int(input("Enter an int: "))

if (number / 2 == number // 2) or (number / 7 == number // 7):
    if number / 2 == number // 2:
        if number / 7 == number // 7:
            print("TAR HEELS")
        else:
            print("TAR")
    else:
        if number / 7 == number // 7:
            print("HEELS")
else:
    print("CAROLINA")
