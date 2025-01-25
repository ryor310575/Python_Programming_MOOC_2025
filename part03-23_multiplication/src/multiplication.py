# Write your solution here
limit=int(input("Please type in a number: "))
i = 1
suma=0
while i<=limit:
    j = 1
    while j<=limit:
        suma=i*j
        print(f"{i} x {j} = {suma}")
        j+=1
    i+=1