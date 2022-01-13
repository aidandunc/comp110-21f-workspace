"""This is for the physics studio."""

mass = eval(input("Enter the mass of the projectile in grams: "))
deltaY = eval(input("Enter the spring compression in cm: "))
hMax = eval(input("Enter the maximum height of the projectile in cm: "))

# convert the mass into kg
mass = float(mass) / 1000
g = 9.8

# convert the compression to meters
# enter your code here

deltaY /= 100

# convert the maximum height to meters
# enter your code here

hMax /= 100

# calculate k for this mass and compression

k = (2 * mass * g * (deltaY + hMax)) / ((deltaY**2))
if(k <= 0):
    print("Invalid (negative) spring constant k – try again!")
else:
    print("Spring constant k = ", k)
    