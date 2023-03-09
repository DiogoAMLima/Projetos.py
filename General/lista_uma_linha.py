lista = [linha.strip() for linha in open("lista.txt", "r")]
# Separando cada linha que estiver dentro do arquivo lista.txt
# "r" é de read, para ler o arquivo

print(f'\033[31m{lista}\033[m')

