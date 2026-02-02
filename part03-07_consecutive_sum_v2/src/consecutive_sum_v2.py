# Please write a new version of the program in the previous exercise.
# In addition to the result it should also print out the calculation performed:
#
# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3
#
# Sample output
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10
#
# Sample output
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21
#
# You may assume the number typed in by the user is always equal to 2 or higher.

# Write your solution here
limit=int(input("Limit: "))
if limit<2:
    limit=2
counter=1
suma=0
suma_string="The consecutive sum: "
while suma<limit:
    suma=suma+counter
    suma_string = suma_string + str(counter)
    if suma<limit:
      suma_string = suma_string + " + "
    counter +=1
print(suma_string+" = " + str(suma))