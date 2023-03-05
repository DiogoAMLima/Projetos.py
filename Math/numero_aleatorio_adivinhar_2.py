from random import randint

print('\033[35m—\033[m' * 18, '\033[97mNÚMERO ALEATÓRIO\033[m', '\033[35m—\033[m' * 18)

tentativas = 0
right = False  # Variável booleana
while not right:  # Lopping: enquanto não for False, o looping continua
    aleatorio = randint(1, 10)
    numero = int(input("\nInforme o número que você acha que foi sorteado entre 1 e 10... "))
    if numero == aleatorio:  # Verificando se o número escolhido é igual ao número sorteado
        right = True  # Se a condição acima for verdade, o looping será encerrado
        print(f'\n\033[36mVocê acertou, número escolhido: {numero} = número sorteado: {aleatorio}\033[m')
        tentativas += 1  # Incremento do iterador
        print(f'\nVocê tentou \033[31m{tentativas}\033[m vezes')
    else:
        print(f'\n\033[33mNão foi dessa vez, número escolhido: {numero} != número sorteado: {aleatorio}\033[m')
        tentativas += 1  # Incremento do iterador
        print(f'\nVocê tentou \033[37m{tentativas}\033[m vezes')

print()
print('\033[35m—\033[m' * 45)  # Multiplicando o texto dentro de '', no caso é uma barra: —
