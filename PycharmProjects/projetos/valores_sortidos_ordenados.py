from random import randint
from time import sleep
from operator import itemgetter

jogador1 = str(input('Informe o nome do primeiro jogador: '))
jogador2 = str(input('Informe o nome do segundo jogador: '))
jogador3 = str(input('Informe o nome do terceiro jogador: '))
jogador4 = str(input('Informe o nome do quarto jogador: '))

a = int(input('\nInforme o valor inicial que pode ser sorteado: '))
b = int(input('Informe até que valor pode ser sorteado: '))

jogo = {f'\033[31m{jogador1}\033[m': randint(a, b),
        f'\033[32m{jogador2}\033[m': randint(a, b),
        f'\033[33m{jogador3}\033[m': randint(a, b),
        f'\033[34m{jogador4}\033[m': randint(a, b)}

ranking = []

print('\n\033[37mVALORES SORTEADOS:\033[m ')
for chave, valor in jogo.items():  # .items = retorna uma lista com os dois valores (chave e valor)
    print(f'\n{chave} tirou \033[36m{valor}\033[m')
    sleep(0.6)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # Ordenar lista de dicionários
print('\n\033[30mRANKING DOS JOGADORES\033[m')
for i, v in enumerate(ranking):
    print(f'\n\033[97m{i+1}º\033[m lugar: {v[0]} com o valor sorteado de: \033[35m{v[1]}.\033[m')
    sleep(0.6)
