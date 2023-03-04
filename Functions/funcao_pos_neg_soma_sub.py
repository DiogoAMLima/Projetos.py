def pos_soma(n):  # Função com parâmetro
    if n < 0:
        print(f'\nNúmero digitado \033[31m{n}\033[m é negativo...')
    else:
        s = 0
        while n != 0:  # Enquanto o número não for igual a 0, a soma continua e a subtração também
            s += n
            n -= 1
        return s


valor = float(input('Informe um valor positivo: '))
print(f'\nO resultado da soma é: \033[34m{pos_soma(valor)}\033[m ')  # Colocando o valor informando na função


def neg_sub(n):  # Função com parâmetro
    if n > 0:
        print(f'\nNúmero digitado \033[31m{n}\033[m é positivo...')
    else:
        s = 0
        while n != 0:  # Enquanto o número não for igual a 0, as somas continuam
            s += n
            n += 1
        return s


valor2 = float(input('\nInforme um valor negativo: '))
print(f'\nO resultado da subtração é: \033[35m{neg_sub(valor2)}\033[m')  # Colocando o valor informando na função
