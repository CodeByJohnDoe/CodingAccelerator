# Exercice Coding Accelerator
 
# Mettre la premiere lettre en majuscules et les autres en minuscules

# Importation des modules
import sys

# Fonctionnement principal du programme
def first_up() :
    error = "error"
    if len(sys.argv) != 2 :
        return sys.exit()
    argv = sys.argv[1].split()
    result = []
    delta_majascii = ord("a") - ord("A")


    for i in range (len(argv)) :
        current_string = list(argv[i])
        first_lettercheck = False
        new_string = []

        # Recherche d'une lettre
        for j in range(len(current_string)):
            if current_string[j].isalpha() :
                # Recherche de la premiere lettre pour la mettre en majuscule
                if first_lettercheck == False and ord(current_string[j]) >= 97 :
                    new_string.append(chr(ord(current_string[j]) - delta_majascii))
                    first_lettercheck = True
                else :
                    new_string.append(current_string[j])
            else :
                new_string.append(current_string[j])
        result.append(''.join(new_string))

    # Assemblage
    result = ' '.join(result)

    return result

# Resultat
print(first_up())
