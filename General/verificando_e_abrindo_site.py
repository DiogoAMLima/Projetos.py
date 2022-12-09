import urllib.request
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

tempo = int(input('Informe quando tempo (segundos) o site deverá ficar aberto: '))

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except urllib.error.URLError:
    print('O site GOOGLE não está acessível no momento.')
else:
    print('Consegui, o GOOGLE está acessível.')
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get("https://google.com")
    sleep(tempo)
