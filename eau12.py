# Exercice Coding Accelerator
 
# Tri à bulle croissant 

# Importation des modules
import sys

# Fonctionnement principal du programme
def triabulle(array) :
    error = "error"
    if len(array) < 2 :
        return error , sys.exit() 
    list_array = []
    list_len = len(list_array)

    for i in range (list_len) :
        if not (ord(list_array[i]) >= 48 and ord(list_array[i]) <= 57)  :
            return error, sys.exit()
    # Vérification d'acquisition de nombre
    for x in range (len(array)) :
        if int(array[x]) :
            list_array.append(array[x])
        else :
            return error , sys.exit() 
    list_len = len(list_array)
    for i in range(list_len):
        for j in range (0, list_len - 1 ):
            if int( list_array[j]) > int(list_array[j + 1]) :
                list_array[j], list_array[j + 1]  = list_array[j + 1], list_array[j]

    return list_array
                
# Resultat
print(triabulle(sys.argv[1:]))
