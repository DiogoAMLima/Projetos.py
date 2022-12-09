print('\033[36mResposta deve estar já dividida, ou seja, se for 5 / 10 responda 0.5...\033[m\n')

print('Uma caixa contém 4 bolas \033[31mvermelhas\033[m, 3 \033[32mverdes\033[m, '
      '2 \033[33mamarelas\033[m e 1 \033[35mroxa\033[m. A partir dessas informações responda:\n')

print('Lembrando que o total de bolas são = \033[34m10\033[m\n')

print('Fórmula = \033[34mP (probabilidade)\033[m = \033[33m(Quantidade de bolas de alguma cor específica)\033[m / '
      'Espaço amostral\n')

resp = float(input('Qual a probabilidade de retirar uma bola e ela ser \033[31mvermelha\033[m? '))
if resp == 0.4:
    print('\nVocê acertou ☻, Parabéns!!\n')
    print('A resolução era: P = 4/10\n')
    resp2 = float(input('Qual a probabilidade de retirar uma bola e ela ser '
                        '\033[31mvermelha\033[m ou \033[1;30mpreto\033[m? '))
    if resp2 == 0.7:
        print('\nVocê acertou ☻, Parabéns!!\n')
        print('A resoluçãp era: P = 7/10\n')
        resp3 = float(input('Qual a probabilidade de retirar duas bolas sendo uma \033[35mroxa\033[m e a outra '
                            '\033[32mverde\033[m (com reposição)? '))
        if resp3 == 0.03:
            print('\nVocê acertou ☻, Parabéns!!\n')
            print('A resoluçãp era: P = 1/10 x 3/10 = 3/100\n')
            resp4 = float(input('Qual a probabilidade de retirar três bolas sendo, 2 \033[35mroxa\033[m'
                                ' e uma \033[32mverde\033[m (com reposição)? '))
            if resp4 == 0.003:
                print('\nVocê acertou ☻, Parabéns!!\n')
                print('A resoluçãp era: P = 1/10 x 1/10 x 3/10 = 3/1000\n')
                resp5 = float(input('Qual a probabilidade de retirar 4 bolas sendo, uma \033[35mroxa\033[m,'
                                    ' uma \033[33mamarela\033[m, outra \033[35mroxa\033[m e uma \033[32mverde\033[m'
                                    ' (com reposição)? '))
                if resp5 == 0.0006:
                    print('\nVocê acertou todas as questões ☻, \033[1;30mPARABÉNS\033[m!!\n')
                    print('A resoluçãp era: P = 1/10 x 2/10 x 1/10 x 3/10 = 6/10000\n')
                else:
                    print('\nQue pena, tente na próxima...')
            else:
                print('\nQue pena, tente na próxima...')
        else:
            print('\nQue pena, tente na próxima...')
    else:
        print('\nQue pena, tente na próxima...')
else:
    print('\nQue pena, tente na próxima...')
