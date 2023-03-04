def gerar_senha():  # Definindo a função
    while True:  # Laço de repetição
        import random
        import time
        op = str(input('\nPara continuarmos o procedimento, pressione qualquer tecla ou s para sair... ')).strip()
        if op == 's':
            print('\n\033[33mFinalizando...\033[m')
            break
        else:

            # Definindo as variaveis de acordo com os nomes

            num = "0123456789"

            caracteres_especiais = r"!@#$%&*/\?:"

            letra_minuscula = "abcdefghijklmnopqrstuvwxyz"

            letra_maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            juntando = num + caracteres_especiais + letra_minuscula + letra_maiuscula  # Unindo as strings

            try:
                tamanho_da_senha = int(input('\nInforme a quantidade de caracteres: '))
                print(f'\nA quantidade de caracteres escolhida foi: \033[34m{tamanho_da_senha}\033[m\n')
                senha = "".join(random.sample(juntando, tamanho_da_senha))
                # Juntando as strings relacionadas com o método sample que de acordo com o tamanho,
                # geram os caracteres para a senha
                print('\033[31mEstamos gerando sua senha, por favor aguarde...\033[m\n')
                time.sleep(4)
                print(f'\033[34mSua senha é:\033[m \033[35m{senha}\033[m')
            except (ValueError, TypeError):
                print('Tivemos um problema com os tipos de dados que você digitou! Necessário que seja um número '
                      'inteiro!')


gerar_senha()
