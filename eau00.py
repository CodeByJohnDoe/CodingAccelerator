# Exercice Coding Accelerator
 
# Afficher dans l'odre croissant les différentes combinaisons possibles de 3 chiffres 

# Importation des modules
import sys

# Fonctionnement principal du programme
def combinaissons_de3chiffres() :
    if len(sys.argv) == 1:
        result =[]
        compare_list = []
        compare_number = []
        a = 0
        b = 0
        c = 0
        for a in range(0, 10):
            for b in range(0, 10):
                for c in range(0, 10):
                    
                    # Règle de combinaison
                    if a != b and a != c and b!= c : 
                        compare_list = sorted(result)   
                        compare_number = ''.join(sorted(f"{a}{b}{c}"))
                        if compare_number not in compare_list:
                            result.append(f"{a}{b}{c}")

        print(', '.join(result))                 

# Resultat
combinaissons_de3chiffres()
