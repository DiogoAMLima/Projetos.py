# Função para converter binário, octal, hexadecimal para decimal

def num_bin_octal_hex():
    b = str(input('Digite um número em binário: 0 ou 1 '))
    o = str(input('Digite um número em octal: '))
    h = str(input('Digite um número em hexadecimal: '))
    print(f'\nO valor digitado em binário \033[31m{b}\033[m, em octal \033[32m{o}\033[m '
          f'e em hexadecimal \033[33m{h}\033[m são respectivamente em decimal: '
          f'\033[34m{format(int(b, 2))}\033[m, \033[35m{format(int(o, 8))}\033[m e \033[36m{format(int(h, 16))}\033[m')


num_bin_octal_hex()
