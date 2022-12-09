import matplotlib.pyplot as plt

# Exemplo de gráfico em linhas:

# Gastos de comida por mês:

comida = [150, 235, 230, 167, 190, 300, 340, 360, 290, 250, 344, 302]

# Gastos de bebida por mês:

bebida = [60, 50, 88, 77, 40, 100, 130, 160, 55, 67, 90, 86]

# Gastos com contas por mês:

contas = [500, 612, 550, 499, 700, 769, 657, 567, 597, 488, 510, 590]

# Meses:

m = ['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGS', 'STM', 'OTB', 'NOV', 'DEZ']

# Tamanho do gráfico:

plt.figure(figsize=(14, 9))

# Título:

plt.title("Gastos em um ano")

# Primeira, segunda e terceira linha no gráfico de comparação de preços:

plt.plot(m, comida, label='Gastos com comida', color='Green')


plt.plot(m, bebida, label='Gastos com bebida', color='Blue')


plt.plot(m, contas, label='Gastos com as contas', color='Black')

# Legenda ao eixo x e y respectivamente:
plt.xlabel("Meses", color='Red')
plt.ylabel("Gastos em reais", color='Red')

# Grade e legenda:

plt.grid()
plt.legend()

# Mostrar o gráfico:

plt.show()
