(input("Aperte alguma tecla para as fórmulas aparecerem... "))

pergunta = 1

while pergunta != 0:
    print("1 - Velocidade média: vm = Δs/Δt\n")
    print("Δs = (s - so) || Δt = (t - to)\n")
    print("2 - Aceleração média: am = Δv/Δt \n")
    print("Δv = (v - vo) || Δt = (t - to)\n")
    while True:
        try:
            pergunta = int(input("Informe o número da fórmula que quer resolver ou digite 0 para sair: "))
            if pergunta != int:
                break
            print('Digite apenas 1, 2 ou 0')
        except ValueError:
            print('Digite um número válido')
    if pergunta == 0:
        print("Até a próxima...")
    if pergunta == 1:
        print("1 - Sobre velocidade média, você quer descobrir: vm(velocidade média), Δs(distancia) ou Δt(tempo) ?")
        print('Digite apenas vm, distancia ou tempo para continuar...')
        resposta: str = str(input())
        if resposta != 'vm' and 'distancia' and 'tempo':
            print('Comando errado, tente novamente...')
        else:
            if resposta == 'vm':
                s = float(input(f'Informe o valor de s '))
                so = float(input(f'Informe o valor de so '))
                t = float(input(f'Informe o valor de t '))
                to = float(input(f'Informe o valor de to '))
                try:
                    if s - so == 0:
                        print('Não pode haver divisão por 0 pois, s - so resulta em 0... \n')
                    if t - to == 0:
                        print('Não pode haver divisão por 0 pois, t - to resulta em 0... \n')
                except ZeroDivisionError:
                    pass
                try:
                    resultadovm = (s - so) / (t - to)
                    print('A velocidade média é: '"{:.2f}".format(resultadovm), 'm/s \n')
                except ZeroDivisionError:
                    print('Tente novamente...\n')
            if resposta == 'distancia':
                t = float(input(f'Informe o valor de t '))
                to = float(input(f'Informe o valor de to '))
                vm = float(input(f'Informe o valor de vm '))
                resultadods = vm * (t - to)
                print('A distância é: '"{:.2f}".format(resultadods), 'm \n')
            if resposta == 'tempo':
                s = float(input(f'Informe o valor de s '))
                so = float(input(f'Informe o valor de so '))
                vm = float(input(f'Informe o valor de vm '))
                try:
                    if s - so == 0:
                        print('Não pode haver divisão por 0 pois, s - so resulta em 0...')
                    if vm == 0:
                        print('Não pode haver divisão por 0 pois, a vm é igual a 0...')
                except ZeroDivisionError:
                    pass
                try:
                    resultadotp = (s - so) / vm
                    print('O tempo é: '"{:.2f}".format(resultadotp), 's \n')
                except ZeroDivisionError:
                    print('Tente novamente...\n')
    if pergunta == 2:
        print("2 - Sobre aceleração média, você quer descobrir: am(aceleração média), Δv(velocidade) ou Δt(tempo) ?")
        print('Digite apenas am, velocidade ou tempo para continuar...')
        resposta: str = str(input())
        if resposta != 'am' and 'velocidade' and 'tempo':
            print('Comando errado, tente novamente...')
        else:
            if resposta == 'am':
                v = float(input(f'Informe o valor de v '))
                vo = float(input(f'Informe o valor de vo '))
                t = float(input(f'Informe o valor de t '))
                to = float(input(f'Informe o valor de to '))
                try:
                    if v - vo == 0:
                        print('Não pode haver divisão por 0 pois, v - vo é igual a 0...')
                    if t - to == 0:
                        print('Não pode haver divisão por 0 pois, t - to é igual a 0...')
                except ZeroDivisionError:
                    pass
                try:
                    resultadoam = (v - vo) / (t - to)
                    print('A aceleração média é: '"{:.2f}".format(resultadoam), 'm/s2 \n')
                except ZeroDivisionError:
                    print('Tente novamente...\n')
            if resposta == 'velocidade':
                t = float(input(f'Informe o valor de t '))
                to = float(input(f'Informe o valor de to '))
                am = float(input(f'Informe o valor de am '))
                resultadovm = am * (t - to)
                print('A velocidade média é: '"{:.2f}".format(resultadovm), 'm/s \n')
            if resposta == 'tempo':
                v = float(input(f'Informe o valor de v '))
                vo = float(input(f'Informe o valor de vo '))
                am = float(input(f'Informe o valor de am '))
                try:
                    if v - vo == 0:
                        print('Não pode haver divisão por 0 pois, v - vo resulta em 0...')
                    if am == 0:
                        print('Não pode haver divisão por 0 pois, am é igual a 0...')
                except ZeroDivisionError:
                    pass
                try:
                    resultadotp = (v - vo) / am
                    print('O tempo é: '"{:.2f}".format(resultadotp), 's \n')
                except ZeroDivisionError:
                    print('Tente novamente...\n')
    elif pergunta >= 3:
        print("Número incorreto, tente outra vez... \n")
    elif pergunta <= -1:
        print("Número incorreto, tente outra vez... \n")
