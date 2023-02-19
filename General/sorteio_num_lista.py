import random

lista = []

alcance = int(input('Informe quantos números terão na lista: '))
print()

for i in range(0, alcance):
    num = float(input(f'Informe um número na posição {i}: '))
    lista.append(num)

print(f'\nNúmeros escolhidos: \033[31m{lista}\033[m')

print(f'\nNúmero sorteado: \033[36m{random.choice(lista)}\033[m')
