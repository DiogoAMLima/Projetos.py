# pip install pytube

from pytube import YouTube

# Funções para baixarmos os vídeos ou somente áudio:


def download_youtube(link):
    objeto = YouTube(link)
    objeto = objeto.streams.get_highest_resolution()
    try:
        objeto.download()
    except (ValueError, TypeError):
        print("\033[31mTivemos algum problema com o download do vídeo, verifique a URL\033[m")
    print("\n\033[33mO vídeo foi baixado com sucesso!!!\033[m")


link = str(input("\n\033[34mDigite seu link:\033[m "))

download_youtube(link)


def download_audio(link2):
    objeto2 = YouTube(link2)
    objeto2 = objeto2.streams.get_audio_only()
    try:
        objeto2.download()
    except (ValueError, TypeError):
        print("\033[31mTivemos algum problema com o download do áudio, verifique a URL\033[m")
    print("\n\033[35mO áudio do vídeo foi baixado com sucesso!!!\033[m")


link2 = str(input("\n\033[36mDigite seu link:\033[m "))

download_audio(link2)
