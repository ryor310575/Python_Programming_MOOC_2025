# Write your solution here
hash_width=int(input("Width: "))
hash_height=int(input("Height: "))
line_counter=hash_height
while line_counter >0:
    print("#" * hash_width)
    line_counter-=1