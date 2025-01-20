# ***********  Numbers spelled out  ***********
# Please write a function named dict_of_numbers(), which returns a new dictionary. 
# The dictionary should have the numbers from 0 to 99 as its keys. The value attached 
# to each key should be the number spelled out in words. Please have a look at the 
# example below:

# numbers = dict_of_numbers()
# print(numbers[2])
# print(numbers[11])
# print(numbers[45])
# print(numbers[99])
# print(numbers[0])
# Sample output
# two
# eleven
# forty-five
# ninety-nine
# zero

# NB: Please don't formulate each spelled out number by hand. Figure out how you 
# can use loops and dictionaries in your solution.


# Write your solution here
def dict_of_numbers()->dict:
    new_dict={}
    numbers_dict={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    for number in range(100):
        if number < 14:
            new_dict[number]=numbers_dict[number]
        elif number >= 14 and number < 20:
            new_dict[number]=str(numbers_dict[number-10])+"teen"
            if number == 18:
                new_dict[number]="eighteen"
            if number == 15:
                new_dict[number]="fifteen"
        elif number >=20:
            first_part=str(numbers_dict[int(number // 10 * 10)])
            second_part= str(numbers_dict[int(number % 10)])
            if second_part == 'zero':
                new_dict[number]=first_part
            else:
                new_dict[number]=first_part + "-" + second_part
    return new_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[16])
    print(numbers[18])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
