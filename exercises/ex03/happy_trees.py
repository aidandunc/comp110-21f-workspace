"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth = int(input("Depth: "))
i = 1
j = 1

while i < depth + 1:
    while j < depth + 1:
        print(TREE * j)
        j += 1
    i += 1