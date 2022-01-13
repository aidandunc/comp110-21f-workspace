"""More examples of while loops."""

user_string = str(input("Please input a string: "))

counter = int(0)

while counter < len(user_string):
    print(user_string[counter])
    counter += 1

print("Done!")