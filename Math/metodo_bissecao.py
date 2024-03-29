import math

print('\033[31m————————————————Método Bisseção————————————————\033[m')  # Este método consiste em dividir o
# intervalo [a, b], de forma iterativa, ao meio.

print('Dada a equação: x**5 - 3x**4 + 3x**3 - 2x**2 - 5x + 2 = 0')  # Equação informada

print('Intervalo \033[31m(-2, 0) e (0, 3)\033[m')  # Intervalo para as iterações

print('Raizes negativas: \033[32m-2, -1, 0\033[m')

print('Raizes positivas: \033[33m0, 1, 2, 3\033[m')

print('\n\033[34mResultado das raizes negativas:\033[m')

posit = []

res1 = ((-2)**5) - (3*(-2)**4) + (3*(-2)**3) - (2*(-2)**2) - (5*(-2)) + 2  # Resultado de x = -2
print(f'\nx = -2 resultado: {res1}')
if res1 > 0:
    posit.append(res1)

res2 = ((-1)**5) - (3*(-1)**4) + (3*(-1)**3) - (2*(-1)**2) - (5*(-1)) + 2  # Resultado de x = -1
print(f'\nx = -1 resultado: {res2}')
if res2 > 0:
    posit.append(res2)

res3 = (0**5) - (3*0**4) + (3*0**3) - (2*0**2) - (5*0) + 2  # Resultado de x = 0
print(f'\nx = 0 resultado: {res3}')
if res3 > 0:
    posit.append(res3)

print('\n\033[35mResultado das raizes positivas:\033[m')

res4 = (0**5) - (3*0**4) + (3*0**3) - (2*0**2) - (5*0) + 2  # Resultado de x = 0
print(f'\nx = 0 resultado: {res4}')
if res4 > 0:
    posit.append(res4)

res5 = (1**5) - (3*1**4) + (3*1**3) - (2*1**2) - (5*1) + 2  # Resultado de x = 1
print(f'\nx = 1 resultado: {res5}')
if res5 > 0:
    posit.append(res5)

res6 = (2**5) - (3*2**4) + (3*2**3) - (2*2**2) - (5*2) + 2  # Resultado de x = 2
print(f'\nx = 2 resultado: {res6}')
if res6 > 0:
    posit.append(res6)

res7 = (3**5) - (3*3**4) + (3*3**3) - (2*3**2) - (5*3) + 2  # Resultado de x = 3
print(f'\nx = 3 resultado: {res7}')
if res7 > 0:
    posit.append(res7)

print(f'\nA(s) raíz(es) positiva(s) é/são: {posit}')

print(f'\nIntervalo \033[31m(0,0) (2,3)\033[m contém {len(posit)} raize(s)')  # Quantidade de raízes

print('\nEstimativa para número de iterações necessário para calcular a menor raiz positiva possível'
      ' com precisão de \033[32m0,070\033[m')

print('\nAchando o valor de k: k>= (log(b - a) - log(0,070)) / log(2)\n')

k = (math.log(3 - 2, 10) - math.log(0.070, 10)) / math.log(2, 10)
print(f'O valor de k é: \033[36m{k}\033[m e aproximando: \033[33m{math.ceil(k)}\033[m')
