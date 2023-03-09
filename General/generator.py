from random import randint
print('\033[31m—\033[m', '\033[32mGERADOR DE SENHA\033[m', '\033[31m—\033[m' * 18, '\n')
senha = list()
while True:  # Looping
    digito_1 = str(input('Informe o primeiro dígito da senha: ')).upper()  # Colocando o dígito em maiúsculo 
    print(f'O dígito escolhido foi: \033[31m{digito_1}\033[m')
    senha.append(digito_1)  # Adicionando o dígito a lista
    aleatorio = randint(0, 5)  # Sorteando um número entre 0 e 5
    if 0 <= aleatorio <= 5:
        senha.append(aleatorio)  # Adicionando o dígito a lista
        letra_1 = str(input('\nInforme outro dígito: '))
        print(f'O dígito escolhido foi: \033[36m{letra_1}\033[m')
        senha.append(letra_1)  # Adicionando o dígito a lista
    aleatorio_2 = randint(6, 10)  # Sorteando um número entre 6 e 10
    if 6 <= aleatorio_2 <= 10:
        senha.append(aleatorio_2)  # Adicionando o dígito a lista
        letra_2 = str(input('\nInforme mais um dígito: '))
        print(f'O dígito escolhido foi: \033[33m{letra_2}\033[m')
        senha.append(letra_2)  # Adicionando o dígito a lista
    aleatorio_3 = randint(11, 16)  # Sorteando um número entre 11 e 16
    if 11 <= aleatorio_3 <= 16:
        senha.append(aleatorio_3)  # Adicionando o dígito a lista
        letra_3 = str(input('\nInforme o último dígito da senha: '))
        print(f'O dígito escolhido foi: \033[34m{letra_3}\033[m')
        senha.append(letra_3)  # Adicionando o dígito a lista
    while True:
        res = str(input('\nQuer continuar? [S/N] ')).upper()
        if res in 'SN':
            break
        print('Responda S ou N')
    if res == 'N':
        break
print(f'A senha formada foi \033[35m{senha}\033[m')
print('\033[37m-=\033[m' * 40)
