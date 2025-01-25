# Write your solution here
word=input("Please type in a string: ")
counter=1
word_length=len(word)
# print(f"The length is {word_length}")
while counter<=word_length:
    partial_word=word[:counter]
    print(partial_word)
    # print(f"{counter}: {partial_word}")
    counter+=1