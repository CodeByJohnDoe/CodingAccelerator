# Exercice Coding Accelerator
# Test unitaire pour les exercices

import sys
import os
import json
import subprocess # terninal interne

def test_unitaire():
    """Exécute les tests unitaires pour chaque exercice."""
    # Vérification que le fichier de test existe
    nom_fichier = "airunitaire.json"
    try:
        with open(nom_fichier, 'r', encoding="utf-8") as fichier:
            list_unitaire = json.load(fichier)
    except PermissionError:
        print("error: permission refusée")
        sys.exit(1)
    except FileNotFoundError:
        print("error: fichier introuvable")
        sys.exit(1)
    except json.JSONDecodeError:
        print("error: fichier JSON invalide")
        sys.exit(1)

    # Exécuter les tests pour chaque groupe d'exercices
    for test_group in list_unitaire:
        for i, test in enumerate(test_group['tests'], 1):
            exercise_name   = test_group['name']
            input_args      = test      ['input'].split()  # Convertit la chaîne en arguments
            print(input_args)
            expected_output = test      ['expected']
            print(expected_output)

            try:
                # Exécuter l'exercice Python correspondant
                result = subprocess.run(
                    ["python", f"{exercise_name}.py"] + input_args,
                    capture_output=True,
                    text=True,
                    check=True
                )

                # Comparer la sortie réelle avec la sortie attendue
                actual_output = result.stdout.strip()

                # Gestion du cas où l'exercice retourne une liste
                if actual_output.startswith('[') and actual_output.endswith(']'):
                    actual_output = eval(actual_output)  # Convertit la chaîne de liste en liste Python

                # Si c'est une liste, on la convertit en chaîne pour comparaison
                if isinstance(actual_output, list):
                    actual_output = '\n'.join(actual_output)
                if isinstance(expected_output, list):
                    expected_output = '\n'.join(expected_output)

                if actual_output == expected_output.strip():
                    print(f"{exercise_name} ({i}/{len(test_group['tests'])}): success")
                else:
                    print(f"{exercise_name} ({i}/{len(test_group['tests'])}): failure")

            except subprocess.CalledProcessError as e:
                print(f"{exercise_name} ({i}/{len(test_group['tests'])}): failure")
            except FileNotFoundError:
                print(f"{exercise_name} ({i}/{len(test_group['tests'])}): failure")

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 1:
        print("error: trop d'arguments")
        sys.exit(1)

    test_unitaire()