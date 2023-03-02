# Definindo as funções com os respectivos cálculos de conversão:

def celsius_kelvin():
    try:  # Tratamento de erros
        C = float(input('\nInforme o valor em Celsius: '))
        K = C + 273
        print(f'\nO valor de \033[31m{C}\033[m em Kelvin é: \033[32m{K:.2f}\033[m\n')
    except (ValueError, TypeError):  # Tratamento de erros
        print('\n\033[97mTipo de dados incorreto, deveria ser um float...\033[m\n')


def kelvin_celsius():
    try:  # Tratamento de erros
        K = float(input('\nInforme o valor em Kelvin: '))
        C = K - 273
        print(f'\nO valor de \033[33m{K}\033[m em Celsius é: \033[34m{C:.2f}\033[m\n')
    except (ValueError, TypeError):  # Tratamento de erros
        print('\n\033[97mTipo de dados incorreto, deveria ser um float...\033[m\n')


def celsius_fahrenheit():
    try:  # Tratamento de erros
        C = float(input('\nInforme o valor em Celsius: '))
        resultado = C / 5
        F = (resultado * 9) + 32
        print(f'\nO valor de \033[35m{C}\033[m em Fahrenheit é: \033[36m{F:.2f}\033[m\n')
    except (ValueError, TypeError):  # Tratamento de erros
        print('\n\033[97mTipo de dados incorreto, deveria ser um float...\033[m\n')


def fahrenheit_celsius():
    try:  # Tratamento de erros
        F = float(input('\nInforme o valor em Fahrenheit: '))
        resultado = (F - 32) / 9
        C = resultado * 5
        print(f'\nO valor de \033[37m{F}\033[m em Celsius é: \033[97m{C:.2f}\033[m\n')
    except (ValueError, TypeError):  # Tratamento de erros
        print('\n\033[97mTipo de dados incorreto, deveria ser um float...\033[m\n')


def kelvin_fahrenheit():
    try:  # Tratamento de erros
        K = float(input('\nInforme o valor em Kelvin: '))
        resultado = (K - 273) / 5
        F = (resultado * 9) + 32
        print(f'\nO valor de \033[30m{K}\033[m em Fahrenheit é: \033[34m{F:.2f}\033[m\n')
    except (ValueError, TypeError):  # Tratamento de erros
        print('\n\033[97mTipo de dados incorreto, deveria ser um float...\033[m\n')


def fahrenheit_kelvin():
    try:  # Tratamento de erros
        F = float(input('\nInforme o valor em Fahrenheit: '))
        resultado = (F - 32) / 9
        K = (resultado * 5) + 273
        print(f'\nO valor de \033[33m{F}\033[m em Kelvin é: \033[35m{K:.2f}\033[m\n')
    except (ValueError, TypeError):  # Tratamento de erros
        print('\n\033[97mTipo de dados incorreto, deveria ser um float...\033[m\n')


while True:  # Laço de repetição para escolha da conversão de temperatura
    print('\033[31m——————ESCOLHA UMAS DAS OPÇÕES ABAIXO——————\033[m ')
    print('\n(1) - Para calcular Celsius para Kelvin')
    print('\n(2) - Para calcular Kelvin para Celsius')
    print('\n(3) - Para calcular Celsius para Fahrenheit')
    print('\n(4) - Para calcular Fahrenheit para Celsius')
    print('\n(5) - Para calcular Kelvin para Fahrenheit')
    print('\n(6) - Para calcular Fahrenheit para Kelvin')
    print('\n() - Qualquer valor diferente de 1 a 6')
    try:  # Tratamento de erros
        op = float(input('\nInforme uma das opções acima: '))
        if op >= 7 or op <= 0:  # Excluindo opções que não estejam entre 1 e 6
            print('\n\033[33mNão temos essa opção...\033[m')
            break
        else:
            if op == 1:
                celsius_kelvin()
            elif op == 2:
                kelvin_celsius()
            elif op == 3:
                celsius_fahrenheit()
            elif op == 4:
                fahrenheit_celsius()
            elif op == 5:
                kelvin_fahrenheit()
            else:
                fahrenheit_kelvin()
    except KeyboardInterrupt:  # Tratamento de erros
        print('\n\n\033[33mO(a) Usuário(a) interrompeu a entrada de dados...\033[m')
        break
