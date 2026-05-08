import sys

def afficher_escalier(char, etages):
    try:
        etages = int(etages)
        if etages <= 0:
            return "error"
    except ValueError:
        return "error"

    escalier = []
    for i in range(1, etages + 1):
        espaces = " " * (etages - i)
        caracteres = char * (2 * i - 1)
        escalier.append(espaces + caracteres)

    return "\n".join(escalier)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("error")
        sys.exit()

    char = sys.argv[1]
    etages = sys.argv[2]

    if len(char) != 1:
        print("error")
        sys.exit()

    resultat = afficher_escalier(char, etages)
    if resultat == "error":
        print("error")
        sys.exit()
    else:
        print(resultat)
