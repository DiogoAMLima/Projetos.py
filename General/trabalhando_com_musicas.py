import playsound
import pygame
import webbrowser

# AJUDA: 'https://www.delftstack.com/pt/howto/python/python-play-mp3/#:~:text=playsound%20e%20webbrowser%20.-,
# Tocar%20arquivos%20MP3%20com%20Python%20usando%20o%20pacote%20playsound,wav%20.'

# If you need to solve a problem with VLC: https://stackoverflow.com/questions/59014318/filenotfounderror-could-not-
# find-module-libvlc-dll

# MÚSICAS:

# 1° forma (com playsound):

# musica = r'C:/Users/Pichau/Downloads/Musicas/blackorwhite.mp3'
#
# try:
#     playsound.playsound(f'{musica}')
# except KeyboardInterrupt:
#     print('\033[31mUsuário interrompeu a música\033[m')

# 2° forma (com pygame):

# musica2 = r'C:/Users/Pichau/Downloads/Musicas/KygoFirestoneInstrumental.mp3'
#
# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load(f'{musica2}')
# pygame.mixer.music.play()
# pygame.event.wait()

# 3° forma (janela no navegador):

# webbrowser.open(r'C:/Users/Pichau/Downloads/Musicas/KygoFirestoneInstrumental.mp3')
