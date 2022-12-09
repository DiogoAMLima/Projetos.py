def velocidade_media(s: float, so: float, t: float, to: float) -> float:
    return (s - so) / (t - to)


vm = velocidade_media(4, 2, 10.8, 6)

print('A velocidade média é: '"{:.2f}".format(vm), 'm/s')


def aceleracao(v: float, vo: float, t: float, to: float) -> float:
    return (v - vo) / (t - to)


am = aceleracao(18, 4, 7, 5)

print('A aceleração média é: '"{:.2f}".format(am), 'm/s2')


def tempo_vm(s: float, so: float, vm: float) -> float:
    return (s - so) / vm


tmp = tempo_vm(4, 2, 10)

print('O tempo é: '"{:.2f}".format(tmp), 's')


def distancia_vm(t: float, to: float, vm: float) -> float:
    return vm * (t - to)


dstn = distancia_vm(4, 2, 10)

print('A distância é: '"{:.2f}".format(dstn), 'm')


def tempo_am(v: float, vo: float, am: float) -> float:
    return (v - vo) / am


tmpam = tempo_am(18, 4, 7)

print('O tempo é: '"{:.2f}".format(tmpam), 's')


def velocidade_am(am: float, t: float, to: float) -> float:
    return am * (t - to)


vam = velocidade_am(4, 3, 1)

print('A velocidade é: '"{:.2f}".format(vam), 'm/s')
