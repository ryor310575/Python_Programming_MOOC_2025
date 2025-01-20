# ****** Older people *******
# Points:
# 0

# /

# 1

# In this exercise we are handling tuples just like the ones described in the previous exercise.

# Please write a function named older_people(people: list, year: int), which selects all those people on the list who were born before the year given as an argument. The function should return the names of these people in a new list.

# An example of its use:

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# older = older_people(people, 1979)
# print(older)
# Write your solution here

def older_people(people: list, year: int)->str:
    names=[]
    for gente in people:
        if gente[1] < year:
            names.append(gente[0])
    return names

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)