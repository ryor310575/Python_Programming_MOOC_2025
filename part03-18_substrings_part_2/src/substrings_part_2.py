# Write your solution here
word=input("Please type in a string: ")
word_length=len(word)
counter=word_length-1
# print(f"The length is {word_length}")
while counter>=0:
    partial_word=word[counter:]
    print(partial_word)
    # print(f"{counter}: {partial_word}")
    counter-=1