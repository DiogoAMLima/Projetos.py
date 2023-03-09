import random

lista = []  # Declarando a lista

alcance = int(input('Informe quantos números terão na lista: '))
print()

for i in range(0, alcance):  # Looping de 0 até o número determinado
    num = float(input(f'Informe um número na posição {i}: '))
    lista.append(num)  # Adicionando o número a lista

print(f'\nNúmeros escolhidos: \033[31m{lista}\033[m')  # Lista final

print(f'\nNúmero sorteado: \033[36m{random.choice(lista)}\033[m')  # Sorteando um número da lista final
