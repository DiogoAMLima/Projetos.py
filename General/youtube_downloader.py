# pip install pytube

from pytube import YouTube

# Funções para baixarmos os vídeos ou somente áudio:


def download_youtube(link):  # Inicializando a função que recebe o link do YouTube como parâmetro
    objeto = YouTube(link)  # Instânciando a classe com o link
    objeto = objeto.streams.get_highest_resolution()  # Vídeo em alta resolução
    try:  # Tratamento de erros
        objeto.download()  # Tentando baixar
    except (ValueError, TypeError):
        print("\033[31mTivemos algum problema com o download do vídeo, verifique a URL\033[m")
    print("\n\033[33mO vídeo foi baixado com sucesso!!!\033[m")


link = str(input("\n\033[34mDigite seu link:\033[m "))

download_youtube(link)  # Chamando a função para baixar o vídeo


def download_audio(link2):  # Inicializando a função que recebe o link 2 do YouTube como parâmetro
    objeto2 = YouTube(link2)  # Instânciando a classe com o link 2
    objeto2 = objeto2.streams.get_audio_only()  # Apenas áudio
    try:  # Tratamento de erros
        objeto2.download()  # Tentando baixar
    except (ValueError, TypeError):
        print("\033[31mTivemos algum problema com o download do áudio, verifique a URL\033[m")
    print("\n\033[35mO áudio do vídeo foi baixado com sucesso!!!\033[m")


link2 = str(input("\n\033[36mDigite seu link:\033[m "))

download_audio(link2)  # Chamando a função para baixar o áudio
