def log():  # Definindo a função
    import math  # Necessário importar a library math para utilizarmos os métodos já existentes
    logaritmo = float(input('Informe um número para saber o log: '))
    log_base = float(input('Informe a base do log: '))
    print(f'O resultado do log \033[31m{logaritmo}\033[m na base \033[34m{log_base}\033[m é: '
          f'\033[37m{math.log(logaritmo, log_base)}\033[m')  # Utilizando o método com a base escolhida
    logaritmo2 = float(input('\nInforme mais um número para saber o log na base 10: '))
    print(f'O resultado do log \033[32m{logaritmo2}\033[m na base 10 é: \033[36m{math.log10(logaritmo2)}\033[m')
    # Utilizando o método com a base 10
    logaritmo3 = float(input('\nInforme outro número para saber o log na base 2: '))
    print(f'O resultado do log \033[33m{logaritmo3}\033[m na base 2 é: \033[35m{math.log2(logaritmo3)}\033[m')
    # Utilizando o método com a base 2


log()
