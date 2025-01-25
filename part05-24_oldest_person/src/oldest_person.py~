# ******* The oldest person **********
# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

# An example of the function in action:

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))
# Sample output
# Mary
# Write your solution here
def oldest_person(people: list)->str:
    oldest_name=""
    names=[]
    birthdays=[]
    for gente in people:
        names.append(gente[0])
        birthdays.append(gente[1])
    small_year=min(birthdays)
    year_possition=birthdays.index(small_year)
    oldest_name=names[year_possition]

    return oldest_name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    #people = [('Arthur', 1977), ('Emily', 2014)]

    print(oldest_person(people))