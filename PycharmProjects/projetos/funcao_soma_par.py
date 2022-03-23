print('-----------------------------FUNÇÃO SOMA PARES-----------------------------\n')


def soma_pares(vetor1):
    soma_par = 0
    for num in vetor1:
        if num % 2 == 0:
            soma_par = soma_par + num
    return soma_par


vetor1 = [4, 8, 12, 32, 45, 45, 8]
soma_final = soma_pares(vetor1)
print("O resultado da soma dos elementos contidos no vetor é: {}".format(soma_final))

print('\n')

print('-----------------------------------------------------------------------------')
