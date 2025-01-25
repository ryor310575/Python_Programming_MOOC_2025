# Write your solution here
word="Init"
word_length=0
while True:
    if word=="":
        break
    else:
        word=input("Please type in a string: ")
        word_length=len(word)
        print(word)
        print("-"*word_length)
