import math
# Para usar o math é necessário importar antes de utilizá-lo
# Código com operações básicas: multiplicar, dividir, raiz quadrada, número ao quadrado e ao cubo

print('\033[34m—\033[m' * 18, '\033[33mALGUMAS OPERAÇÕES BÁSICAS\033[m', '\033[34m—\033[m' * 18)
num = float(input("\nDigite algum número: "))
print('\nO número \033[31m{}\033[m, tem como sucessor: '
      '\033[32m{}\033[m e antecessor: \033[33m{}\033[m'.format(num, num+1, num-1))
print('\nO número \033[31m{}\033[m, multiplicado por 2 é: '
      '\033[32m{}\033[m e dividido por 2 é: \033[33m{}\033[m'.format(num, num*2, num/2))
print('\nO número \033[34m{}\033[m, tem como raiz quadrada: \033[35m{}\033[m'.format(num, math.sqrt(num)))

num2 = float(input("\nDigite outro número: "))
multi = float(input("Digite um número para multiplicar o número digitado acima: "))
print('\nO número \033[36m{}\033[m multiplicado por \033[37m{}\033[m é igual a: '
      '\033[97m{}\033[m'.format(num2, multi, num2*multi))
div = float(input("\nDigite um número para dividir o número digitado acima: "))
print('\nO número \033[31m{}\033[m dividido por \033[35m{}\033[m é igual a: '
      '\033[36m{}\033[m'.format(num2, div, num2/div))

num3 = float(input("\nDigite mais um número: "))
print('\nO número \033[32m{}\033[m ao quadrado é: \033[33m{}\033[m, '
      'e o número \033[31m{}\033[m ao cubo é: \033[34m{}\033[m'.format(num3, num3*num3, num3, num3*num3*num3), '\n')

print('\033[34m—\033[m' * 55)

# O .format também é uma forma de mostrar as variáveis em um print. Normalmente, seu usa um f'{}' para mostrar o valor
# da variável, porém será mantido o .format como exemplo de forma de mostrar os valores também.
