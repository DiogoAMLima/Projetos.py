from math import radians, sin, cos, tan

# Forma 1

# ang = float(input("Informe um ângulo que você deseja descobrir em seno,cosseno e tangente: "))
# seno = sin(radians(ang))
# print('O ângulo digitado foi {} e o seno é {:.2f} \n'.format(ang, seno))
# cosseno = cos(radians(ang))
# print('O ângulo digitado foi {} e o cosseno é {:.2f} \n'.format(ang, cosseno))
# tangente = tan(radians(ang))
# print('O ângulo digitado foi {} e a tangente é {:.2f} \n'.format(ang, tangente))

# Forma 2

angulo = float(input("Informe um ângulo que você deseja descobrir em seno,cosseno e tangente:  "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno, Cosseno e Tangente de {} são respectivamente: {:.2f}, {:.2f} e {:.2f}'
      .format(angulo, seno, cosseno, tangente))
