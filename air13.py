# Exercice Coding Accelerator
# Test_unitaire
import subprocess
import json
import sys
def run_tests():
    print_coding_accelerator()
    """
    Exécute les tests unitaires définis dans le fichier JSON.
    Gère plusieurs exercices (air00, air01, etc.) avec leurs tests respectifs.
    """
    try:
        # Chargement du fichier de tests
        with open('airunitaire.json', 'r', encoding='utf-8') as f:
            tests = json.load(f)
    except FileNotFoundError:
        print("Erreur : fichier airunitaire.json introuvable", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Erreur : fichier JSON invalide", file=sys.stderr)
        sys.exit(1)

    # Initialisation des compteurs
    total_tests = 0
    total_success = 0

    # Parcours de chaque groupe de tests 
    for test_group in tests:
        # Surlignement jaune pour le nom de l'exercice
        print(f"\n📝 \033[93mExercice : {test_group['name']}\033[0m")

        # Exécution de chaque test individuel
        for i, test in enumerate(test_group['tests'], 1):
            # Construction de la commande à exécuter
            cmd = ["python", f"{test_group['name']}.py"]
            # Gestion spécifique selon l'exercice
            if test_group['name'] in ['air00', 'air01','air04']:
                cmd.extend(test['input'][:2])  # Ajouter avec les 2 premiers éléments (ou moins)
            elif test_group['name'] in ['air02', 'air03','air05','air06','air07']:
                # Le dernier élément est le séparateur
                cmd.extend(test['input'][:-1])
                if test['input'][-1]:  # Si séparateur n'est pas vide
                    cmd.append(test['input'][-1])

            # Exécution de la commande et capture de la sortie
            result = subprocess.run(cmd, capture_output=True, text=True)

            # Traitement de la sortie (séparation par lignes et suppression des espaces vides)
            actual = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]

            # Incrémentation du compteur total de tests
            total_tests += 1

            # Comparaison avec le résultat attendu
            if actual == test['expected']:
                print(f"   - Test {i}/{len(test_group['tests'])} : ✅ \033[92mSucess\033[0m")
                total_success += 1
            else:
                print(f"  Test {i}/{len(test_group['tests'])} : ❌ \033[91mFailure\033[0m")
                print(f"    Entrée    : {test['input']}")
                print(f"    Attendu   : {test['expected']}")
                print(f"    Reçu      : {actual}")

    # Affichage du cumul final en rouge
    print(f"\n🎯 \033[94mTotal succès : {total_success}/{total_tests}\033[0m")
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

if __name__ == "__main__":
    run_tests()