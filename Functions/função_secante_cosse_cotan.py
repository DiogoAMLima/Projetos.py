def secan_cosse_cotan():
    from math import radians, sin, cos, tan
    angulo = float(input("Informe um ângulo que você deseja descobrir os valores de seno,cosseno, tangente, secante, "
                         "cossecante e cotangente: "))
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))
    print(f'O Seno, Cosseno e Tangente de \033[31m{angulo:.1f}°\033[m são respectivamente: '
          f'\033[34m{seno:.2f}\033[m, \033[34m{cosseno:.2f}\033[m e \033[34m{tangente:.2f}\033[m')
    secante = 1 / cosseno
    cossecante = 1 / seno
    cotangente = 1 / tangente
    print(f'O Secante, Cossecante, Cotangente de \033[31m{angulo:.1f}°\033[m são respectivamente: '
          f'\033[33m{secante:.2f}\033[m, \033[33m{cossecante:.2f}\033[m e '
          f'\033[33m{cotangente:.2f}\033[m')
    print()
    print('Importante lembrar que os valores estão com apenas duas casas decimais...')


secan_cosse_cotan()
