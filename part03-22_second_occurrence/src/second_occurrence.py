# Write your solution here
word=input("Please type in a string: ")
sub_str=input("ase type in a substring: ")
counter=0
position=0
while True:
    if counter>1:
        print(f"The second occurrence of the substring is at index {position-len(sub_str)}.")
        break
    elif word.find(sub_str) < 0:
        print("The substring does not occur twice in the string.")
        break
    else:
        str_position=word.find(sub_str)
        position = position + str_position
        word=word[str_position:]
        word=word[len(sub_str):]
        position = position + len(sub_str)
        counter+=1
