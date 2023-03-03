def estilo_cor():
    palavra = str(input('Informe uma palavra: '))
    escolha_cor = str(input('\nEscolha uma das cores a seguir: Preto (0), Vermelho (1), Verde (2), Amarelo (3), '
                            'Azul (4), Roxo (5), Azul piscina (6) ou Cinza (7), Branco (8): '))
    escolha_estilo = str(input('\n0 = normal, 1 = negrito, 4 = sublinhado, 7 = inverter (negativo): '))
    escolha_fundo = str(input('\nPreto (40), Vermelho (41), Verde (42), Amarelo (43), Azul (44), Roxo (45), '
                              'Azul piscina (46) ou Cinza (47), Branco (107): '))
    # Opções acima referentes a cores, estilos e fundos no terminal
    # Condicionais para mostrar a cor / estilo / fundo escolhido
    if escolha_cor == '0':
        print(f'\n\033[30m{palavra}\033[m')
    elif escolha_cor == '1':
        print(f'\n\033[31m{palavra}\033[m')
    elif escolha_cor == '2':
        print(f'\n\033[32m{palavra}\033[m')
    elif escolha_cor == '3':
        print(f'\n\033[33m{palavra}\033[m')
    elif escolha_cor == '4':
        print(f'\n\033[34m{palavra}\033[m')
    elif escolha_cor == '5':
        print(f'\n\033[35m{palavra}\033[m')
    elif escolha_cor == '6':
        print(f'\n\033[36m{palavra}\033[m')
    elif escolha_cor == '7':
        print(f'\n\033[37m{palavra}\033[m')
    elif escolha_cor == '8':
        print(f'\n\033[97m{palavra}\033[m')
    else:
        print('\n\033[31mNão existe essa opção...\033[m')

    if escolha_estilo == '0':
        print(f'\n\033[0m{palavra}\033[m')
    elif escolha_estilo == '1':
        print(f'\n\033[1m{palavra}\033[m')
    elif escolha_estilo == '4':
        print(f'\n\033[4m{palavra}\033[m')
    elif escolha_estilo == '7':
        print(f'\n\033[7m{palavra}\033[m')
    else:
        print('\n\033[31mNão existe essa opção...\033[m')

    if escolha_fundo == '40':
        print(f'\n\033[40m{palavra}\033[m')
    elif escolha_fundo == '41':
        print(f'\n\033[41m{palavra}\033[m')
    elif escolha_fundo == '42':
        print(f'\n\033[42m{palavra}\033[m')
    elif escolha_fundo == '43':
        print(f'\n\033[43m{palavra}\033[m')
    elif escolha_fundo == '44':
        print(f'\n\033[44m{palavra}\033[m')
    elif escolha_fundo == '45':
        print(f'\n\033[45m{palavra}\033[m')
    elif escolha_fundo == '46':
        print(f'\n\033[46m{palavra}\033[m')
    elif escolha_fundo == '47':
        print(f'\n\033[47m{palavra}\033[m')
    elif escolha_fundo == '107':
        print(f'\n\033[107m{palavra}\033[m')
    else:
        print('\n\033[31mNão existe essa opção...\033[m')


estilo_cor()
