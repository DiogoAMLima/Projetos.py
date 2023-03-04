def musica_janela():  # Inicializando a função
    import webbrowser
    print('\nOrientação para pegar o caminho: clicar no arquivo, botão direito, propriedades. '
          'Clicar em segurança, copiar o endereço de nome do objeto\n')
    caminho = str(input('Informe o caminho da música no diretório: '))
    webbrowser.open(rf'{caminho}')  # Basta informarmos o caminho para o método open


# musica_janela()


def playsound():  # Inicializando a função
    import playsound
    print('\nOrientação para pegar o caminho: clicar no arquivo, botão direito, propriedades. '
          'Clicar em segurança, copiar o endereço de nome do objeto\n')
    musica = str(input('Informe o caminho da música no diretório: '))

    try:  # Tratamento de erros
        playsound.playsound(rf'{musica}')  # Basta informarmos o caminho para o método playsound
    except KeyboardInterrupt:
        print('\n\033[31mUsuário interrompeu a música\033[m')


# playsound()


def mixer_pygame():  # Inicializando a função
    import pygame
    print('\nOrientação para pegar o caminho: clicar no arquivo, botão direito, propriedades. '
          'Clicar em segurança, copiar o endereço de nome do objeto\n')
    musica = str(input('Informe o caminho da música no diretório: '))

    pygame.mixer.init()  # Iniciando o mixer
    pygame.init()  # Iniciando
    pygame.mixer.music.load(f'{musica}')  # Carregando a música
    pygame.mixer.music.play()  # Tocando a música
    pygame.event.wait()  # Retorna o evento da fila, no caso a música 


# mixer_pygame()

print('\033[34mA seguir, mostraremos as opções:\033[m '
      '\n\033[31m1 - Função musica_janela()\033[m'
      '\n\033[33m2 - Função playsound()\033[m'
      '\n\033[35m3 - Função mixer_pygame()\033[m ')

while True:  # Lopping para escolhermos qual libray usar para ouvirmos a música enquanto quisermos
    try:  # Tratamento de erros
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
