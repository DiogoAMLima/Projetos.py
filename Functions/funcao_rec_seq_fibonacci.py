import time


def fibonacci(index):  # Definindo a função e a sequência de fibonacci
    if index == 1:
        return 0
    elif index == 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


while True:  # Laço de repetição para mostrar quantas vezes o/a usuário(a) quiser ver os termos de fibonacci
    try:  # Tratamento de erros
        n = int(input('\nDeseja exibir até qual termo? '))
        print()
    except (ValueError, TypeError):
        print('\033[31mTivemos um problema com os tipos de dados que você digitou! '
              'Necessário que seja um número inteiro!\033[m')
    i = 0
    for valor in range(1, n + 1):
        print(f'\033[36m{i}.° termo:\033[m \033[97m{fibonacci(valor)}\033[m')
        i += 1
        time.sleep(0.5)
    op = str(input('\nDeseja continuar? \033[34m[S/N]\033[m ')).strip().upper()
    if op == 'N':
        print('\n\033[33mFinalizando...\033[m')
        break
    else:
        pass
