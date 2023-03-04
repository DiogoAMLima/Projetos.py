import random


def cracker_password():  # Definindo a função
    all_character = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*/\?:"
    # Definindo os caracteres
    character_list = list(all_character)  # Colocando em uma lista os caracteres definidos

    password = input("Digite sua senha: ")

    cracker = ''

    i = 0
    # Looping que só para quando o cracker descobrir a senha (quando cracker for igual a password)
    while cracker != password:
        cracker = random.choices(character_list, k=len(password))  # Definindo nosso cracker com o .choices novamente
        print(f"\033[31m-=\033[m" * 10 + f"\033[35m{str(cracker)}\033[m" + "\033[31m-=\033[m" * 10)  # Passando para str
        i += 1
        if cracker == list(password):  # Se a variável cracker for igual a senha informada
            # que está em como tipo de lista, o código para e informa a que descobriu sua senha
            print("\nSua senha é: " + "".join(cracker))
            break

    print(f'\nDemorou \033[34m{i}\033[m tentativas para descobrir a sua senha!')


cracker_password()
