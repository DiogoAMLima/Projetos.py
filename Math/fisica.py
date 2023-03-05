(input("Aperte alguma tecla para as fórmulas aparecerem... "))

pergunta = 1

while pergunta != 0:  # Laço de repetição para enquanto for diferente de 0, o código continua
    print("1 - Velocidade média: vm = Δs/Δt\n")
    print("Δs = (s - so) || Δt = (t - to)\n")
    print("2 - Aceleração média: am = Δv/Δt \n")
    print("Δv = (v - vo) || Δt = (t - to)")
    while True:  # Laço de repetição
        try:  # Tratamento de erros
            pergunta = int(input("\nInforme o número da fórmula que quer resolver ou digite 0 para sair: "))
            if pergunta != int:  # Se o tipo digitado para a variável for diferente de inteiro, o laço acabará
                break
            print('\n\033[31mDigite apenas 1, 2 ou 0\033[m')
        except ValueError:
            print('\n\033[31mDigite um número válido\033[m')
    if pergunta == 0:
        print("\n\033[33mAté a próxima...\033[m")
    if pergunta == 1:
        print("\n1 - Sobre velocidade média, você quer descobrir: vm(velocidade média), Δs(distancia) ou Δt(tempo) ?")
        print('Digite apenas vm, distancia ou tempo para continuar...')
        resposta: str = str(input())
        if resposta != 'vm' and 'distancia' and 'tempo':
            print('\033[35mComando errado, tente novamente...\033[m')
        else:
            if resposta == 'vm':
                s = float(input(f'\nInforme o valor de s: '))
                so = float(input(f'Informe o valor de so: '))
                t = float(input(f'Informe o valor de t: '))
                to = float(input(f'Informe o valor de to: '))
                try:
                    if s - so == 0:
                        print('\nNão pode haver divisão por 0 pois, s - so resulta em 0...\n')
                    if t - to == 0:
                        print('\nNão pode haver divisão por 0 pois, t - to resulta em 0...\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
                try:
                    resultadovm = (s - so) / (t - to)
                    print('\n\033[34mA velocidade média é: '"{:.2f}".format(resultadovm), 'm/s\033[m\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
            if resposta == 'distancia':
                t = float(input(f'\nInforme o valor de t: '))
                to = float(input(f'Informe o valor de to: '))
                vm = float(input(f'Informe o valor de vm: '))
                resultadods = vm * (t - to)
                print('\n\033[34mA distância é: '"{:.2f}".format(resultadods), 'm\033[m\n')
            if resposta == 'tempo':
                s = float(input(f'\nInforme o valor de s: '))
                so = float(input(f'Informe o valor de so: '))
                vm = float(input(f'Informe o valor de vm: '))
                try:
                    if s - so == 0:
                        print('\nNão pode haver divisão por 0 pois, s - so resulta em 0...\n')
                    if vm == 0:
                        print('\nNão pode haver divisão por 0 pois, a vm é igual a 0...\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
                try:
                    resultadotp = (s - so) / vm
                    print('\n\033[34mO tempo é: '"{:.2f}".format(resultadotp), 's\033[m\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
    if pergunta == 2:
        print("\n2 - Sobre aceleração média, você quer descobrir: am(aceleração média), Δv(velocidade) ou Δt(tempo) ?")
        print('Digite apenas am, velocidade ou tempo para continuar...')
        resposta: str = str(input())
        if resposta != 'am' and 'velocidade' and 'tempo':
            print('\n\033[31mComando errado, tente novamente...\033[m')
        else:
            if resposta == 'am':
                v = float(input(f'\nInforme o valor de v: '))
                vo = float(input(f'Informe o valor de vo: '))
                t = float(input(f'Informe o valor de t: '))
                to = float(input(f'Informe o valor de to: '))
                try:
                    if v - vo == 0:
                        print('\nNão pode haver divisão por 0 pois, v - vo é igual a 0...\n')
                    if t - to == 0:
                        print('\nNão pode haver divisão por 0 pois, t - to é igual a 0...\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
                try:
                    resultadoam = (v - vo) / (t - to)
                    print('\n\033[35mA aceleração média é: '"{:.2f}".format(resultadoam), 'm/s2\033[m\n')
                except ZeroDivisionError:
                    print('\n\033[31mTente novamente...\033[m\n')
            if resposta == 'velocidade':
                t = float(input(f'\nInforme o valor de t: '))
                to = float(input(f'\nInforme o valor de to: '))
                am = float(input(f'\nInforme o valor de am: '))
                resultadovm = am * (t - to)
                print('\n\033[35mA velocidade média é: '"{:.2f}".format(resultadovm), 'm/s\033[m\n')
            if resposta == 'tempo':
                v = float(input(f'\nInforme o valor de v: '))
                vo = float(input(f'Informe o valor de vo: '))
                am = float(input(f'Informe o valor de am: '))
                try:
                    if v - vo == 0:
                        print('\nNão pode haver divisão por 0 pois, v - vo resulta em 0...\n')
                    if am == 0:
                        print('\nNão pode haver divisão por 0 pois, am é igual a 0...\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
                try:
                    resultadotp = (v - vo) / am
                    print('\n\03335mO tempo é: '"{:.2f}".format(resultadotp), 's\033[m\n')
                except ZeroDivisionError:
                    print('\nTente novamente...\n')
    elif pergunta >= 3 or pergunta <= -1:
        print("\n\033[36mNúmero incorreto, tente outra vez...\033[m\n")

# O .format também é uma forma de mostrar as variáveis em um print. Normalmente, seu usa um f'{}' para mostrar o valor 
# da variável, porém será mantido o .format como exemplo de forma de mostrar os valores também.
# O resto do código são condicionais e tratamento de erros.
