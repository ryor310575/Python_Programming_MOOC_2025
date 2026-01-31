# This program should print out a countdown. The code is as follows:
#
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number > 0:
#     break
#
# print("Now!")
# This should print out
#
# Sample output
# Countdown!
# 5
# 4
# 3
# 2
# 1
# Now!
#
# However, the program doesn't quite work. Please fix it.
#
# 12345678910


number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number <= 0:
    break

print("Now!")