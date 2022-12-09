def velocidade_media(s, so, t, to):
    return (s - so) / (t - to)


print(f'A velocidade média é: \033[31m{velocidade_media(4, 2, 10.8, 6):.2f} m/s\033[m')


def aceleracao(v, vo, t, to):
    return (v - vo) / (t - to)


print(f'A aceleração média é: \033[32m{aceleracao(18, 4, 7, 5):.2f} m/s2\033[m')


def tempo_vm(s, so, vm):
    return (s - so) / vm


print(f'O tempo é: \033[33m{tempo_vm(4, 2, 10):.2f} s\033[m')


def distancia_vm(t, to, vm):
    return vm * (t - to)


print(f'A distância é: \033[34m{distancia_vm(4, 2, 10):.2f} m\033[m')


def tempo_am(v, vo, am):
    return (v - vo) / am


print(f'O tempo é: \033[35m{tempo_am(18, 4, 7):.2f} s\033[m')


def velocidade_am(am, t, to):
    return am * (t - to)


print(f'A velocidade é: \033[36m{velocidade_am(4, 3, 1):.2f} m/s\033[m')