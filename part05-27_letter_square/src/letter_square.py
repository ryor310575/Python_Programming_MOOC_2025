# ********* A square of letters **********
# This final exercise in this part is a relatively demanding problem solving task. 
# It can be solved in many different ways. Even though this current section in the 
# material covers tuples, tuples are not necessarily the best way to go about solving this.

# Please write a program which prints out a square of letters as specified in the examples 
# below. You may assume there will be at most 26 layers.

# Sample output
# Layers: 3

# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC
# Sample output
# Layers: 4

# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD
# NB: this exercise doesn't ask you to write any functions, so you should not 
# place any code within an if __name__ == "__main__" block.

# Write your solution here
# Write your solution here
# String with a length given times is how LONG IS THE FINAL STR
def char_string(character:str,times:int)->str:
    new_word=""
    while len(new_word)<times:
        new_word=new_word+character
    return new_word

# Agrega una cantidad de caracteres al inicio de una cadena
def initial_pad(character:str,word:str,times:int)->str:
    new_word=word
    i=0
    while i<times:
        new_word=character+new_word
        i+=1
    return new_word
# Agrega una cantidad de caracteres al final de una cadena
def final_pad(character:str,word:str,times:int)->str:
    new_word=word
    i=0
    while i<times:
        new_word=new_word+character
        i+=1
    return new_word
# Agrega caracteres al inicio y al final de una cadena de forma balanceada
def bilateral_pad(character:str,word:str,times:int)->str:
    new_word=initial_pad(character,final_pad(character,word,times),times)
    return new_word
# Completa letras ascendentes hasta llegar al tamano deseado de la cadena
def max_pad(word:str,size:int,alphabet:tuple,char_pos:int)->str:
    character=""
    new_word=word
    word_lenght=len(new_word)
    while word_lenght < size:
        character=alphabet[char_pos]
        new_word=bilateral_pad(character,new_word,1)
        word_lenght=len(new_word)
        char_pos+=1
    return new_word

def print_square(layers:int):
    alphabet=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    counter=layers-1
    character=""
    max_size=2*layers-1
    word_size=2*layers-1
    # Dibujar la parte superior
    while character!="A":
        character=alphabet[counter]
        new_word=char_string(character,word_size)
        new_word=max_pad(new_word,max_size,alphabet,counter+1)
        print(new_word)
        character=alphabet[counter]
        word_size-=2
        counter-=1
    # Dibujar la parte inferiro 
    counter=1
    word_size=3
    character=alphabet[counter]
    new_word=char_string(character,word_size)
    while True:
        character=alphabet[counter]
        new_word=char_string(character,word_size)
        print(max_pad(new_word,max_size,alphabet,counter+1))
        counter+=1
        word_size+=2
        if len(new_word)>=max_size:
            break
        





def main():
    layers=int(input("Layers: "))
    print_square(layers)

main()