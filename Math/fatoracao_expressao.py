import sympy

# Expressão de exemplo: x**2 - 2*x - 8

variavel = str(input('Informe a variável: '))

variavel_exp = sympy.Symbol(f'{variavel}')

numero = int(input('\nInforme o primeiro valor: '))

numero2 = int(input('\nInforme o segundo valor: '))

expressao = variavel_exp ** numero - numero * variavel_exp - numero2

print(f'\nA expressão é: \033[35m{expressao}\033[m')

fatoracao = sympy.factor(variavel_exp ** numero - numero * variavel_exp - numero2)

print(f'\nA expressão fatorada resulta em: \033[34m{fatoracao}\033[m')

expansao = sympy.expand(fatoracao)

print(f'\nA expansão de \033[33m{fatoracao}\033[m é: \033[31m{expansao}\033[m')
