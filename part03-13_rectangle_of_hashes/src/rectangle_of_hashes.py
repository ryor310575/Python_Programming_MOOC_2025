# Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.
#
# Sample output
# Width: 10
# Height: 3
# ##########
# ##########
# ##########

# Write your solution here
hash_width=int(input("Width: "))
hash_height=int(input("Height: "))
line_counter=hash_height
while line_counter >0:
    print("#" * hash_width)
    line_counter-=1