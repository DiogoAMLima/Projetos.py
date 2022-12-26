import numpy as np
from rich import print as print

print('[red]-=-[/]' * 15, '[blue]MATRIZES[/]', '[red]-=-[/]' * 15, '\n')

matriz_1 = np.array([[3, 3],
                     [7, 6]])
print(f'A primeira matriz é:\n [purple]{matriz_1}[/]')

matriz_2 = np.array([[2, 2],
                     [3, 3]])
print(f'\nA segunda matriz é:\n [yellow]{matriz_2}[/]')

matriz_3 = matriz_1 * matriz_2
print(f'\nA multiplicação da primeira com a segunda matriz é: \n [green]{matriz_3}[/]')

print('[black]-=-[/]' * 33)
