phrase = "MessiIsChampionsOfTheWorld"
phrase = [i for i in phrase]  # Separando as letras
print(f'\033[31m{phrase}\033[m')
phrase = "".join([i for i in phrase])
print(f'\n\033[32m{phrase}\033[m')  # Sem espaço entre as letras
phrase = " ".join([i for i in phrase])
print(f'\n\033[33m{phrase}\033[m')  # Espaço entre as letras
