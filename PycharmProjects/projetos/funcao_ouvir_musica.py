def musica_janela():
    import webbrowser
    print('\nOrientação para pegar o caminho: clicar no arquivo, botão direito, propriedades. '
          'Clicar em segurança, copiar o endereço de nome do objeto\n')
    caminho = str(input('Informe o caminho da música no diretório: '))
    webbrowser.open(rf'{caminho}')


# musica_janela()


def playsound():
    import playsound
    print('\nOrientação para pegar o caminho: clicar no arquivo, botão direito, propriedades. '
          'Clicar em segurança, copiar o endereço de nome do objeto\n')
    musica = str(input('Informe o caminho da música no diretório: '))

    try:
        playsound.playsound(rf'{musica}')
    except KeyboardInterrupt:
        print('\n\033[31mUsuário interrompeu a música\033[m')


# playsound()


def mixer_pygame():
    import pygame
    print('\nOrientação para pegar o caminho: clicar no arquivo, botão direito, propriedades. '
          'Clicar em segurança, copiar o endereço de nome do objeto\n')
    musica = str(input('Informe o caminho da música no diretório: '))

    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load(f'{musica}')
    pygame.mixer.music.play()
    pygame.event.wait()


# mixer_pygame()


print('\033[34mA seguir, mostraremos as opções:\033[m '
      '\n\033[31m1 - Função musica_janela()\033[m'
      '\n\033[33m2 - Função playsound()\033[m'
      '\n\033[35m3 - Função mixer_pygame()\033[m ')

while True:
    try:
        escolha = str(input('\nEscolha uma das opções disponíveis acima ou 0 para sair: '))
        if escolha == '0':
            print('\n\033[37mFinalizando...\033[m')
            break
        elif escolha == '1':
            musica_janela()
        elif escolha == '2':
            playsound()
        elif escolha == '3':
            mixer_pygame()
        else:
            print('\n\033[32mNão encontramos a função desejada...\033[m')
    except (UnicodeDecodeError, KeyboardInterrupt):
        print('\n\033[36mAperte novamente para sair...\033[m')
