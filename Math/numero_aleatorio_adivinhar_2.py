from random import randint
print('--------------------------------NÚMERO ALEATÓRIO 2--------------------------------')

print('\n')

tentativas = 0
right = False
while not right:
    aleatorio = randint(1, 10)
    numero = int(input("Informe o número que você acha que foi sorteado entre 1 e 10... "))
    if numero == aleatorio:
        right = True
        print(f'Você acertou, {numero} = {aleatorio}')
        tentativas += 1
        print(f'Você tentou {tentativas} vezes')
    else:
        print(f'Não foi dessa vez, {numero} != {aleatorio}')
        tentativas += 1
        print(f'Você tentou {tentativas} vezes')

print('\n')

print('----------------------------------------------------------------------------------')
