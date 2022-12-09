from random import randint
print('--------------------------------NÚMERO ALEATÓRIO--------------------------------')

print('\n')

i = 0
pontos = 0
while i < 3:
    aleatorio = randint(1, 5)
    numero = int(input("Informe o número que você acha que foi sorteado entre 1 e 5... "))
    if numero == aleatorio:
        print(f'Você acertou, {numero} = {aleatorio}')
        pontos += 1
        print(f'Você ganhou um ponto e agora tem {pontos} ponto(s)')
    else:
        print(f'Não foi dessa vez, {numero} != {aleatorio}')
        pontos -= 1
        print(f'Você perdeu um ponto e agora tem {pontos} ponto(s)')

    print('\n')

    aleatorio2 = randint(0, 10)
    numero2 = int(input("Informe o número que você acha que foi sorteado entre 0 e 10... "))
    if numero2 == aleatorio2:
        print(f'Você acertou, {numero2} = {aleatorio2}')
        pontos += 1
        print(f'Você ganhou um ponto e agora tem {pontos} ponto(s)')
    else:
        print(f'Não foi dessa vez, {numero2} != {aleatorio2}')
        pontos -= 1
        print(f'Você perdeu um ponto e agora tem {pontos} ponto(s)')

    print('\n')
    i += 1

print(f'Você terminou com {pontos} pontos')

print('----------------------------------------------------------------------------------')
