"""Counting letters in a string."""

__author__ = "730530326"

letter_of_interest = str(input("What letter do you want to search for? "))
word_of_interest = str(input("Enter a word: "))
i = int(0)
number_of_instances = int(0)

while i < len(word_of_interest):
    if word_of_interest[i] == letter_of_interest:
        i += 1
        number_of_instances += 1
    else:
        i += 1

print("Count: " + str(number_of_instances))
