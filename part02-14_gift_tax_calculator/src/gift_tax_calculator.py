# Some say paying taxes makes Finns happy, so let's see if the secret of happiness
# lies in one of the taxes set out in Finnish tax code.
#
# According to the Finnish Tax Administration, a gift is a transfer of property to
# another person against no compensation or payment. If the total value of the gifts
# you receive from the same donor in the course of 3 years is €5,000 or more, you must pay gift tax.
#
# When the gift is received from a close relative or a family member, the amount of tax
# to be paid is determined by the following table:
#
# Value of gift	        Tax at the lower limit	    Tax rate for the exceeding part (%)
# 5000 — 25000	        100	                        8
# 25000 — 55000	        1700	                    10
# 55000 — 200000	    4700	                    12
# 200000 — 1000000	    22100	                    15
# 1000000 —	            142100	                    17

# So, for a gift of 6000 euros the recipient pays a tax of 180 euros (100 + (6000 - 5000) * 0.08).
# Similarly, for a gift of 75 000 euros the recipient pays a tax of 7100 euros (4700 + (75000 - 55 000) * 0.12).
#
# Please write a program which calculates the correct amount of tax for a gift from a close relative.
# Have a look at the examples below to see what is expected. Notice the lack of thousands separators
# in the input values - you may assume there will be no spaces or other thousands separators in the
# numbers in the input, as we haven't yet covered dealing with these.
#
# Sample output
# Value of gift: 3500
# No tax!
#
# Sample output
# Value of gift: 5000
# Amount of tax: 100.0 euros
#
# Sample output
# Value of gift: 27500
# Amount of tax: 1950.0 euros


# Write your solution here
gift=int(input("Value of gift: "))
tax_lower_limit=0
tax_exceeding_part=0.0
lower_limit=0.0
if gift<5000:
    # print(f"{gift}<5000")
    lower_limit = 0
    tax_lower_limit = 0
    tax_exceeding_part = 0.0
elif 5000 <= gift < 25000:
    # print(f"5000 <= {gift} < 25000")
    lower_limit = 5000
    tax_lower_limit = 100
    tax_exceeding_part = 0.08
elif 25000 <= gift < 55000:
    # print(f"25000 <= {gift} < 55000")
    lower_limit = 25000
    tax_lower_limit = 1700
    tax_exceeding_part = 0.1
elif 55000 <= gift < 200000:
    # print(f"55000 <= {gift} < 200000")
    lower_limit = 55000
    tax_lower_limit = 4700
    tax_exceeding_part = 0.12
elif 200000 <= gift < 1000000:
    # print(f"200000 <= {gift} < 1000000")
    lower_limit = 200000
    tax_lower_limit = 22100
    tax_exceeding_part = 0.15
elif gift >=1000000:
    # print(f"{gift} <=1000000")
    lower_limit = 1000000
    tax_lower_limit = 142100
    tax_exceeding_part = 0.17

tax_to_pay=(tax_lower_limit+(gift-lower_limit)*tax_exceeding_part)
# print(lower_limit)
# print(tax_lower_limit)
# print(tax_exceeding_part)
# print(gift-lower_limit)
# print(tax_to_pay)

if tax_to_pay>0:
    print(f"Amount of tax: {tax_to_pay} euros")
else:
    print("No tax!")