print('\033[36m——————————————————————————— SOMA MÚLTIPLOS DE 4 ———————————————————————————\033[m')
qntd_numeros = 0
soma_numeros = 0
m_4 = []
for cont in range(0, 1001):  # Looping de 0 a 1000
    if cont % 4 == 0:  # Verificando se é múltiplo de 4
        qntd_numeros += + 1
        m_4.append(cont)
        # Variável para receber a quantidade de números que são múltiplos de 4
        soma_numeros += cont
        # Soma dos múltiplos de 4
print(f'\nA quantidade de números é: \033[33m{qntd_numeros}\033[m e a soma desses números é: '
      f'\033[32m{soma_numeros}\033[m\n')

j = 0
for i in m_4:  # Mostrando os valores que são múltiplos de 4 
    print(f'\nMúltiplo de 4: \033[34m{m_4[j]}\033[m')
    j += 1
print('\n\033[31m—\033[m' * 75)
