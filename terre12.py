# Exercice Coding Accelerator
 
# Résultat de passage de l'heure AM/PM en 24H

# Importation des modules
import sys



# Fonctionnement principal du programme
def adapthour():
    error = "erreur, veuillez entrer une heure avec le format HH:mmAM ou HH:mmPM. Ex: 09:05AM ou 09:05PM."
    argv_count = len(sys.argv) - 1 
    
    # Sécurité : vérifier si l'argument existe avant d'y accéder
    if argv_count != 1:
        print(error)
        return

    input = sys.argv[1]
    check_separator = input.find(":")
    check_AM = input.find('AM')
    check_PM = input.find('PM')
   
    # Vérification du format de base de l heure
    if check_separator == 2 and (check_AM == 5 or check_PM == 5):
        HH_str, input_scrap = input.split(":", 1)
        # Vérification du format de base de la tranche horaire
        if check_AM == 5 : 
            MM_str = input_scrap.split("AM")[0]
            indicator = 'AM'
        else :
            MM_str = input_scrap.split("PM")[0]
            indicator = 'PM'

        # Vérification que ce sont bien des chiffres et que la longueur est bonne
        if len(HH_str) == 2 and HH_str.isnumeric() and len(MM_str) == 2 and MM_str.isnumeric():
            HH = int(HH_str)
            MM = int(MM_str)

            # Vérfificaytion des plages d'heures réelles
            if not (0 <= HH <= 12 and 0 <= MM <= 59):
                print(error)
                return

            # Application de la conversion
            if HH == 12 and indicator == "AM":
                HH = 0
            elif HH == 12 and indicator == "PM":
                HH = 12
            else:
                HH = HH + 12

            # Affichage formaté :02d pour garder le zéro devant (ex: 09:05)
            print(f"{HH:02d}:{MM:02d}")
        else:
            print(error)
    else :
        print(error)

# Resultat
adapthour()