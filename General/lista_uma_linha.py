lista = [linha.strip() for linha in open("lista.txt", "r")]

print(f'\033[31m{lista}\033[m')
