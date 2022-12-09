def escolha():
    while True:
        try:
            print()
            input('Aperte enter para o Menu aparecer: ')
            print('\033[31m—\033[m' * 13, 'MENU', '\033[31m—\033[m' * 13)
            print('\033[32mOPÇÃO 1 - SOMAR\033[m\n'
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
            print('\033[0;35mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[35mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            if op == 1:
                x = int(input('Informe o primeiro número: '))
                y = int(input('Informe o segundo número: '))
                soma = x + y
                print(f'{x} + {y} = \033[33m{soma}\033[m')
                print()
            elif op == 2:
                x = int(input('Informe o primeiro número: '))
                y = int(input('Informe o segundo número: '))
                subtrair = x - y
                print(f'{x} - {y} = \033[33m{subtrair}\033[m')
                print()
            elif op == 3:
                x = int(input('Informe o primeiro número: '))
                y = int(input('Informe o segundo número: '))
                multiplicar = x * y
                print(f'{x} * {y} = \033[33m{multiplicar}\033[m')
                print()
            elif op == 4:
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                divisao = x / y
                print(f'{x} / {y} = \033[33m{divisao}\033[m')
                print()
            elif op == 5:
                x = float(input('Informe o primeiro número: '))
                y = float(input('Informe o segundo número: '))
                quociente = x // y
                resto = x % y
                print(f'O quociente de {x} // {y} e resto de {x} % {y} são \033[33m{quociente} e {resto}\033[m')
                print()
            elif op == 6:
                num = int(input('Informe um número: '))
                f = 1
                for c in range(num, 0, -1):
                    f *= c
                print(f'O fatorial é \033[33m{f}\033[m')
                print()
            elif op == 7:
                n = int(input('Informe um número: '))
                quadrado = n * n
                print(f'{n} ao quadrado é \033[33m{quadrado}\033[m')
                print()
            elif op == 8:
                n = int(input('Informe um número: '))
                cubo = n * n * n
                print(f'{n} ao cubo é \033[33m{cubo}\033[m')
                print()
            else:
                print('\033[34m—\033[m' * 28, '\033[34mAté mais\033[m', '\033[34m—\033[m' * 28)
                break


escolha()
