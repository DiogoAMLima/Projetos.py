import random
import time
import emoji

# Definindo os valores:

ele_1 = int(input('Informe o primeiro elemento da matriz: [0, 0] '))
ele_2 = int(input('Informe o segundo elemento da matriz:  [0, 1] '))
ele_3 = int(input('Informe o terceiro elemento da matriz: [1, 0] '))
ele_4 = int(input('Informe o quarto elemento da matriz:   [1, 1] '))

matriz = [ele_1, ele_2, ele_3, ele_4]

print(f'[0, 0] = \033[31m{ele_1}\033[m [0, 1] = \033[32m{ele_2}\033[m \n'
      f'[1, 0] = \033[33m{ele_3}\033[m [1, 1] = \033[34m{ele_4}\033[m')

print(f'Estamos sorteando um elemento da matriz: \033[35m{matriz}\033[m por favor, aguarde...')

time.sleep(0.8)

elemento_sortido = random.choice(matriz)  # Sorteando e escolhendo um elemento da matriz

# Tentando adivinhar o valor sorteado:

op = int(input('\nInforme o número que acha que foi sorteado: '))

# Fazendo a comparação com o valor escoliho e o valor sorteado:

if op == elemento_sortido:
    print(emoji.emojize('\n\033[34mParabéns! :full_moon_face:\033[m'))  # entre :: está o código do emoji
    print(f'\nO elemento escolhido foi: \033[97m{elemento_sortido}\033[m')
else:
    print(emoji.emojize('\n\033[36mQue pena! :disappointed_face:\033[m'))  # entre :: está o código do emoji
    print(f'\nO elemento escolhido foi: \033[97m{elemento_sortido}\033[m')
