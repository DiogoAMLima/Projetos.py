import math

ma = 0

valores = []

for i in range(9):
    x = float(input(f'Informe um valor para o valor {i+1}° lista: '))
    valores.append(x)  # Adicionando o valor informado a lista valores

# print(valores)

for i in range(len(valores)):  # O alcance irá até o tamanho de valores (9)
    ma += valores[i]

ma = ma / len(valores)

print(f'\nA média aritmética é: \033[34m{ma:.2f}\033[m')  # Apenas duas casas decimais

desvio = 0

for i in range(len(valores)):  # O alcance irá até o tamanho de valores (9)
    desvio += ((valores[i] - ma) ** 2) / len(valores)

print(f'\nO desvio padrão é: \033[97m{math.sqrt(desvio):.2f}\033[m')  # math.sqrt = Retorna a raiz quadrada

coef = (math.sqrt(desvio) / ma) * 100

print(f'\nO coeficiente de variação é: \033[31m{coef:.1f}%\033[m')  # math.sqrt = Retorna a raiz quadrada
