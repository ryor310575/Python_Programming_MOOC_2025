# Write your solution here
phrase= input("Please type in a string: ")
phrase_lower=phrase.lower()
a_case=""
e_case=""
o_case=""
if "a" in phrase_lower:
    a_case="a found"
else:
    a_case = "a not found"
if "e" in phrase_lower:
    e_case="e found"
else:
    e_case = "e not found"
if "o" in phrase_lower:
    o_case="o found"
else:
    o_case = "o not found"
print(a_case)
print(e_case)
print(o_case)