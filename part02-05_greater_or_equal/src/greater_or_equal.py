# Write your solution here
# Please write a program which asks for two 
# integer numbers. The program should then 
# print out whichever is greater. If the numbers 
# are equal, the program should print a different message.

n1 = int(input("Please type in the first number: "))
n2 = int(input("Please type in another number: "))
if n1 > n2:
    print(f'The greater number was: {n1}')
elif n2 > n1:
    print(f'The greater number was: {n2}')
else:
    print("The numbers are equal!")