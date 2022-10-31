def pos_soma(n):  # Função com parâmetro
    if n < 0:
        print(f'Número digitado \033[31m{n}\033[m é negativo...')
    else:
        s = 0
        while n != 0:
            s += n
            n -= 1
        return s


valor = float(input('Informe um valor: '))
print(f'\nO resultado da soma é: \033[34m{pos_soma(valor)}\033[m ')


def neg_sub(n):  # Função com parâmetro
    if n > 0:
        print(f'Número digitado \033[31m{n}\033[m é positivo...')
    else:
        s = 0
        while n != 0:
            s += n
            n += 1
        return s


valor2 = float(input('\nInforme outro valor: '))
print(f'\nO resultado da subtração é: \033[35m{neg_sub(valor2)}\033[m')
