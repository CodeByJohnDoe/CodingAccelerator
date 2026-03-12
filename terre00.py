# Exercice Coding Accelerator
 
# Afficher l'alaphabet en lettre en minuscule suivie d'un retour à la ligne

# Set up des variables
result = []

# Set up des constantes
a = ord("a")
b = a + 26

# Fonctionnement du programme
for x in range(a,b) :
    result.append(chr(x))

# Affichage du résultat
print(''.join(result))