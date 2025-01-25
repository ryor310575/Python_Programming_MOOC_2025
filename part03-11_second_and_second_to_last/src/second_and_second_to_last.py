# Write your solution here
word=input("Please type in a string: ")
if len(word)<2:
    print("String too short")
else:
    if word[1]==word[-2]:
        print(f"The second and the second to last characters are {word[1]}")
    else:
        print("The second and the second to last characters are different")