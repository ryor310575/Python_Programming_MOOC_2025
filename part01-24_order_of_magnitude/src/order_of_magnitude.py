# Write your solution here
num=int(input("Please type in a number: "))
if num>1000:
    print("Thank you!")
elif num<10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")
elif num<100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
else:
    print("This number is smaller than 1000")
    print("Thank you!")