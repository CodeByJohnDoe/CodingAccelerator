# Exercice Coding Accelerator
 
# Afficher le nombre N°eme de la suite de fibonacci

# Importation des modules
import sys

# Fonctionnement principal du programme
def show_fibonacci() :
    error = "erreur, merci de d'entrer un seul nombre >= 0 :)"
    if len(sys.argv) != 2 :
        print(error)
    
    arg = sys.argv[1]
    if not arg.isnumeric() : #  isnumercic prend uniquement des chiffres possitif entier
        print(error)

    wish = int(arg)
    suit_fibonacci = [0, 1, 1, 2,]
    for x in range(3, wish):
        suit_fibonacci.append(suit_fibonacci[x-2] + suit_fibonacci[x-1])
    print(suit_fibonacci[wish])    

# Resultat
show_fibonacci()
