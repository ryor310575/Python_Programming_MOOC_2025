# Write your solution here
word=input("Word: ")
word_length=len(word)
print("*"*30)
if word_length%2==0:
    space_right=" " * ((30-2-word_length)//2)
    space_left=" " * ((30-2-word_length)//2)
    print("*"+space_right+word+space_left+"*")
else:
    space_right=" " * ((30-2-(word_length-1))//2)
    space_left=" " * (((30-2-(word_length-1))//2)-1)
    print("*"+space_right+word+space_left+"*")
print("*"*30)