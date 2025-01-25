# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    counter = number
    factorial = 1
    if number<=0:
        print("Thanks and bye!")
        break
    while counter >=1:
        factorial = factorial * counter
        counter -= 1
    print(f"The factorial of the number {number} is {factorial}")