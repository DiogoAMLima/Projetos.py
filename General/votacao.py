# Votação:

# Variaveis:

character = str(input('Informe o nome do personagem: '))
character2 = str(input('Informe o nome de outro personagem: '))
character3 = str(input('Informe o nome de mais um personagem: '))

limite = int(input('\nEscolha o tamanho da borda entre os totais de votos: '))

votos_char, votos_char2, votos_char3 = 0, 0, 0

# Looping:

while True:
    print()
    print('\033[97m—\033[m' * limite)
    print(f'\033[32mTotal de votos em {character}\033[m: \033[35m{votos_char}\033[m\n'
          f'\033[33mTotal de votos em {character2}\033[m: \033[35m{votos_char2}\033[m\n'
          f'\033[34mTotal de votos em {character3}\033[m: \033[35m{votos_char3}\033[m')
    print('\033[97m—\033[m' * limite)
    # Votação:
    try:
        vote = int(input(f'\nVote em um dos personagens preferido digitados acima ou 0 para sair:\n\n1 - {character}\n'
                         f'2 - {character2}\n3 - {character3}\n\nInforme o número para seu voto: '))
        if vote == 0:
            print('\n\033[31mAté a próxima...\033[m')
            break
        elif vote == 1:
            votos_char += 1
        elif vote == 2:
            votos_char2 += 1
        elif vote == 3:
            votos_char3 += 1
        else:
            pass
    except(TypeError, ValueError, KeyboardInterrupt):
        print('\n\033[31mO(A) usuário(a) interrompeu a entrada de dados ou digitou um valor errado...\033[m')
    print('\n' * 50)  # "Limpando a tela"
