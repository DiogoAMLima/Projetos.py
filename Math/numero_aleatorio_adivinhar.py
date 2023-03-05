from random import randint

print('\033[31m—\033[m' * 18, '\033[97mNÚMERO ALEATÓRIO\033[m', '\033[31m—\033[m' * 18)

i = 0
pontos = 0
while i < 3:  # Laço de repetição
    aleatorio = randint(1, 5)  # Número aleatório entre 1 e 5
    numero = int(input("\nInforme o número que você acha que foi sorteado entre 1 e 5... "))
    if numero == aleatorio:  # Verificando se o número escolhido é igual ao sorteado
        print(f'\n\033[32mVocê acertou, número escolhido: {numero} = número sorteado: {aleatorio}\033[m')
        pontos += 1
        print(f'\n\033[33mVocê ganhou um ponto e agora tem {pontos} ponto(s)\033[m')
    else:
        print(f'\n\033[97mNão foi dessa vez, número escolhido: {numero} != número sorteado: {aleatorio}\033[m')
        pontos -= 1
        print(f'\n\033[31mVocê perdeu um ponto e agora tem {pontos} ponto(s)\033[m')

    aleatorio2 = randint(0, 10)  # Número aleatório entre 1 e 10
    numero2 = int(input("\nInforme o número que você acha que foi sorteado entre 0 e 10... "))
    if numero2 == aleatorio2:  # Verificando se o número escolhido é igual ao sorteado
        print(f'\n\033[32mVocê acertou, número escolhido: {numero2} = número sorteado: {aleatorio2}\033[m')
        pontos += 1
        print(f'\n\033[33mVocê ganhou um ponto e agora tem {pontos} ponto(s)\033[m')
    else:
        print(f'\n\033[97[mNão foi dessa vez, número escolhido: {numero2} != número sorteado: {aleatorio2}\033[m')
        pontos -= 1
        print(f'\n\033[31mVocê perdeu um ponto e agora tem {pontos} ponto(s)\033[m')

    i += 1  # Incremento da variável do looping

print(f'\n\033[34mVocê terminou com {pontos} pontos\033[m\n')

print('\033[35m—\033[m' * 45)  # Multiplicando o texto dentro de '', no caso é uma barra: —
