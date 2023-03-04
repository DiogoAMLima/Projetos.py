def verifica_primo():  # Inicializando a funçãp
    try:  # Tratamento de erros
        # Um número primo é aquele que é dividido apenas por um e por ele mesmo.
        # Se houver mais do que divisores do que esses, não será primo
        num = int(input('Digite um número para testar se é primo: '))
        res = 0
        print()
        for cont in range(1, num + 1):  # Acrescentando 1 para que o range vá até o número digitado
            if num % cont == 0:  # Condicional para verificar se é primo
                print(f'\033[34m{num}\033[m % \033[32m{cont}\033[m = \033[35m{num % cont}\033[m')
                res += 1
        if res == 2:  # Se tiver dois divisores (1 e ele mesmo, é primo)
            print('\n\033[31mNúmero é primo\033[m')
            print(f"\nApenas \033[36m{res}\033[m divisores")  # Mostrando a quantidade de divisores
        else:
            print('\n\033[32mNúmero não é primo\033[m')
            print(f"\n\033[36m{res} divisores\033[m")
    except (TypeError, ValueError, KeyboardInterrupt):
        print(
            '\n\033[34mTivermos um problema com o dado digitado '
            'ou o(a) usuário(a) interrompeu a entrada de dados.\033[m')


verifica_primo()
