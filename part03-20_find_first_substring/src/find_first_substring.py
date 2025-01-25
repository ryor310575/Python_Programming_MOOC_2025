# Write your solution here
word=input("Please type in a word: ")
character=input("Please type in a character: ")
char_position=word.find(character)
# print(f"Word Length: {len(word)} Char Positions: {char_position}")
if char_position+3<=len(word) and char_position>=0:
    slice_word=word[char_position:char_position+3]
    print(slice_word)