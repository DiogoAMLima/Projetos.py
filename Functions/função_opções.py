def escolha():  # Inicializando a função
    while True:  # Looping para escolhermos as operações quantas vezes quisermos
        try:  # Tratamento de erros
            input('\nAperte enter para o Menu aparecer: ')
            print()
            print('\033[31m—\033[m' * 13, '\033[36mMENU\033[m', '\033[31m—\033[m' * 13)
            print('\n\033[32mOPÇÃO 1 - SOMAR\033[m\n'
                  '\033[32mOPÇÃO 2 - SUBTRAIR\033[m\n'
                  '\033[32mOPÇÃO 3 - MULTIPLICAR\033[m\n'
                  '\033[32mOPÇÃO 4 - DIVIDIR\033[m\n'
                  '\033[32mOPÇÃO 5 - QUOCIENTE E RESTO\033[m\n'
                  '\033[32mOPÇÃO 6 - FATORIAL\033[m\n'
                  '\033[32mOPÇÃO 7 - NÚMERO AO QUADRADO\033[m\n'
                  '\033[32mOPÇÃO 8 - NÚMERO AO CUBO\033[m\n')
            op = int(input('Informe uma das opções acima ou qualquer outro número para sair: '))
            print()
        except(ValueError, TypeError):

            print('\n\033[0;35mERRO: por favor, digite um número int ou float válido\033[m')
            continue
            # Continue identifica o erro, mostrará o erro e ignora essa parte do looping para o looping continuar
        except KeyboardInterrupt:
            print('\n\033[35mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            if op == 1:  # Soma de dois números
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                soma = x + y
                print(f'\n{x} + {y} = \033[33m{soma:.2f}\033[m\n')
            elif op == 2:  # Subtração de dois números
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                subtrair = x - y
                print(f'\n{x} - {y} = \033[33m{subtrair:.2f}\033[m\n')
            elif op == 3:  # Multiplicação de dois números
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                multiplicar = x * y
                print(f'\n{x} * {y} = \033[33m{multiplicar:.2f}\033[m\n')
            elif op == 4:  # Divisão entre dois números
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                divisao = x / y
                print(f'\n{x} / {y} = \033[33m{divisao:.2f}\033[m\n')
            elif op == 5:  # Quociente e resto entre dois números
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                quociente = x // y
                resto = x % y
                print(f'\nO quociente de {x} // {y} e resto de {x} % {y} são \033[33m{quociente} e {resto}\033[m\n')
            elif op == 6:  # Fatorial de um número
                try:
                    num = int(input('Informe um número: '))
                    f = 1
                    for c in range(num, 0, -1):
                        f *= c
                    print(f'\nO fatorial é \033[33m{f}\033[m\n')
                except ValueError:
                    print('\n\033[31mO tipo de dado digitado está incorreto...\033[m\n')
            elif op == 7:  # Número ao quadrado
                n = float(input('Informe um número: '))
                quadrado = n * n
                print(f'\n{n} ao quadrado é \033[33m{quadrado:.2f}\033[m\n')
            elif op == 8:  # Número ao cubo
                n = float(input('Informe um número: '))
                cubo = n * n * n
                print(f'\n{n} ao cubo é \033[33m{cubo:.2f}\033[m\n')
            else:
                print('\033[34m—\033[m' * 28, '\033[34mAté mais\033[m', '\033[34m—\033[m' * 28)
                break


escolha()
