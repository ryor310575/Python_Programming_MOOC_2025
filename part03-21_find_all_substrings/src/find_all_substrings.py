# Write your solution here
word=input("Please type in a word: ")
character=input("Please type in a character: ")
word_lower=word.lower()
word_sliced=word_lower
while True:
    char_position = word_sliced.find(character)
    word_sliced=word_sliced[char_position:]
    if len(word_sliced)<3:
        break
    else:
        word_to_print=word_sliced[:3]
        word_sliced=word_sliced[1:]
        print(word_to_print)