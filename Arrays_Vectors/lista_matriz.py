matriz = [[0, 0], [0, 0], [0, 0], [0, 0]]  # Definição da matriz (4 linhas e 2 colunas)

for li in range(0, 4):  # Percorrendo as linhas
    for co in range(0, 2):  # Percorrendo as colunas
        matriz[li][co] = int(input(f'Digite um valor para \033[34m[{li},\033[m \033[35m{co}]:\033[m '))
        # Inserindo valores na matriz
print()
# Percorrendo e mostrando os valores da matriz
for lin in range(0, 4):
    for col in range(0, 2):
        print(f'\033[31m[{matriz[lin][col]:^5}]\033[m', end='')  # ^5 permite dar espaços entre os [] e o valor dentro
    print()
