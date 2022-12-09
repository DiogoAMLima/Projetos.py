def estilo_cor():
    palavra = str(input('Informe uma palavra: '))
    escolha_cor = str(input('Escolha uma das cores a seguir: Preto (0), Vermelho (1), Verde (2), Amarelo (3), '
                            'Azul (4), Roxo (5), Azul piscina (6) ou Cinza (7), Branco (8): '))
    escolha_estilo = str(input('0 = normal, 1 = negrito, 4 = sublinhado e 7 = inverter (negativo)'))
    escolha_fundo = str(input('Preto (40), Vermelho (41), Verde (42), Amarelo (43), Azul (44), Roxo (45), '
                              'Azul piscina (46) ou Cinza (47), Branco (107):'))
    if escolha_cor == '0':
        print(f'\033[30m{palavra}\033[m')
    elif escolha_cor == '1':
        print(f'\033[31m{palavra}\033[m')
    elif escolha_cor == '2':
        print(f'\033[32m{palavra}\033[m')
    elif escolha_cor == '3':
        print(f'\033[33m{palavra}\033[m')
    elif escolha_cor == '4':
        print(f'\033[34m{palavra}\033[m')
    elif escolha_cor == '5':
        print(f'\033[35m{palavra}\033[m')
    elif escolha_cor == '6':
        print(f'\033[36m{palavra}\033[m')
    elif escolha_cor == '7':
        print(f'\033[37m{palavra}\033[m')
    elif escolha_cor == '8':
        print(f'\033[97m{palavra}\033[m')
    else:
        print('\033[31mNão existe essa opção...\033[m')


estilo_cor()

# Código não finalizado
