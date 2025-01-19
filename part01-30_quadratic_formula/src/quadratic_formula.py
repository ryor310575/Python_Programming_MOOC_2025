# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
val_a=int(input("Value of a: "))
val_b=int(input("Value of b: "))
val_c=int(input("Value of c: "))
# x = (-b ± sqrt(b²-4ac))/(2a)
discriminatory=val_b*val_b - 4*val_a*val_c
if discriminatory<0:
    discriminatory=-1*discriminatory
root1= (-1 * val_b + sqrt(discriminatory)) / (2 * val_a)
root2= (-1 * val_b - sqrt(discriminatory)) / (2 * val_a)
print(f"The roots are {root1} and {root2}")