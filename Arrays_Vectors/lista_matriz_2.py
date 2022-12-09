matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
simpar = scol = matrizv2 = 0
# Definindo a matriz:
for lin in range(0, 4):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para \033[33m[{lin},\033[m \033[36m{col}]:\033[m '))

# Soma dos valores ímpares:
for lin in range(0, 4):
    for col in range(0, 3):
        print(f'\033[33m[{matriz[lin][col]:^5}]\033[m', end='')
        if matriz[lin][col] % 2 == 1:
            simpar += matriz[lin][col]
    print()
print(f'A soma dos valores ímpares é: \033[97m{simpar}\033[m')

# Soma da 4 coluna:
for lin in range(0, 4):
    scol += matriz[lin][2]
print(f'A soma dos valores da quarta coluna é: \033[35m{scol}\033[m')

# Soma de todos os valores vezes 2:
for lin in range(0, 4):
    for col in range(0, 3):
        matrizv2 += matriz[lin][col] * 2
print(f'A soma de todos os valores multiplicados por 2 é: \033[34m{matrizv2}\033[m', end='')


# Multiplicando os valores de cada elemento:
for lin in range(0, 4):
    for col in range(0, 3):
        matriz2[lin][col] = int(input(f'Digite um valor para \033[33m[{lin},\033[m \033[36m{col}]:\033[m '))

mult = float(input('\nInforme um número para multiplicar os elementos da matriz: '))

for lin in range(0, 4):
    for col in range(0, 3):
        print(f'\033[33m[{matriz2[lin][col]*mult:.1f}]\033[m ', end='')
