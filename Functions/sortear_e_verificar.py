from random import randint
from time import sleep


def sorteado(sorteados):
    print('Serão sorteados \033[97m10\033[m valores entre \033[37m-10\033[m e \033[30m10\033[m: ', end='')
    for i in range(0, 10):
        num = randint(-10, 10)
        sorteados.append(num)
        print(f'\033[35m{num}\033[m ', end='')
        sleep(0.4)
    print('  \033[36mFinalizado\033[m!!!')


def verificar(sorteados):
    qntd_neg = 0
    qntd_pos = 0
    par = 0
    impar = 0
    for valor in sorteados:
        if valor < 0:
            qntd_neg += 1
        if valor >= 0:
            qntd_pos += 1
        if valor % 2 == 0:
            par += 1
        if valor % 2 == 1:
            impar += 1
    print(f'\nA quantidade de números negativos foram: \033[31m{qntd_neg}\033[m')
    print(f'\nA quantidade de números positivos foram: \033[32m{qntd_pos}\033[m')
    print(f'\nA quantidade de pares é: \033[33m{par}\033[m')
    print(f'\nA quantidade de ímpares é: \033[34m{impar}\033[m')


valores = list()

sorteado(valores)
verificar(valores)
