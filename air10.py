import sys

def afficher_pyramide(char, etages):
    try:
        etages = int(etages)
        if etages <= 0:
            return "error"
    except ValueError:
        return "error"

    pyramide = []
    for i in range(1, etages + 1):
        espaces = " " * (etages - i)
        caracteres = char * (2 * i - 1)
        pyramide.append(espaces + caracteres)

    return "\n".join(pyramide)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("error")
        sys.exit()

    char = sys.argv[1]
    etages = sys.argv[2]

    if len(char) != 1:
        print("error")
        sys.exit()

    resultat = afficher_pyramide(char, etages)
    if resultat == "error":
        print("error")
        sys.exit()
    else:
        print(resultat)