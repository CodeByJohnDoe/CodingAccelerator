# Exercice Coding Accelerator
 
# Afficher tout les combinaisons de deux nombre entre 00 et 99 dans l'ordre croissant

# Importation des modules
import sys

# Fonctionnement principal du programme
def show_00to99() :
    if len(sys.argv) == 1:
        result =[]
        compare_list = []
        for a in range(100):
            for b in range(a + 1, 100):

                # Règle de combinaison
                if a != b and (a  not in compare_list and b not in compare_list): 
                    result.append(f"{a:02}" " " f"{b:02}")

    print(', '.join(result))                 


# Resultat
show_00to99()
