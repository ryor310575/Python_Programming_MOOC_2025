# Please write a program which asks the user for two words. 
# The program should then print out whichever of the two 
# comes alphabetically last.

# You can assume all words will be typed in lowercase 
# entirely.

# Some examples of expected behaviour:

# Sample output
# Please type in the 1st word: car
# Please type in the 2nd word: scooter
# scooter comes alphabetically last.

# Sample output
# Please type in the 1st word: zorro
# Please type in the 2nd word: batman
# zorro comes alphabetically last.

# Sample output
# Please type in the 1st word: python
# Please type in the 2nd word: python
# You gave the same word twice.


# Write your solution here
n1 = input("Please type in the 1st word: ")
n2 = input("Please type in the 2nd word: ")
if n1 > n2:
    print(f'{n1} comes alphabetically last.')
elif n2 > n1:
    print(f'{n2} comes alphabetically last.')
else:
    print("You gave the same word twice.")