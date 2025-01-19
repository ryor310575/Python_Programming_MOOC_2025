# Write your solution here
students_count=int(input("How many students on the course?"))
group_size=int(input("Desired group size?"))
int_resoult=students_count//group_size
fraction_resoult=students_count/group_size
if students_count%group_size==0:
    rest_resoult=0
else:
    rest_resoult = 1
# print(f"int: {int_resoult} frac: {fraction_resoult} rest: {rest_resoult}")
group_formed=students_count//group_size + rest_resoult
print(f"Number of groups formed: {group_formed}")