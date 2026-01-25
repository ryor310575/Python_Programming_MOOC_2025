# Please write a program which asks for the names 
# and ages of two persons. The program should then 
# print out the name of the elder.

# Some examples of expected behaviour:

# Sample output
# Person 1:
# Name: Alan
# Age: 26
# Person 2:
# Name: Ada
# Age: 27
# The elder is Ada


# Person 1:
# Name: Bill
# Age: 1
# Person 2:
# Name: Jean
# Age: 1
# Bill and Jean are the same age

# Write your solution here
print("Person 1:")
p1n = input("Name: ")
p1a = int(input("Age: "))
print("Person 2:") 
p2n = input("Name: ")
p2a = int(input("Age: "))
if p1a > p2a:
    print(f'The elder is {p1n}')
elif p2a > p1a:
    print(f'The elder is {p2n}')
else:
    print(f'{p1n} and {p2n} are the same age')