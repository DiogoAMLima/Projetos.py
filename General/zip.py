# Exemplo de zip com valores pré-estabelecidos:

# x = [10, 20, 25, 30]
# y = [1, 2, 3, 4]
# z = [100, 200, 300, 400]
#
# for valor1, valor2, valor3 in zip(x, y, z, strict=True):
#     print(valor1, valor2, valor3)

# Parâmetro strict só permitirá que funcione caso os tamanhos das listas sejam iguais
# (cada lista possuindo o mesmo número de elementos)

# Interação com o usuário para adicionar valores em listas:

x = []
y = []
z = []

valores = int(input('Informe a quantidade de valores que terá nas lista: '))

i = 0

for i in range(valores):
    values = int(input('\nInforme o valor a ser adicionado na lista x: '))
    x.append(values)
    values2 = int(input('Informe o valor a ser adicionado na lista y: '))
    y.append(values2)
    values3 = int(input('Informe o valor a ser adicionado na lista z: '))
    z.append(values3)

for a, b, c in zip(x, y, z):
    print(f'\n\033[31m{a}\033[m, \033[33m{b}\033[m, \033[34m{c}\033[m')

# Não é necessário o parâmetro strict porque já definimos o tamanho da lista anteriormente para todas as listas
