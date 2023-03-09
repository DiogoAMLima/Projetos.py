from random import randint
from time import sleep

# Exemplo 1:

# Interação com o usuário para escolha de 4 números:

numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'\nVocê digitou os valores \033[31m{numeros}\033[m')  # Mostrando os valores digitados
print(f'\nO valor 2 apareceu \033[32m{numeros.count(2)}\033[m veze(s)')
# Verificando quantas vezes o valor 2 foi digitado
if 4 in numeros:
    print(f'\nO valor 4 apareceu na posição \033[33m{numeros.index(4)+1}\033[m')  # Verificando a posição do número 4
else:
    print('\nO valor 4 não foi digitado em nenhuma posição')

# Exemplo 2:

numeros_2 = (randint(1, 5), randint(1, 10), randint(1, 15), randint(1, 20))
print('\n\033[37mSORTEANDO 4 NÚMEROS, POR FAVOR AGUARDE\033[m')  # Sorteando valores
sleep(1)
print('\nOs valores sorteados foram: ', end='')
for n in numeros_2:
    print(f' \033[34m{n}\033[m ', '|', end='')  # Colocar os números na mesma linha
print(f'\n\nO maior valor sorteado foi \033[35m{max(numeros_2)}\033[m')  # Maior número
print(f'\nO menor valor sorteado foi \033[36m{min(numeros_2)}\033[m')  # Menor número

# Exemplo 3:

compras = ('Carne', 31.99,
           'Frango', 13.99,
           'Linguiça', 9.99,
           'Arroz', 19.99,
           'Feijão', 5.67,
           'Macarrão', 3.99,
           'Açúcar', 4.99,
           'Sal', 1.99)

for compra in range(0, len(compras)):  # looping de 0 até o tamanho de compras
    if compra % 2 == 0:  # Par
        print(f'{compras[compra]:.<20}', end='')  # 19 pontos entre o produto e o preço da esquerda para a direita
    else:
        print(f'R${compras[compra]:>6.2f}')  # Duas casas decimais com espaços entre o cifrão e o valor dos produtos
