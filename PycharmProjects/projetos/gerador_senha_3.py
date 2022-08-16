import random
import time

print("\033[32m———————— LOPP DE GERADOR DE SENHA ————————\033[m")

num = "0123456789"

caracteres_especiais = r"!@#$%&*/\?:"

letra_minuscula = "abcdefghijklmnopqrstuvwxyz"

letra_maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

juntando = num + caracteres_especiais + letra_minuscula + letra_maiuscula

while True:
    op = str(input('Para continuarmos o procedimento, pressione qualquer tecla ou s para sair... '))
    if op == 's':
        print('\033[33mFinalizando...\033[m')
        break
    else:
        try:
            tamanho_da_senha = int(input('\nInforme a quantidade de caracteres: '))
            print(f'A quantidade de caracteres escolhida foi: {tamanho_da_senha}\n')
            senha = "".join(random.sample(juntando, tamanho_da_senha))
            print('\033[31mEstamos gerando sua senha, por favor aguarde...\033[m\n')
            time.sleep(4)
            print(f'\033[34mSua senha é:\033[m {senha}')
            print('\n')
        except (ValueError, TypeError):
            print('Tivemos um problema com os tipos de dados que você digitou! Necessário que seja um número inteiro!')
