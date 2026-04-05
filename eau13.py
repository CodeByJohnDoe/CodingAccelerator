# Exercice Coding Accelerator
 
# Tri à par selection croissant 

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
    for i in range(list_len- 1):
        current_min = int(list_array[i])
        idx = i
        for j in range (i , list_len):

            if current_min > int(list_array[j]) :
                current_min = int(list_array[j])
                idx = j
        list_array[i], list_array[idx] = str(current_min) ,list_array[i]

    return ' '.join(list_array)
                
# Resultat
print(triabulle(sys.argv[1:]))
