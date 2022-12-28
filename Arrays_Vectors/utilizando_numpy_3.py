import numpy as np

# Preenchendo valores:

preencher = int(input('Informe o valor para preencher o array: '))

a = np.zeros((4, 4))

a.fill(preencher)

print(f'\n\033[31m{a}\033[m')

# Somando valores:

a += 3

print(f'\n\033[32m{a}\033[m')

# Subtraindo valores:

a -= 2

print(f'\n\033[33m{a}\033[m')

# Método sum:

soma = a.sum()

print(f'\nA soma de todos os elementos do array a é: \033[34m{soma}\033[m')

b = np.zeros((4, 4))

b.fill(3)  # Preenchendo com 3

soma_linha = b.sum(axis=0)
soma_coluna = b.sum(axis=1)

print(f'\n\033[35m{soma_linha}\033[m \n\033[36m{soma_coluna}\033[m')

a_prod = a.prod()  # Elevando o elemento pela quantidade de elementos

print(f'\n\033[37mValor do elemento elevado ao quanitdade de elementos: {a_prod:.2f}\033[m')

c = np.eye(4, k=-1) * 7

print(f'\n\033[97m{c}\033[m')

valor = int(input('\nInforme um valor: '))

condicao = int(input('\nInforme outro valor: '))

c[c < valor] = condicao
print(f'\n\033[34m{c}\033[m')

average = c.mean()  # Média

print(f'\n\033[30mA média é: {average:.2f}\033[m')

# Repetindo valores:

repetir = int(input('\nInforme um número: '))
qntd = int(input('\nInforme quantas vezes o númeor se repetirá: '))

d = np.repeat(repetir, qntd)

print(f'\nO número {repetir} repetido {qntd} vezes no array é igual a: \033[31m{d}\033[m')

e = np.array([[1, 2],
              [3, 4]])

troca = np.swapaxes(e, 0, 1)

print(f'Realizando a troca temos: \n\033[32m{troca}\033[m')

f = np.array([[1, 5],
              [6, 9]])

# Operações:

soma_array = e + f

sub_array = e - f

print(f'\nSoma de da matriz e com a f resulta em:\n\033[33m{soma_array}\033[m \n'
      f'e a subtração entre e e f resulta em:\n\033[35m{sub_array}\033[m')

resto_div = f % e

print(f'\nModulo de f % e é igual a: \n\033[34m{resto_div}\033[m')

operacao = ((e / 2) - f + 2 * e)

print(f'\n\033[97m{operacao}\033[m')
