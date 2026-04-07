# Exercice Coding Accelerator
 
# Tri à par selection croissant 

# Importation des modules
import sys

# Fonctionnement principal du programme
def tollbox_split(array, string_separator) :
    error = "error"
    if not array :
        return error , sys.exit() 
    list_array = []
    list_len = len(list_array)

    # Vérification d'acquisition de nombre
    splited = []
    marker = 0
    for i in range (list_len) :
        current_split = []
        if list_array [i] == string_separator :
            current_split.append(list_array[marker:i -1 ]) 
        if list_array [i] == list_len :
            current_split.append(list_array[marker:i ]) 

    return splited
                
# Resultat
string = " "
for i in (tollbox_split(sys.argv[1:]), string) :
    print(i)