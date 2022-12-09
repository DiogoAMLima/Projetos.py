import math
# Para usar o math é necessário importar antes de utilizá-lo
print('------------------------------ALGUMAS OPERAÇÕES BÁSICAS-------------------------------')
num = float(input("Digite algum número: "))
print('O número {}, tem como sucessor: {} e antecessor: {}'.format(num, num+1, num-1))
print('O número {}, multiplicado por 2 é: {} e dividido por 2 é: {}'.format(num, num*2, num/2))
print('O número {}, tem como raiz quadrada: {}'.format(num, math.sqrt(num)))

print('\n')

num2 = float(input("Digite outro número: "))
multi = float(input("Digite um número para multiplicar o número digitado acima: "))
print('O número {} multiplicado por {} é igual a: {}'.format(num2, multi, num2*multi))
print("\n")
div = float(input("Digite um número para dividir o número digitado acima: "))
print('O número {} dividido por {} é igual a: {}'.format(num2, div, num2/div))

print("\n")

num3 = float(input("Digite mais um número: "))
print('O número {} ao quadrado é: {}, e o número {} ao cubo é: {}'.format(num3, num3*num3, num3, num3*num3*num3))

print('\n')

print('-------------------------------------------------------------------------------------')
