from math import radians, sin, cos, tan  # Métodos prontos para trigonometria

# Forma 1

# ang = float(input("Informe um ângulo que você deseja descobrir em seno,cosseno e tangente: "))
# seno = sin(radians(ang))
# print('O ângulo digitado foi {} e o seno é {:.2f} \n'.format(ang, seno))
# cosseno = cos(radians(ang))
# print('O ângulo digitado foi {} e o cosseno é {:.2f} \n'.format(ang, cosseno))
# tangente = tan(radians(ang))
# print('O ângulo digitado foi {} e a tangente é {:.2f} \n'.format(ang, tangente))

# Forma 2

angulo = float(input("Informe um ângulo que você deseja descobrir em seno,cosseno e tangente: "))
seno = sin(radians(angulo))  # Valor do ângulo
cosseno = cos(radians(angulo))  # Valor do ângulo
tangente = tan(radians(angulo))  # Valor do ângulo
print(f'O Seno, Cosseno e Tangente de {angulo:.1f} são respectivamente: {seno:.2f}, {cosseno:.2f} e {tangente:.2f}')
