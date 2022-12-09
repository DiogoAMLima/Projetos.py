import random
import time

ele_1 = int(input('Informe o primeiro elemento da matriz: [0, 0] '))
ele_2 = int(input('Informe o segundo elemento da matriz: [0, 1] '))
ele_3 = int(input('Informe o terceiro elemento da matriz: [1, 0] '))
ele_4 = int(input('Informe o quarto elemento da matriz: [1, 1] '))

matriz = [ele_1, ele_2, ele_3, ele_4]

print(f'[0, 0] = \033[31m{ele_1}\033[m [0, 1] = \033[32m{ele_2}\033[m \n'
      f'[1, 0] = \033[33m{ele_3}\033[m [1, 1] = \033[34m{ele_4}\033[m')

print(f'Estamos sorteando um elemento da matriz: \033[35m{matriz}\033[m por favor, aguarde...')

time.sleep(0.8)

elemento_sortido = random.choice(matriz)
print(f'\nO elemento escolhido foi: \033[97m{elemento_sortido}\033[m')
