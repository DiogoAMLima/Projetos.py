import random
import string
import time


def gerador_senha_2():
    qntd = int(input('Informe quantos caracteres terá a senha: '))

    password = "".join(random.choices(string.printable, k=qntd)).replace(" ", ".")

    print('\n\033[31mEstamos gerando sua senha, por favor aguarde!!!\033[m')
    time.sleep(1.5)

    return print(f'\nSua senha é: \033[34m{password}\033[m')


gerador_senha_2()

