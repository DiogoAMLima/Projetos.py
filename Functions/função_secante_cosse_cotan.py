def secan_cosse_cotan():  # Inicializando a função
    from math import radians, sin, cos, tan  # Métodos prontos para trigonometria
    angulo = float(input("Informe um ângulo que você deseja descobrir os valores de seno, cosseno, tangente, secante, "
                         "cossecante e cotangente: "))
    seno = sin(radians(angulo))  # Valor do ângulo
    cosseno = cos(radians(angulo))  # Valor do ângulo
    tangente = tan(radians(angulo))  # Valor do ângulo
    print(f'O Seno, Cosseno e Tangente de \033[31m{angulo:.1f}°\033[m são respectivamente: '
          f'\033[34m{seno:.2f}\033[m, \033[34m{cosseno:.2f}\033[m e \033[34m{tangente:.2f}\033[m')
    secante = 1 / cosseno
    cossecante = 1 / seno
    cotangente = 1 / tangente
    print(f'O Secante, Cossecante, Cotangente de \033[31m{angulo:.1f}°\033[m são respectivamente: '
          f'\033[33m{secante:.2f}\033[m, \033[33m{cossecante:.2f}\033[m e '
          f'\033[33m{cotangente:.2f}\033[m')
    print('\n\033[32mImportante lembrar que os valores estão com apenas duas casas decimais...\033[m')


secan_cosse_cotan()
