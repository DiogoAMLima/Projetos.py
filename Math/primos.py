try:
    num = int(input('Digite um número para testar se é primo: '))
    res = 0
    for cont in range(1, num + 1):
        if num % cont == 0:
            res += 1
    if res == 2:
        print('\n\033[31mNúmero é primo\033[m')
    else:
        print('\n\033[32mNúmero não é primo\033[m')
except (TypeError, ValueError, KeyboardInterrupt):
    print('\n\033[34mTivermos um problema com o dado digitado ou o(a) usuário(a) interrompeu a entrada de dados.\033[m')
# Laço de repetição para verificar o resto da divisão do número digitado (num) pelo contador (cont).
# O contador irá checar de 1 até: número digitado + 1.
# Exemplo: Se 40 for digitado, ele irá verificar até o número 41, pois, (num + 1) = 41.
# Se resultado for 2 é porque ele foi divisível 2 vezes, caso passe de 2,ou seja, 3 para cima, ele não será primo, pois,
# O número só é primo quando é maior que 1 e é divisível por 1 e ele mesmo.
