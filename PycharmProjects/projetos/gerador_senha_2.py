import random
import time

print("\033[32m———————— GERADOR DE SENHA ————————\033[m")

num = "0123456789"  # Números disponíveis para formação de senha

caracteres_especiais = r"!@#$%&*/\?:"
# Caracteres especiais disponíveis (r na frente para o python ler exatamente o que está dentro das aspas)

letra_minuscula = "abcdefghijklmnopqrstuvwxyz"  # Todas as letras minúsculas possíveis

letra_maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Todas as letras maiúsculas possíveis

juntando = num + caracteres_especiais + letra_minuscula + letra_maiuscula  # Juntando em uma string

# Método join() -> O método join() é um método de string e retorna uma string na qual os
# elementos da sequência foram unidos por um separador str.

# Método sample() -> sample() é uma função embutida de módulo aleatório em Python que retorna uma lista de comprimento
# particular de itens escolhidos da sequência, ou seja, lista, tupla, string ou conjunto. Usado para amostragem
# aleatória sem reposição. Parâmetros: sequência : pode ser uma lista, tupla, string ou conjunto.

try:
    tamanho_da_senha = int(input('Informe a quantidade de caracteres: '))
    print(f'A quantidade de caracteres escolhida foi: {tamanho_da_senha}\n')
    senha = "".join(random.sample(juntando, tamanho_da_senha))
    print('\033[31mEstamos gerando sua senha, por favor aguarde...\033[m\n')
    time.sleep(4)
    print(f'\033[34mSua senha é:\033[m {senha}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou! Necessário que seja um número inteiro!')
