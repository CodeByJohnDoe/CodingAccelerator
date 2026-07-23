# air00.py
import sys

def tollbox_split(string_to_cut, separator=None):
    """
    Découpe une chaîne de caractères selon un séparateur donné.

    Args:
        string_to_cut (str): La chaîne à découper
        separator (str, optional): Le séparateur à utiliser. Par défaut utilise les espaces, tabulations et sauts de ligne.

    Returns:
        list: Liste des mots découpés
    """
    # Gestion du cas chaîne vide
    if not string_to_cut:
        return []

    # Définition des séparateurs par défaut (espace, tabulation, saut de ligne)
    if separator is None:
        separators = " \t\n"
    else:
        separators = separator

    splited = []  # Liste pour stocker les mots découpés
    start = 0     # Position de début du mot courant

    # Parcours de chaque caractère de la chaîne
    for i, char in enumerate(string_to_cut):
        # Si le caractère est un séparateur
        if char in separators:
            # Si on a trouvé un mot entre start et i
            if i > start:
                splited.append(string_to_cut[start:i])
            # On déplace le marqueur après le séparateur
            start = i + 1

    # Ajout du dernier mot s'il reste quelque chose
    if start < len(string_to_cut):
        splited.append(string_to_cut[start:])

    return splited

if __name__ == "__main__":
    # Vérification des arguments en ligne de commande
    if len(sys.argv) < 2:
        print("error", file=sys.stderr)
        sys.exit(1)

    # Récupération du séparateur (2ème argument optionnel)
    separator = sys.argv[2] if len(sys.argv) > 2 else None

    # Exécution du découpage
    result = tollbox_split(sys.argv[1], separator)

    # Affichage des résultats (un mot par ligne)
    for word in result:
        print(word)