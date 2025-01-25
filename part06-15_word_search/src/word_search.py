# The exercise template includes the file words.txt, which contains words in English.

# Please write a function named find_words(search_term: str). It should return a list containing 
# all the words in the file which match the search term.

# The search term may include lowercase letters and the following wildcard characters:

# A dot . means that any single character is acceptable in its place. For example, ca. would yield 
# words like cat and car, p.ng would yield words like ping and pong, and .a.e would yield words like 
# sane, care and late.
# An asterisk * at the end of the search term means that any word which begins with the search term 
# is acceptable. An asterisk at the beginning of the search term means that any word which ends with
# the search term is acceptable. For example, ca* would yield words like california, cat, caring and 
# catapult, while *ane would yield words like crane, insane and aeroplane. There can only ever be a 
# single asterisk in the search term.
# If there are no wildcard characters in the search term, only words which match the search term 
# exactly are returned.
# You may assume both wildcards are never used in the same search term.

# The words in the file are all written in lowercase. You may also assume the argument to the function 
# will be in lowercase entirely.

# If no matching words are found, the function should return an empty list.

# Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search 
# for more information about them online.

# An example of the function in action:

# print(find_words("*vokes"))
# Sample output
# ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']

# Write your solution here
#******************** FUNCTION *************************
#*********    look for asterisk wld card        ********
#*******************************************************
def asterisk_wild(search_term: str)->list:
    words_found=[]
    word_to_search=""
    if "*" in search_term: # Evalua que exista el termino *
        if search_term[0]=="*": # Verifica que este al inicio
            word_to_search=search_term[1:].lower() # Elimina el primer termino y lo lleva a miusculas
            with open("words.txt") as my_file:
                for line in my_file:
                    if line.strip().endswith(word_to_search):# Revisa si la palabra finaliza con la cadena buscada
                        words_found.append(line.strip())
        elif search_term[-1]=="*":# Verifica que este al final
            word_to_search=search_term[:-1].lower()# Elimina el ultimo termino y lo lleva a miusculas
            with  open("words.txt") as my_file:
                for line in my_file:
                    if line.strip().startswith(word_to_search): # Revisa si la palabra inicia con la cadena buscada
                        words_found.append(line.strip())
    else:
        words_found[0]="no asterisk"
    return words_found
#******************** FUNCTION *************************
#*********            change pos               ********
#*******************************************************
def change_pos(word:str,position:int,character:str)->str:
    new_word=""
    new_word=word[0:position]+character+word[(position+1):]
    return new_word

#******************** FUNCTION *************************
#*********       look for dot wild card          ********
#*******************************************************
def wild_card_words(search_list:list,wild_card:str)-> list:
    wild_words_list=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for word in search_list:
        dot_position=word.find(wild_card)
        if dot_position==-1: # Evalua que exista el termino DOT
            wild_words_list=search_list
            return wild_words_list
        else:
            i=0
            while i<len(alphabet):
                new_word=word[0:dot_position]+alphabet[i]+word[(dot_position+1):]
                wild_words_list.append(new_word)
                i+=1
    wild_words_list=wild_card_words(wild_words_list,wild_card)
    return wild_words_list

#******************** FUNCTION *************************
#*********       look for dot wild card          ********
#*******************************************************
def wild_card_words_2(search_list:list,wild_card:str)-> list:
    wild_words_list=[]
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for word in search_list:
        dot_position=word.find(wild_card)
        if dot_position==-1: # Evalua que exista el termino DOT
            wild_words_list=search_list
            return wild_words_list
        else:
            for x in alphabet:
                new_word=word.replace(wild_card,x,1)
                wild_words_list.append(new_word)
    wild_words_list=wild_card_words_2(wild_words_list,wild_card)
    return wild_words_list

#******************** FUNCTION *************************
#*********       look for dot wild card         ********
#*******************************************************
def dot_wild(search_term:str)-> list:
    words_found=[]
    word_to_search=[]
    if "." in search_term: # Evalua que exista el termino DOT
        # word_to_search=wild_card_words([search_term],".")
        word_to_search=wild_card_words_2([search_term],".")
        with  open("words.txt") as my_file:
            for line in my_file:
                line=line.strip()
                if  line in word_to_search:
                    words_found.append(line)
    else:
        words_found[0]="no dot"
    return words_found


#********************   MAIN   *************************
#*********         Execute Find words           ********
#*******************************************************
def find_words(search_term: str)->list:
    words_found=[]
    if "*" in search_term:
        words_found=asterisk_wild(search_term)
    elif "." in search_term:
        words_found=dot_wild(search_term)
    else:
        with  open("words.txt") as my_file:
            for line in my_file:
                if line.strip() == search_term:
                    words_found.append(line.strip())
    return words_found

def main():
    print(find_words("car.y"))
    print(find_words(".are"))
    print(find_words("carr*"))
    print(find_words("*arry"))
    print(find_words("care"))
main()