def fatorial(n):  # Função com parâmetro
    f = 1
    for valor in range(n, 0, -1):  # Será feito o for do número digitado até 1
        print(f'\033[31m{valor}\033[m', end='')  # Mostrando cada valor do número digitado até 1
        if valor > 1:
            print(' \033[36mx\033[m ', end='')  # Símbolo de x entre cada valor mostrado
        else:
            print(' \033[97m=\033[m ', end='')  # Símbolo de igual
        f *= valor
    return f


numero = int(input('Informe um valor para calcular o fatorial: '))
print(f'\033[33m{fatorial(numero)}\033[m')  # Resultado
