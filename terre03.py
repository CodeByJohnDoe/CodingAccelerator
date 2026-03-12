# Exercice Coding Accelerator
 
# Afficher l'alaphabet en lettre en minuscule en débutantd'une lettre suivie d'un retour à la ligne

# Importation des modules
import sys

# Set up des variables
result = []

# Set up des constantes
start = ord(sys.argv[1])
z = ord("z")

# Fonctionnement du programme
for x in range(start,z) :
    result.append(chr(x))

# Affichage du résultat
print(''.join(result))