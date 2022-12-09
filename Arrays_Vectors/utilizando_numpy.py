import numpy as np

matriz = np.array([[0, 0, 0], [1, 2, 3], [4, 5, 6]])
# print(matriz)

col = 0
lin = 0

# Quantidade de Linhas e Colunas:
print(f'A quantidade de elementos do array é: \033[33m{matriz.shape}\033[m')

# Números de elementos de um array:
print(f'\nA quantidade de elementos do array é: \033[32m{matriz.size}\033[m\n')

# Visualizando as colunas do array:

for i in range(3):
    print(f'\033[34mColuna {i}:\033[m ', f'\033[31m{matriz[:, col]}\033[m')
    col += 1

print()

# Visualizando as linhas do array:

for i in range(3):
    print(f'\033[35mLinha {i}:\033[m ', f'\033[36m{matriz[lin, :]}\033[m')
    lin += 1


# Números ímpares ou pares em um array:

while True:
    try:
        op = str(input('Informe se deseja ver um array com números pares ou ímpares: [P/I]? ')).strip().upper()
        if 'P' in op:
            array_pares = np.array([num for num in range(0, 51, 2)])
            print(array_pares)
        elif 'I' in op:
            array_impares = np.array([num for num in range(1, 51, 2)])
            print(array_impares)
        else:
            print('\n\033[31mNão existe essa opção...\033[m')
            break
    except (TypeError, ValueError):
        print('\n\033[31mNão existe essa opção...\033[m')
        break
