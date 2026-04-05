# Exercice Coding Accelerator
 
# Tri à ASCII Croissant

# Importation des modules
import sys
from toolbox import triaselction


# Fonctionnement principal du programme
def triASCII(array) :
    error = "error"
    if len(array) < 2 :
        return error , sys.exit() 
    list_array = []
    for x in range (len(array)) :
        list_array.append(array[x])
    list_len = len(list_array)

    # Capture des premiers caractères pour les trier
    list_first_char = []
    for i in range (len(array)):
        list_first_char.append(str(ord(list(list_array[i])[0])))

    # Mise en correspondance des indices
    sorted_list = triaselction(list_first_char).split(' ')
    sorted_list_array = []
    for i in range (len(sorted_list)) :
        for j in range (len(list_first_char)) :
            if sorted_list[i] == list_first_char[j] :
                sorted_list_array.append(list_array[j])

    return ' '.join(sorted_list_array)
                
# Resultat
print(triASCII(sys.argv[1:]))
