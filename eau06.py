# Exercice Coding Accelerator
 
# Mettre une lettre sur deux en Maj

# Importation des modules
import sys

# Fonctionnement principal du programme
def upper_1of2() :
    error = "error"
    if len(sys.argv) != 2 :
        return sys.exit() 

    # Vérifcation qu'on a au moins une lettre
    test = list(sys.argv[1])
    check = []
    for char in range (len(test)):
        if str(test[char]).isalpha() :
            check.append(True)
        else :
            check.append(False)
    
    if not any(check) :
        return error

    # Mise en majuscule d'une lettre sur deux 
    delta_majascii = ord("a") - ord("A")
    result = []
    maj = True
    for abc in range (len(test)):
        if (test[abc]).isalpha() and maj == True :
            ord_char = ord(test[abc])
            if ord_char >= ord("a") :
                result.append(chr(ord_char - delta_majascii))
            else :
                result.append(test[abc])
            maj = False
        elif (test[abc]).isalpha() and maj == False:
            result.append(test[abc])
            maj = True
        else :
            result.append(test[abc])

    return ''.join(result)
                
# Resultat
print(upper_1of2())
