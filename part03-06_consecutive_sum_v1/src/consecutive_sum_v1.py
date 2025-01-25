# Write your solution here
limit=int(input("Limit: "))
if limit<2:
    limit=2
counter=1
suma=0
while suma<limit:
    # print(f"---- Debug {counter} -------")
    # print(f"suma: {suma}")
    # print (f"counter: {counter}")
    suma=suma+counter
    counter +=1
print(suma)