lista1 = [8]  # Criando uma lista com tamanho 8

lista1[0] = 1  # Armazenando o valor 1 na posição 0

print(f'\033[34mValor da posição 0: {lista1[0]}\033[m')  # Verificando o valor da pósição 0

valor = int(input('\nInforme um valor: '))

lista1.append(valor)  # Adicionando um valor

print(f'\n\033[33m{valor}\033[m adicionando a lista')

print(f'\nVerificando o último valor da lista: \033[32m{lista1[-1]}\033[m')

# Adicionando dois valores na lista

lista1.append(7)
lista1.append(10)

print(f'\nLista completa: \033[36m{lista1}\033[m')
print(f'\nAcessando períoda determinado da lista: \033[35m{lista1[1:4]}\033[m')  # Vai da posição 1 a 3

esc = int(input('\nInforme uma posição que deseja remover da lista: '))
del lista1[esc]  # Deletando um valor da lista a partir de uma posição
print(f'\nLista completa: \033[37m{lista1}\033[m')

# Método extend
y = [22, 21]
lista1.extend(y)
print(f'\nAdicionando \033[31m{y}\033[m na lista: \033[31m{lista1}\033[m')

# Método pop
lista2 = ['Luffy', 'Goku', 'Naruto', 'dog']
print(f'\nLista2: \033[33m{lista2}\033[m')
lista2.pop(3)
print(f'\nRemovendo o último item da lista: \033[32m{lista2}\033[m')

esc2 = int(input('\nInforme o valor que deseja remover da lista: '))
lista1.remove(esc2)  # Será removido o 1° item na qual o valor é esc2

# Ordenando os valores da lista:
lista1.sort()
print(f'\nLista1 ordenada: \033[97m{lista1}\033[m')

# Método clear
lista1.clear()  # Remove todos os elementos da lista
print(f'\nRemovendo todos os elementos da Lista1: \033[34m{lista1}\033[m')
