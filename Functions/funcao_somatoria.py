# Primeiro exemplo:


def funcao_somatorio_x_x2(n2):
    soma2 = 0
    for i in range(n2):
        x = i + 2
        soma2 += 2 * x + 3 * x ** 2
    return soma2


print(f'O resultado da primeira função somatória é: \033[31m{funcao_somatorio_x_x2(3)}\033[m')

# Como funciona:

# Primeira vez que rodar:
# 1: x = 2: 4 + 12 = 16

# Segunda vez que rodar:
# 2: x = 3: 6 + 27 = 33

# Terceira vez que rodar:
# 3: x = 4: 8 + 48 = 56

# Somando 56 + 33 + 16 = 105

print()

# Interação com o usuário:


def funcao_de_somatorio(qntd_vezes):
    try:
        qntd_vezes = int(input('Informe quantas vezes o loop deve ser feito: '))  # Usuário escolhendo o núemro do loop
        soma = 0
        for i in range(qntd_vezes):
            y = i + 3  # i começa em 0 e vai até o loop escolhido pelo usuário - 1
            soma += 2 * y + 2 * y ** 2
            # Se o usuário escolheu 2, então o código rodará duas vezes com o y valendo 0 e depois 1
        return soma
    except (TypeError, ValueError):
        print('\n\033[31mTivemos um problema com os tipos de dados que você digitou, '
              'deveria ser um dado tipo inteiro!\033[m')


print(f'\nO resultado da segunda função somatória é: \033[35m{funcao_de_somatorio(qntd_vezes=True)}\033[m')

# Como funciona:

# Primeira vez que rodar:
# 1: y = 3: 6 + 18 = 24

# Segunda vez que rodar:
# 2: y = 4: 8 + 32 = 40

# Somando 24 com 40 temos 64
