matriz = [[0, 0], [0, 0], [0, 0], [0, 0]]

for li in range(0, 4):
    for co in range(0, 2):
        matriz[li][co] = int(input(f'Digite um valor para \033[34m[{li},\033[m \033[35m{co}]:\033[m '))
print()
for lin in range(0, 4):
    for col in range(0, 2):
        print(f'\033[31m[{matriz[lin][col]:^5}]\033[m', end='')
    print()
