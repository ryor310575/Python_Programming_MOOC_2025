# Write your solution here
while True:
    name = input("Editor: ")
    name_lower = name.lower()
    if name_lower == "visual studio code":
        print("an excellent choice!")
        break
    elif name.lower() == "word" or name == "notepad":
        print("awful")
    # elif name_lower.find("visual studio code") and name_lower.find("emacs"):
    #     print("an excellent choice!")
    #     print("an excellent choice!")
    else:
        print("not good")