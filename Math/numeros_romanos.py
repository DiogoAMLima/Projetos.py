print('\033[37m——————————————————————————— NÚMEROS ROMANOS ———————————————————————————\033[m\n')
print('Lista de números: \033[33m1, 5, 10, 20, 50, 100, 500, 1000\033[m')
numeros = [1, 5, 10, 20, 50, 100, 500, 1000]
numeros_rom = ['I', 'V', 'X', 'XX', 'L', 'C', 'D', 'M']  # Lista com os números romanos
while True:  # Looping
    num = int(input('\nInforme um número que esteja na lista mostrada acima: '))
    if num in numeros:  # Verificando se o número escolhido está na lista, se estiver, 
        # será mostrado o número romano correspondente de acordo com a lista de números romanos
        if num == 1:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[0]}\033[m\n')
        elif num == 5:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[1]}\033[m\n')
        elif num == 10:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[2]}\033[m\n')
        elif num == 20:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[3]}\033[m\n')
        elif num == 50:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[4]}\033[m\n')
        elif num == 100:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[5]}\033[m\n')
        elif num == 500:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[6]}\033[m\n')
        elif num == 1000:
            print(f'\nO \033[32m{num}\033[m em números romanos é: \033[35m{numeros_rom[7]}\033[m\n')
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            if resp in 'SN':
                break
            print('\nResponda apenas \033[31mS ou N:\033[m\n')
        if resp == 'N':
            print('\nATÉ A PRÓXIMA')
            break
    else:
        print('\n\033[31mErro, digite um número que esteja nesta lista: 1, 5, 10, 20, 50, 100, 500, 1000\033[m')

# numeros_rom[0] -> mostrando o valor da primeira posição da lista de números romanos
# numeros_rom[1] -> mostrando o valor da segunda posição da lista de números romanos
# E assim continua...
