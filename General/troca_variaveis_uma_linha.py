# x = 15
# y = 12
#
# x, y = y, x
#
# print(x, y)

x = int(input('Informe um número para a variável x: '))
y = int(input('Informe um número para a variável y: '))

x, y = y, x

print(f'A variável \033[35mx\033[m agora é igual a: \033[34m{x}\033[m e a \033[35my\033[m é igual a: \033[36m{y}\033[m')
