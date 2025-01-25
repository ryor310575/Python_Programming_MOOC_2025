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