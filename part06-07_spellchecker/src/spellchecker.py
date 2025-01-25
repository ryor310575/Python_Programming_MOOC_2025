#*******************************************************
#***************      Spell checker      ***************
#*******************************************************
# Please write a program which asks the user to type in some text. Your program should then perform a 
# spell check, and print out feedback to the user, so that all misspelled words have stars around them. 
# Please see the two examples below:

# Sample output
# Write text: We use ptython to make a spell checker

# We use *ptython* to make a spell checker
# Sample output
# Write text: This is acually a good and usefull program

# This is *acually* good and *usefull* program
# The case of the letters should be irrelevant to the functioning of your program.

# The exercise template includes the file wordlist.txt, which contains all the words the spell checker 
# should accept as correct.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an 
# if __name__ == "__main__" block.

# NB2 If Visual Studio can't find the file and you have checked that there are no spelling errors, 
# take a look at these instructions.


#*******************************************************
# write your solution here
#*******************************************************

#**    Convertir un archivo a lista version lenta  ****
# Esta funcion convierte un archivo con palabras en cada 
# lineaen un arreglo
# 1) Toma el archivo diccionario y lo convierte en un 
# arreglo para recorrerlo.
#*******************************************************
def file_to_list_V0(fle_name:str)->list:
    file_info = [] #Abre una lista vacia
    with open(fle_name) as new_file:
        for line in new_file:
            file_info.append(line.strip())
    return file_info

#**    Convertir un archivo a lista version rapida  ****
# Esta funcion convierte un archivo con palabras en cada 
# lineaen un arreglo
# 1) Toma el archivo diccionario y lo convierte en un 
# arreglo para recorrerlo.
#*******************************************************
def file_to_list(fle_name:str)->list:
    file_info = [] #Abre una lista vacia
    my_new_file=open(fle_name)
    my_new_file_text=my_new_file.read()
    file_info=my_new_file_text.split('\n')
    return file_info

#*********     Convertir una lista a diccionario     ********
# Esta funcion convierte una lista con palabras en cada linea
# en un diccionario
# 1) Toma el archivo diccionario y lo convierte en diccionario 
# ordenado alfabeticamente por la primera palabra.
#*******************************************************
def list_to_dict(file_list:list)->dict:
    file_dict_info = {} #Abre un diccionario vacio
    for word in file_list:
        if word =='':
            continue
        initial=word[0].strip()
        # initialize a new list when the letter is first encountered
        if initial not in file_dict_info:
            file_dict_info[initial]=[]
        file_dict_info[initial].append(word)
    return file_dict_info

#*******************************************************
# This fuction compare to words. The case doesnt care.
# first verify if the words have the same numbers of characters
# then verify if two words have the same characters.
# finally verify the order. If have some diference return the word
# into stars
# If everything is the same return the same word
#*******************************************************

def evaluate_words(word_to_check:str, word_right:str)-> bool:
    compare_indicator=True # Assume the words are the same
    # Set both words as lower case
    word_to_check_lower= word_to_check.lower()
    word_right_lower=word_right.lower()
    # Remove not printable characters with STRRIP Method
    word_to_check_lower= word_to_check_lower.strip()
    word_right_lower=word_right_lower.strip()
    #Compare the words
    if word_to_check_lower != word_right_lower:
        compare_indicator=False
    return compare_indicator

def main():
    # Get the new text and put it into a list
    text_to_spell=input("Write text: ")
    #text_to_spell="This is acually a good and usefull program"
    
    # Separa las palabras de la frase en una lista
    new_text_list=text_to_spell.split()
    text_spell_result=""
    # Obtiene la lista con palabras correctas.
    list_rigth_words=file_to_list("wordlist.txt")
    # ordena la lista en un diccionario por iniciales.
    dict_rigth_words=list_to_dict(list_rigth_words)

    for word_to_spell in new_text_list:
        word_to_spell_lower=word_to_spell.lower()
        initial=word_to_spell_lower[0]
        list_rigth_words=dict_rigth_words[initial]
        if word_to_spell_lower not in list_rigth_words:
            word_to_spell=f'*{word_to_spell}*'
            text_spell_result=text_spell_result + word_to_spell + " "
        else:
            text_spell_result= text_spell_result + word_to_spell + " "
    text_spell_result=text_spell_result.strip()
    print(text_spell_result)

main()