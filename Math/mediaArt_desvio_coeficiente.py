import math

ma = 0

valores = []

for i in range(9):
    x = float(input(f'Informe um valor para o valor {i+1} lista: '))
    valores.append(x)

# print(valores)

for i in range(len(valores)):
    ma += valores[i]

ma = ma / len(valores)

print(f'\nA média aritmética é: \033[34m{ma}\033[m')

desvio = 0

for i in range(len(valores)):
    desvio += ((valores[i] - ma) ** 2) / len(valores)

print(f'\nO desvio padrão é: \033[97m{math.sqrt(desvio):.2f}\033[m')

coef = (math.sqrt(desvio) / ma) * 100

print(f'\nO coeficiente de variação é: \033[31m{coef:.1f}%\033[m')
