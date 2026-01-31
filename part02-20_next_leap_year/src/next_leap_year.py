# Please write a program which asks the user for a year, and prints out the next leap year.
#
# Sample output
# Year: 2023
# The next leap year after 2023 is 2024
#
# If the user inputs a year which is a leap year (such as 2024),
# the program should print out the following leap year:
#
# Sample output
# Year: 2024
# The next leap year after 2024 is 2028
#---------------------------------------
# Leap Year program as reference
# year=int(input("Please type in a year: "))
# if year%100==0:
#     if year%400==0:
#         if year%400==0:
#             print("That year is a leap year.")
#         else:
#             print("That year is not a leap year.")
#     else:
#         print("That year is not a leap year.")
# elif year%4==0:
#     print("That year is a leap year.")
# else:
#     print("That year is not a leap year.")


# Write your solution here
year=int(input("Year: "))
year_counter=year
while True:
    year_counter+=1
    if year_counter%100==0:
        if year_counter%400==0:
            print(f"The next leap year after {year} is {year_counter}")
            break
    elif year_counter%4==0:
        print(f"The next leap year after {year} is {year_counter}")
        break

