import random

# Escolhendo todos os caracteres

all_character = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*/\?:"
character_list = list(all_character)  # Colocando em uma lista

password = input("Digite sua senha: ")

cracker = ''

i = 0  # Iterador

while cracker != password:  # Enquanto o cracker for diferente da senha escolhida o looping continua
    cracker = random.choices(character_list, k=len(password))  # Retorna uma lista de caracteres selecionados de
    # acordo com o tamanho passado a constante k, que é o tamanho da nossa lista
    print(f"\033[31m-=\033[m" * 10 + f"\033[35m{str(cracker)}\033[m" + "\033[31m-=\033[m" * 10)
    i += 1  # Iterador para descobrirmos no final, quantas vezes tentamos "quebrar a senha"
    if cracker == list(password):  # Se o cracker for igual a lista ao password (transformado em lista)
        print("\nSua senha é: " + "".join(cracker))  # Juntando o cracker com sua senha é:
        break

print(f'\nDemorou \033[34m{i}\033[m tentativas para descobrir a sua senha!')
