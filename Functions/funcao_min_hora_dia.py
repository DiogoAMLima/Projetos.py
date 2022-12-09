def tempo():
    try:
        seg = float(input('Informe o valor em segundos: '))

        min = seg / 60
        print(f'\nO número digitado \033[32m{seg:.0f}\033[m corresponde a \033[33m{min:.2f} minuto(s)\033[m')
        hora = seg / 3600
        print(f'\nO número digitado \033[32m{seg:.0f}\033[m corresponde a \033[34m{hora:.2f} hora(s)\033[m')
        dia = seg / (24 * 60 * 60)  # O dia possui 24 horas, 1 hora possui 60 minutos e 1 minuto possui 60 segundos
        print(f'\nO número digitado \033[32m{seg:.0f}\033[m corresponde a \033[35m{dia:.2f} dia(s)\033[m')

    except (KeyboardInterrupt, TypeError, ValueError):
        print('\n\033[31mTivermos um problema com o dado digitado '
              'ou o(a) usuário(a) interrompeu a entrada de dados.\033[m')


tempo()
