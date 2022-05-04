def sen_cos_tan():
    from math import radians, sin, cos, tan
    angulo = float(input("Informe um ângulo que você deseja descobrir em seno,cosseno e tangente: "))
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))
    print(f'O Seno, Cosseno e Tangente de {angulo:.1f} são respectivamente: {seno:.2f}, {cosseno:.2f} e {tangente:.2f}')


sen_cos_tan()
