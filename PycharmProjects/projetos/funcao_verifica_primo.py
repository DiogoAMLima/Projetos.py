def verifica_primo():
    try:
        num = int(input('Digite um número para testar se é primo: '))
        res = 0
        for cont in range(1, num + 1):
            if num % cont == 0:
                res += 1
        if res == 2:
            print('\n\033[31mNúmero é primo\033[m')
        else:
            print('\n\033[32mNúmero não é primo\033[m')
    except (TypeError, ValueError, KeyboardInterrupt):
        print(
            '\n\033[34mTivermos um problema com o dado digitado '
            'ou o(a) usuário(a) interrompeu a entrada de dados.\033[m')


verifica_primo()
