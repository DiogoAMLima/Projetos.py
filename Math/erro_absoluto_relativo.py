import math

print('———————————— \033[34mERRO ABSOLUTO E RELATIVO\033[m ————————————')

# Erro_Absoluto(𝑥, 𝑥ҧ) = ||𝑥 − 𝑥ҧ||

# Erro_Relativo(𝑥, 𝑥ҧ) = ||𝑥 − 𝑥ҧ|| / ||x||

# Exemplo:

# x = [1;4] e 𝑥ҧ = [2;3]

# x - 𝑥ҧ = [1-2; 4-3] = [-1;1]

# Erro absoluto(x,𝑥ҧ) = ||x-𝑥ҧ|| / (-1 ** 1/2) + (1 ** 1/2) = raiz de 2

# Calculando a raiz quadrada:

# raiz = math.pow(2, 1/2)
# print(raiz)

# Ou:

# raiz_de_2 = 2 ** (1/2)
# print(raiz_de_2)
#
# print('\n')
#
# raiz_de_17 = math.pow(17, 1/2)
# print(raiz_de_17)

# print(raiz_de_2 / raiz_de_17)

# Erro relativo(x,𝑥ҧ) = || x - 𝑥ҧ || / ||x|| = raiz_de_2 / raiz_de_17 = 0.3429971702850177

# Erro absoluto com um valor:

# x = 1,48965887 e 𝑥ҧ = 1,38

# Erro absoluto: |𝑥 − 𝑥ҧ| = 0,10965887

# Erro relativo: |𝑥 − 𝑥ҧ| / | x | = 0,10965887 / 1,48965887

# print(0.10965887 / 1.48965887)

print('\n')

# Aproximadamente: 7,3%

# Entrando com informações:

valor1 = float(input('Informe o valor de x: '))
valor_x_linha = float(input('Informe o valor de x linha: '))
print('\n')

try:
    op = str(input('x terá outro valor? [s] ou [n]? Isto implicará em mais um valor para x_linha... '))
    print('\n')
    if op == 's':
        valor2 = float(input('Informe o segundo valor de x: '))
        print('\n')
        valor_x_linha2 = float(input('Informe o segundo valor de x linha: '))
        print('\n')
        a = valor1 - valor_x_linha
        print(f'O resultado de ||x-𝑥ҧ|| é: {a}')
        print('\n')
        b = valor2 - valor_x_linha2
        print(f'O resultado de ||x-𝑥ҧ|| é: {b}')
        print('\n')
        print(f'Temos [{a};{b}]')
        print('\n')
        erro_absoluto = math.pow((a * a) + (b * b), 1/2)
        print(f'O erro absoluto é: \033[32m{erro_absoluto}\033[m')
        print('\n')
        erro_relativo = erro_absoluto / math.pow(((valor1 * valor1) + (valor2 * valor2)), 1/2)
        print(f'O erro relativo é: \033[32m{erro_relativo}\033[m')
    elif op == 'n':
        erro_absoluto_simples = valor1 - valor_x_linha
        print(f'O erro absoluto é: \033[31m{erro_absoluto_simples}\033[m')
        print('\n')
        erro_relativo_simples = erro_absoluto_simples / valor1
        print(f'O erro realtivo é: \033[31m{erro_relativo_simples}\033[m')
except (ValueError, TypeError):
    print(print('Tivemos um problema de: tipos de dados ou opção diferente de s ou n que você digitou! '
                'Necessário que seja uma string!'))
