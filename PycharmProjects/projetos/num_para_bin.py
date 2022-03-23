print('---------------------BINÁRIO---------------------')
print('\n')
n = int(input("Informe um número inteiro: "))
# bin é conversor automático do python, assim como oct (OCTAL), hex (HEXADECIMAL),...
print(f'O número {n} em binário é: {format(bin(n)[2:])}')
# [2:] é para retirar o 0b da resposta.
print('\n')
print('-------------------------------------------------')
