# Exercice Coding Accelerator
 
# Séparer une chaine de charactère 

# Importation des modules
import sys

# Fonctionnement principal du programme
def tollbox_split(string_to_cut, string_separator=" "):
    list_array = string_to_cut
    list_len = len(list_array)
    # Vérification
    if list_len == 0:
        return "error"

    splited = []
    marker = 0

    for i in range(list_len):
        # On cherche le séparateur
        if list_array[i] == string_separator:
            if i > marker:
                splited.append(list_array[marker:i])
            marker = i + 1
    
    # On ajoute le dernier mot
    if marker < list_len:
        splited.append(list_array[marker:])

    return splited

# --- Test ---

# Vérification
if len(sys.argv) < 2:
    print("error")
    sys.exit()
reponse = tollbox_split(sys.argv[1])
if reponse == "error":
    sys.exit()
else:
    for mot in reponse:
        print(mot)