# Exercice Coding Accelerator

# Séparer une chaîne de caractères avec espaces, tabulations et retours à la ligne comme séparateurs

import sys

def tollbox_split(string_to_cut, string_separator=None): # Set up en None si vide
    # Si la chaîne est vide
    if not string_to_cut:
        return "error"

    splited = []
    marker = 0
    separators = " \t\n"  # Espace, tabulation, retour à la ligne

    for i in range(len(string_to_cut)):
        # Si le caractère est un séparateur
        if string_to_cut[i] in separators:
            # Si on a un mot entre marker et i
            if i > marker:
                splited.append(string_to_cut[marker:i])
            marker = i + 1

    # Ajout du dernier mot
    if marker < len(string_to_cut):
        splited.append(string_to_cut[marker:])

    return splited

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

    reponse = tollbox_split(sys.argv[1])
    if reponse == "error":
        sys.exit()
    else:
        for mot in reponse:
            print(mot)
