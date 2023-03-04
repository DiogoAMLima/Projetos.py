def sacar_dinheiro():  # Inicializando a função
    print('Células disponíveis para saque: \033[97m50, 20, 10, 5, 2, 1\033[m\n')
    print('\033[31m-=\033[m' * 20)
    valor_saque = int(input('\nInforme o valor do saque: '))
    total = valor_saque
    ced = 50
    total_ced = 0
    while True:  # Loop
        # Condicional para verificação das cédulas que serão utilizadas, diminuimos o número da variável total para que
        # possa ser utilizado outro valor da cédula
        if total >= ced:
            total -= ced
            total_ced += 1
        else:
            if total_ced > 0:
                print(f'\nTotal de \033[34m{total_ced}\033[m cédula(s) de \033[35m{ced}\033[m')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            elif ced == 2:
                ced = 1
            total_ced = 0
            if total == 0:
                break
    print()
    print('\033[31m-=\033[m' * 20)


sacar_dinheiro()
