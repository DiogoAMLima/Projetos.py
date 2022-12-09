import numpy as np

# v = [1, 2, 4]
# v2 = [2, 1, 4]
#
# resultado = np.dot(v, v2)
# print(resultado)

# No exemplo acima temos = (1 * 2) + (2 * 1) + (4 * 4) = 20

# Interação com o(a) usuário(a):

v = []
v2 = []

qntd = int(input('Informe a quantidade de valores que terá nas listas: '))

i = 0

for i in range(qntd):
    values = int(input('\nInforme o valor a ser adicionado na lista v: '))
    v.append(values)
    values2 = int(input('Informe o valor a ser adicionado na lista v2: '))
    v2.append(values2)

resultado = np.dot(v, v2)
print(f'\nO resultado é: \033[35m{resultado}\033[m')
