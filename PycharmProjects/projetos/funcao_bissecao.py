def equacao():
    posit = []
    neg = []
    posicao = []
    posicao2 = []
    for i in range(-2, +1, 1):
        resp = (i ** 5) - (3 * i ** 4) + (3 * i ** 3) - (2 * i ** 2) - (5 * i) + 2
        if resp > 0:
            posicao.append(i)
            neg.append(resp)
        print(f'{resp}', end=', ')
    print('\n')
    print(neg)
    print(f'\nValore(s) onde tivemos raiz(es) positiva(s): {posicao}\n')
    for j in range(0, 4):
        resp1 = (j ** 5) - (3 * j ** 4) + (3 * j ** 3) - (2 * j ** 2) - (5 * j) + 2
        if resp1 > 0:
            posicao2.append(j)
            posit.append(resp1)
        print(f'{resp1}', end=', ')
    print('\n')
    print(posit)
    print(f'\nValore(s) onde tivemos raiz(es) positiva(s): {posicao2}\n')
    print('Para termos os intervalos completos que contém uma raiz: (0,0) (2,3)\n')


equacao()


def log():
    import math
    k = (math.log(3 - 2, 10) - math.log(0.070, 10)) / math.log(2, 10)
    print(f'O valor de k é: \033[36m{k}\033[m e aproximando: \033[33m{math.ceil(k)}\033[m')


log()
