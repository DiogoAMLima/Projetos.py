from rich import print
import os

# Constantes:

votos_char, votos_char2, votos_char3 = 0, 0, 0

character = str(input('Informe o nome do personagem: '))
character2 = str(input('Informe o nome do personagem: '))
character3 = str(input('Informe o nome do personagem: '))

limite = int(input('\nEscolha o tamanho da borda entre os totais de votos: '))

# Looping:

while True:
    print('—' * limite)
    print(f'\n[on blue]Total de votos no {character}:[/] {votos_char}{os.linesep}[on green]Total de votos no {character2}:[/] '
          f'{votos_char2}{os.linesep}[on red]Total de votos no {character3}: {votos_char3}{os.linesep}[/]')
    # os.linesep para quebrar linha em qualquer SO
    print('—' * limite)
    # Votação:
    try:
        vote = int(input(f'Vote no seu personagem preferido de One Piece dos chapéus de palha:{os.linesep}1 - {character}'
                         f'{os.linesep}2 - {character2}{os.linesep}3 - {character3}{os.linesep}Informe o número para seu voto: '))
        if vote == 1:
            votos_char += 1
        elif vote == 2:
            votos_char2 += 1
        elif vote == 3:
            votos_char3 += 1
        else:
            pass
    except(TypeError, ValueError, KeyboardInterrupt):
        print('O(A) usuário(a) interrompeu a entrada de dados ou digitou um valor errado...')
    os.system('cls')  # Apagando o terminal
