# Please write a program which asks the user for words. If the user types 
# in a word for the second time, the program should print out the number 
# of different words typed in, and exit.

# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

# NB: this exercise doesn't ask you to write any functions, so you should 
# not place any code within an if __name__ == "__main__" block.
# Write your solution here
my_list = []
i = 0
count = 0
item_word = ""
while True :
    item_word = input('Word: ')
    if item_word not in my_list:
        count +=1
    else:
        break
    my_list.append(item_word)
print(f'You typed in {count} different words')