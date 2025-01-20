# Please write a function named palindromes, which takes a string argument and 
# returns True if the string is a palindrome. Palindromes are words which are 
# spelled exactly the same backwards and forwards.

# Please also write a main program which asks the user to type in words until 
# they type in a palindrome:

# Sample output
# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!
# NB:, the main program should not be within an if __name__ == "__main__": block

# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def invertir_cadena(cadena : str ) -> str:
    cadena_inv=cadena[::-1]
    #for caracter in cadena:
    #    cadena_inv= caracter + cadena_inv
    return cadena_inv

def palindromes(palin : str)->bool:
    palin_rev = invertir_cadena(palin)
    if palin == palin_rev:
        return True
    else:
        return False

def main():
        while True:
            palabra = input("Please type in a palindrome: ")
            if palindromes(palabra) == True:
                print(f'{palabra} is a palindrome!')
                break
            else:
                print("that wasn't a palindrome")


main()
