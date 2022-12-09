import random
import time

print("\033[32m———————— LOPP DE GERADOR DE SENHA ————————\033[m")

num = "0123456789"

caracteres_especiais = r"!@#$%&*/\?:"

letra_minuscula = "abcdefghijklmnopqrstuvwxyz"

letra_maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

juntando = num + caracteres_especiais + letra_minuscula + letra_maiuscula

while True:
    op = str(input('\nPara continuarmos o procedimento, pressione qualquer tecla ou s para sair... ')).strip()
    if op == 's':
        print('\n\033[33mFinalizando...\033[m')
        break
    else:
        try:
            tamanho_da_senha = int(input('\nInforme a quantidade de caracteres: '))
            print(f'\nA quantidade de caracteres escolhida foi: \033[34m{tamanho_da_senha}\033[m\n')
            senha = "".join(random.sample(juntando, tamanho_da_senha))
            print('\033[31mEstamos gerando sua senha, por favor aguarde...\033[m\n')
            time.sleep(4)
            print(f'\033[34mSua senha é:\033[m \033[35m{senha}\033[m')
        except (ValueError, TypeError):
            print('Tivemos um problema com os tipos de dados que você digitou! Necessário que seja um número inteiro!')
