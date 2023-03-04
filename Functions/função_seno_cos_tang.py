def sen_cos_tan():  # Inicializando a função
    from math import radians, sin, cos, tan  # Métodos prontos para trigonometria
    angulo = float(input("Informe um ângulo que você deseja descobrir em seno,cosseno e tangente: "))
    seno = sin(radians(angulo))  # Valor do ângulo
    cosseno = cos(radians(angulo))  # Valor do ângulo
    tangente = tan(radians(angulo))  # Valor do ângulo
    print(f'O Seno, Cosseno e Tangente de \033[34m{angulo:.1f}\033[m são respectivamente: '
          f'\033[35m{seno:.2f}\033[m, \033[37m{cosseno:.2f}\033[m e \033[97m{tangente:.2f}\033[m')


sen_cos_tan()
