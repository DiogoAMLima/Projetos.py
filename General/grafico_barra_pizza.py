import matplotlib.pyplot as plt

print('\033[34m—————————————————GRÁFICO EM BARRAS E PIZZA—————————————————\033[m')

# Exemplos de gráficos em barras e pizza:

# Interação com o usuário (gráfico de barras):

d = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']  # Dias da semana

h = []

for dias in d:
    horas = float(input(f'Informe a quantidade de horas treinadas na academia na {dias}: '))
    h.append(horas)
# print(h)

x = float(input('\nInforme a dimesão do eixo x do gráfico: '))
y = float(input('\nInforme a dimesão do eixo y do gráfico: '))

plt.figure(figsize=(x, y))

print()

cores = ['Black', 'Blue', 'Gray', 'Yellow', 'Green', 'Red', 'Orange', 'Pink', 'White']
print(cores)

cor = str(input('\nEscolha uma cor listada acima, (digite exatamente como está na tela): '))

if cor not in cores:
    print('\n\033[35mEsta cor não está na lista...\033[m')
else:
    print('\nCor escolhida com sucesso')

    plt.bar(d, h, color=cor, label='Horas treinadas na academia')

    plt.grid(False)
    plt.box(False)
    plt.title('Horas treinadas na academia durante esta semana: ')
    plt.legend()
    plt.show()

    # Gráfico de pizza:

    a = float(input('\nInforme a dimesão do eixo x do gráfico da pizza: '))
    b = float(input('\nInforme a dimesão do eixo y do gráfico da pizza: '))

    plt.figure(figsize=(a, b))

    plt.pie(h, labels=d, autopct='%1.1f%%', shadow=True, startangle=90)

    # Título:
    plt.title("Porcentagem de horas treinadas na academia")

    plt.show()
