import numpy as np

cl = int(input('\nInforme quantas colunas e linhas terá o array: '))

array1 = np.eye(cl)
print(f'\n\033[31m{array1}\033[m')

diagonal = int(input('\nInforme a diagonal que será preenchida: '))

array2 = np.eye(4, k=diagonal)
print(f'\n\033[32m{array2}\033[m')

subs = int(input('\nInforme um valor para substituir os zeros da diagonais: '))

array2[array2 == 0] = subs
print(f'\n\033[33m{array2}\033[m')

# Verificando uma condição do array:

condicao = int(input('\nInforme um número para comparar com o valor que substituiu os zeros acima: '))

array2[array2 < subs] = condicao
print(f'\n\033[34m{array2}\033[m')

# Preenchendo linhas e colunas:

preencher = int(input('\nInforme um valor para preencher as duas últimas linhas '
                      '(vai depender de quantas colunas e linhas tem o array): '))

array2[2:] = preencher
print(f'\n\033[35m{array2}\033[m')

preencher2 = int(input('\nInforme um valor para preencher a 2 coluna '
                       '(vai depender de quantas colunas e linhas tem o array): '))

array2[:, 1] = preencher2
print(f'\n\033[36m{array2}\033[m')

preencher3 = int(input('\nInforme um valor para preencher as duas últimas linhas com as 2 primeiras colunas '
                       '(vai depender de quantas colunas e linhas tem o array): '))

array2[2:, :2] = preencher3
print(f'\n\033[37m{array2}\033[m')

# Ordenando:

print('\n\033[32mLista Ordenada\033[m')
s_array = np.sort(array2)
print(f'\n\033[97m{s_array}\033[m')

linha_coluna = int(input('\nInforme -1 se deseja ordenar pela linha ou 0 pela coluna: '))

if linha_coluna == -1:
    s_array2 = np.sort(array2, axis=linha_coluna)
    print(f'\n\033[31m{s_array2}\033[m')
elif linha_coluna == 0:
    s_array2 = np.sort(array2, axis=linha_coluna)
    print(f'\n\033[33m{s_array2}\033[m')
else:
    print('\n\033[31mNão existe esta opção...\033[m')
