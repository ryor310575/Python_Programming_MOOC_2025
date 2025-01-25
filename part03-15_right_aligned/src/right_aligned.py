# Write your solution here
in_str=input("Please type in a string: ")
tst_str=in_str
while len(tst_str)<20:
    tst_str="*" + tst_str
    # print(f"Current length: {len(tst_str)} tst_str: {tst_str}")
print(tst_str)