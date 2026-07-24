# Exercice Coding Accelerator
 
# Célébration de la fin de l'eau

# Importation des modules
import sys

# Fonctionnement principal du programme
def terre_celebration() :
    if len(sys.argv) == 1:
        print("J'ai termé l'Epreuve de l'Eau et c'était prise de tête mais bon j'ai quand même réussi !")
    print_coding_accelerator()

# Coding Accelerator
def print_coding_accelerator():
    coding_accelerator = r"""
 _____           _ _                  ___               _                _
/  __ \         | (_)                / _ \             | |              | |
| /  \/ ___   __| |_ _ __   __ _    / /_\ \ ___ ___ ___| | ___ _ __ __ _| |_ ___  _ __
| |    / _ \ / _` | | '_ \ / _` |   |  _  |/ __/ __/ _ \ |/ _ \ '__/ _` | __/ _ \| '__|
| \__/\ (_) | (_| | | | | | (_| |   | | | | (_| (_|  __/ |  __/ | | (_| | || (_) | |
\____/\___/ \__, _|_|_| |_|\__, |   \_| |_/\___\___\___|_|\___|_|  \__,_|\__\___/|_|
                            __/ |
                           |___/
"""
    print("\033[1;33m" + coding_accelerator + "\033[0m")

# Resultat
terre_celebration()
