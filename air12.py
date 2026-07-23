import subprocess
import json
import sys

def run_tests():
    """
    Exécute les tests unitaires définis dans le fichier JSON.
    Compare les résultats obtenus avec les résultats attendus.
    """
    try:
        # Chargement du fichier de tests
        with open('airunitaire.json', 'r') as f:
            tests = json.load(f)
    except FileNotFoundError:
        print("Erreur : fichier airunitaire.json introuvable", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Erreur : fichier JSON invalide", file=sys.stderr)
        sys.exit(1)

    # Parcours de chaque groupe de tests
    for test_group in tests:
        print(f"\nExercice : {test_group['name']}")

        # Exécution de chaque test individuel
        for i, test in enumerate(test_group['tests'], 1):
            # Construction de la commande à exécuter
            cmd = ["python", f"{test_group['name']}.py", test['input']]
            if 'separator' in test:
                cmd.append(test['separator'])

            # Exécution de la commande et capture de la sortie
            result = subprocess.run(cmd, capture_output=True, text=True)

            # Traitement de la sortie (séparation par lignes et suppression des espaces vides)
            actual = [line.strip() for line in result.stdout.strip().split('\n') if line.strip()]

            # Comparaison avec le résultat attendu
            if actual == test['expected']:
                print(f"Test {i}/{len(test_group['tests'])} : success")
            else:
                print(f"Test {i}/{len(test_group['tests'])} : failure")
                print(f"  Attendu : {test['expected']}")
                print(f"  Reçu : {actual}")

if __name__ == "__main__":
    run_tests()