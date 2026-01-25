# Write your solution here
number = input("Please type in a number: ")
print(f'Integer part: {int(float(number))}')
print(f'Decimal part: {float(number) - int(float(number))}')