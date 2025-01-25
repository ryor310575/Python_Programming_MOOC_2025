# Write your solution here
limit=int(input("Please type in a number: "))
num1=0
num2=0
counter=1
while counter<=limit:
    num1=counter
    if num1<limit:
        num2=counter+1
        print(num2)
        print(num1)
        counter = num2 + 1
    else:
        print(num1)
        counter +=1