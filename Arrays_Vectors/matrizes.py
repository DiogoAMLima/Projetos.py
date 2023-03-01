import numpy as np

# Título com cor e espaçamento

print('\033[32m-=-\033[m' * 15, '\033[31mMATRIZES\033[m', '\033[32m-=-\033[m' * 15, '\n')

# Definindo a matriz 1:

matriz_1 = np.array([[3, 3],
                     [7, 6]])
print(f'A primeira matriz é:\n \033[33m{matriz_1}\033[m')

# Definindo a matriz 2:

matriz_2 = np.array([[2, 2],
                     [3, 3]])
print(f'\nA segunda matriz é:\n \033[34m{matriz_2}\033[m')

matriz_3 = matriz_1 * matriz_2  # multiplicação da primeira com a segunda matriz
print(f'\nA multiplicação da primeira com a segunda matriz é: \n \033[35m{matriz_3}\033[m\n')

print('\033[36m-=-\033[m' * 33)
