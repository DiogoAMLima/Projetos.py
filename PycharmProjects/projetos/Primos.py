print('-------------------NÚMEROS PRIMOS-------------------')
print('\n')
num = int(input('Digite um número para testar se é primo: '))
resultado = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        resultado += 1
# Laço de repetição para verificar o resto da divisão do número digitado (num) pelo contador (cont).
# O contador irá checar de 1 até: número digitado + 1.
# Exemplo: Se 16 for digitado, ele irá verificar até o número 17, pois, (num + 1) = 17.
# Se resultado for 2 é porque ele foi divisível 2 vezes, caso passe de 2,ou seja, 3 para cima, ele não será primo, pois,
# o número só é primo quando é maior que 1 e é divisível por 1 e ele mesmo.
if resultado == 2:
    print('O NÚMERO É PRIMO')
else:
    print('O NÚMERO NÃO É PRIMO')
print('\n')
print('----------------------------------------------------')
