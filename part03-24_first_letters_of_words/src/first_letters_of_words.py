# Write your solution here
phrase=input("Please type in a sentence: ")
while True:
    if phrase.find(" ")<0:
        print(phrase[0])
        break
    else:
        print(phrase[0])
        phrase = phrase[phrase.find(" ") + 1:]