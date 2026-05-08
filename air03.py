# Exercice Coding Accelerator
# Supprimer les caractères identiques adjacents

import sys

def remove_adjacent_duplicates(input_string):
    if not input_string:
        return "error"

    if len(input_string) == 1:
        return input_string

    result = []
    prev_char = input_string[0]
    result.append(prev_char)

    for current_char in input_string[1:]:
        if current_char != prev_char:
            result.append(current_char)
            prev_char = current_char

    return ''.join(result)

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 2:
        print("error")
        sys.exit()

    output = remove_adjacent_duplicates(sys.argv[1])
    if output == "error":
        sys.exit()
    else:
        print(output)
