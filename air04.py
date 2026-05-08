# Exercice Coding Accelerator
# Opérations sur une liste d'entiers

import sys

def apply_operation(numbers, operation):
    # Vérification des entrées
    if not numbers or not operation:
        return "error"

    # Vérification que l'opération commence par + ou -
    if not (operation.startswith('+') or operation.startswith('-')):
        return "error"

    try:
        op_value = int(operation[1:])
    except ValueError:
        return "error"

    result = []
    for num in numbers:
        try:
            n = int(num)
        except ValueError:
            return "error"

        if operation.startswith('+'):
            result.append(str(n + op_value))
        else:
            result.append(str(n - op_value))

    return ' '.join(result)

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 3:
        print("error")
        sys.exit()

    # Séparation des nombres et de l'opération
    numbers = sys.argv[1:-1]
    operation = sys.argv[-1]

    output = apply_operation(numbers, operation)
    if output == "error":
        print("error")
        sys.exit()
    else:
        print(output)
