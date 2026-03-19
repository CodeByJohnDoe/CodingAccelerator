# Exercice Coding Accelerator
 
# Résultat de passage de l'heure 24H en Am/PM

# Importation des modules
import sys

# Fonctionnement principal du programme
def adapthour():
    error = "erreur, veuillez entrer une heure avec le format HH:MM."
    argv_count = len(sys.argv) - 1 
    
    # Sécurité : vérifier si l'argument existe avant d'y accéder
    if argv_count != 1:
        print(error)
        return

    entree = sys.argv[1]
    check_separator = entree.find(":")
    
    # Vérification du format de base
    if check_separator != -1:
        HH_str, MM_str = entree.split(":", 1)
        indicator = 'AM'
    
        # Vérification que ce sont bien des chiffres et que la longueur est bonne
        if len(HH_str) == 2 and HH_str.isnumeric() and len(MM_str) == 2 and MM_str.isnumeric():
            HH = int(HH_str)
            MM = int(MM_str)
            
            # Vérfificaytion des plages d'heures réelles
            if not (0 <= HH <= 23 and 0 <= MM <= 59):
                print(error)
                return

            # Application de la conversion
            if HH == 0:
                HH = 12
                indicator = "AM"
            elif HH == 12:
                indicator = "PM"
            elif HH > 12:
                HH = HH - 12
                indicator = "PM"
            else:
                indicator = "AM"

            # Affichage formaté :02d pour garder le zéro devant (ex: 09:05)
            print(f"{HH:02d}:{MM:02d} {indicator}")
        else:
            print(error)
    else :
        print(error)

# Resultat
adapthour()