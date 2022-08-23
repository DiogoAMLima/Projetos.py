import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 3)  # Montando o gráfico com o valor que será elevado ao quadrado no meio

plt.title("Teste")  # Título

# Definindo as dimensões do gráfico:

# plt.figure(figsize=(8, 8))  # Eixo x e y seguidamente

# Gráfico, valor, valor ao quadrado, definindo legenda e cor:

plt.plot(a, a**3, label='Gráfico cúbico', color='Red')
plt.legend()  # Colocando a legenda

# Definindo localizações:

# x = 2 # Definindo a localização do ponto x
# y = 4 # Definindo a localização do ponto y
# plt.scatter(x, y)  # Colocando no gráfico

x = [10, 20, 30, 40, 50]  # Definindo uma lista para o ponto x
y = [5, 10, 15, 20, 25]  # Definindo uma lista para o ponto y
# plt.scatter(x, y)  # Colocando no gráfico os valores das listas
plt.scatter(x, y, color='Green')  # Colocando cor nos pontos no gráfico
# plt.scatter(y, x)  # Colocando no gráfico os valores das listas invertido

# Grades e linhas:

# plt.grid()  # Colocando grades
# plt.grid(axis='x')  # Linhas na vertical
# plt.grid(axis='y')  # Linhas na horizontal

# Removendo a moldura do gráfico:

# plt.box(False)

plt.show()  # Mostrar o gráfico
