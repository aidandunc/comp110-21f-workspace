"""Examples of using lists to construct a basic game. """


from random import randint

rolls: list[int] = list()

while 1 not in rolls:
    rolls.append(randint(1, 6))
rolls.pop(len(rolls) - 1)
total = 0
i = 0
while i < len(rolls):
    total += rolls[i]
    i += 1

print(total)

print(rolls)

print(sum(rolls))