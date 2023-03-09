print('\033[32m—————————————————————————————————————LEIS DE KEPLER—————————————————————————————————————\033[m\n')
print('-> Fórmula da 3ª lei de kepler: Quadrado do  período de revolução de cada planeta é '
      'proporcional ao cubo do raio médio de sua órbita.\n'
      '\033[31m-> Quanto mais distante o planeta estiver do sol mais tempo levará para completar a translação.\033[m\n'
      '\033[33m-> T ao quadrado sobre r ao cubo igual a K -> K = (T**T) / (r**3)\033[m')

print('\n\033[35mInformações sobre os planetas -> Período de revolução e raio de órbita:\n'
      'Planetas ||||| Período de revolução(T) ||||| Raio da órbita (r)\033[m\n'
      'Mercúrio:            0,241 anos               0,387 u.a.\n'
      'Vênus:               0,615 anos               0,723 u.a.\n'
      'Terra:               1 ano                    1 u.a.\n'
      'Marte:               1,8881 ano               1,524 u.a.\n'
      'Júpiter:             11,86 anos               5,204 u.a.\n'
      'Saturno:             29,6 anos                9,58 u.a.\n'
      'Urano:               83,7 anos                19,14 u.a.\n'
      'Netuno:              165,4 anos               30,2 u.a.\n')


def planeta():
    planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']
    escolha = str(input('Escolha um planeta da tabela mostrada acima: '))
    if escolha in planetas:
        print(f'\nVocê escolheu o planeta: \033[34m{escolha}\033[m')
        if escolha == 'Mercúrio':
            print(f'A constante K é igual a: {(0.241 * 0.241) / (0.387 ** 3):.3f}\n')
        if escolha == 'Vênus':
            print(f'A constante K é igual a: {(0.615 * 0.615) / (0.723 ** 3):.3f}\n')
        if escolha == 'Terra':
            print(f'A constante K é igual a: {(1 * 1) / (1 ** 3):.3f}\n')
        if escolha == 'Marte':
            print(f'A constante K é igual a: {(1.8881 * 1.8881) / (1.524 ** 3):.3f}\n')
        if escolha == 'Júpiter':
            print(f'A constante K é igual a: {(11.86 * 11.86) / (5.204 ** 3):.3f}\n')
        if escolha == 'Saturno':
            print(f'A constante K é igual a: {(29.6 * 29.6) / (9.58 ** 3):.3f}\n')
        if escolha == 'Urano':
            print(f'A constante K é igual a: {(83.7 * 83.7) / (19.14 ** 3):.3f}\n')
        if escolha == 'Neturno':
            print(f'A constante K é igual a: {(165.4 * 165.4) / (30.2 ** 3):.3f}\n')
    else:
        print('\nEsse planeta não está na lista...\n')


planeta()

print('\033[34m—————————————————————————————————————RAIO MÉDIO—————————————————————————————————————\033[m\n')

print('Afélio -> é o ponto da órbita em que um planeta ou um corpo menor está mais afastada do sol')
print('Perifélio -> é o ponto da órbita em que um planeta ou um corpo menor está mais próximo ao sol\n')


def raio_medio():
    try:
        rmax = float(input('Informe o raio máximo: '))
        rmin = float(input('Informe o raio mínimo: '))
        r = ((rmax + rmin) / 2)
        print(f'O Afélio que é = \033[36m{rmax}\033[m + Perifélio que é = \033[35m{rmin}\033[m, '
              f'teremos o raio médio = \033[33m{r}\033[m')
    except ValueError:
        print('\n\033[31mErro de tipo, tente novamente...\033[m')


raio_medio()


print('\n\033[35m———————————————————————————————LEI DE GRAVITAÇÃO UNIVERSAL———————————————————————————————\033[m')

print('\n\033[34mF = G * (M x m) / R ** R\033[m')
print('\nF = força gravitacional || G = constante de gravitação universal || M = massa do sol || m = massa do planeta'
      '|| R = raio')

print('G = constante de gravitação universal = 6.67 * 10 ** -11 ')
G = abs(6.67 * (10 ** (-11)))
print('M = Massa do sol = 1.989 * 10 ** 30')
M = abs(1.989 * (10 ** 30))

print('\n\033[36mExercício:\033[m')

print(abs(6.67 * (10 ** (-11))) * abs(1.989 * (10 ** 30)) * abs(2 * (10 ** 5)) / (10 * 10))

# Interação com o usuário:


def lgu():
    try:
        R: float = float(input('\nInforme o valor de R: '))
        m: float = float(input('Informe a massa do planeta: '))

        F = abs(G * (abs(M * m)) / abs(R * R))

        print(f'\nA força gravitacional é: \033[34m{F}\033[m')
    except ValueError:
        print('\n\033[31mErro de tipo, tente novamente...\033[m')


lgu()
