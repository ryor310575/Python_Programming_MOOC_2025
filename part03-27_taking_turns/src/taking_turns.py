# Please write a program which asks the user to type in a number.
# The program then prints out the positive integers between 1
# and the number itself, alternating between the two ends of the
# range as in the examples below.
#
# Sample output
# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3
#
# Sample output
# Please type in a number: 6
# 1
# 6
# 2
# 5
# 3
# 4
# Write your solution here
limit=int(input("Please type in a number: "))
down_top=1
top_down=limit
while down_top<=limit:
    if down_top<top_down:
        print(down_top)
        print(top_down)
    elif down_top==top_down:
        print(down_top)
    else:
        break
    down_top+=1
    top_down-=1