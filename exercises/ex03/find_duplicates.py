"""Finding duplicate letters in a word."""

__author__ = "730530326"

word = str(input("Enter a word: "))


i = 0
j = 0
truth_indicator = 0

while i < len(word):
    while j < (len(word[i + 1:])):
        if word[i] == word[i + 1:][j]:
            truth_indicator += 1
            j += 1
        else:
            j += 1
    i += 1
    j = 0

if truth_indicator == 0:
    print("Found duplicate: False")
else:
    print("Found duplicate: True")
