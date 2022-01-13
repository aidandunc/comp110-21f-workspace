"""An example of condiitonal statements."""

SECRET = int(3)

print("I'm thinking of a number between 1-5, what is it?")
guess = int(input("What is your guess? "))

if guess == SECRET:
    print("Correct! The number was " + str(SECRET) + "!")
else:
    print("Sorry! You guessed incorrectly.")
    if guess < SECRET:
        print("Try guessing higher!")
    else:
        print("Try going a little lower!")