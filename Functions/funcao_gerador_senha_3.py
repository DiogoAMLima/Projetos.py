import random


def cracker_password():
    all_character = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*/\?:"
    character_list = list(all_character)

    password = input("Digite sua senha: ")

    cracker = ''

    i = 0

    while cracker != password:
        cracker = random.choices(character_list, k=len(password))
        print(f"\033[31m-=\033[m" * 10 + f"\033[35m{str(cracker)}\033[m" + "\033[31m-=\033[m" * 10)
        i += 1
        if cracker == list(password):
            print("\nSua senha é: " + "".join(cracker))
            break

    print(f'\nDemorou \033[34m{i}\033[m tentativas para descobrir a sua senha!')


cracker_password()
