# ********** Phone book, version 2 **********
# Please write an improved version of the phone book application. Each entry should 
# now accommodate multiple phone numbers. The application should work otherwise 
# exactly as above, but this time all numbers attached to a name should be printed.

# Sample output
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...
# Write your solution here
phone_book={}
while True:
    command=int(input("command (1 search, 2 add, 3 quit): "))
    # Salir
    if command == 3:
        print("quitting...")
        break
    # Buscar
    elif command==1:
        name=input("name: ")
        if name in phone_book:
            for tlf in phone_book[name]:
                print(tlf)
        else:
            print("no number")
    # Agregar
    elif command==2:
        name=input("name: ")
        number=input("number: ")
        if name not in phone_book:
            phone_book[name]=[]
        phone_book[name].append(number)
        print("ok!")
    else:
        print("Wrong Selection")