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