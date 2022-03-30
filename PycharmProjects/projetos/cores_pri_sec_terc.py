from random import randint

print('---------------------------------------------------CORES---------------------------------------------------\n')

primarias = ('Vermelho', 'Azul', 'Amarelo')
aleatorio = randint(0, 2)
print("Escolha uma cor:\n"
      "[0] = Vermelho\n"
      "[1] = Azul\n"
      "[2] = Amarelo\n")
escolha = int(input("Qual a sua escolha? "))

print('\n')

print("Cor escolhida aleatoriamente {}".format(primarias[aleatorio]))

print("\n")

print("Sua escolha foi {}".format(primarias[escolha]))

print("\n")

if aleatorio == 0:  # Vermelho
    if escolha == 0:
        print("Teremos Vermelho (Cor Primária)")
    elif escolha == 1:
        print("Teremos Roxo (Cor Secundária)")
        print("Agora com o Roxo, podemos misturar com o Vermelho e teremos uma cor Terciária: Vermelho-Arroxeado!")
    elif escolha == 2:
        print("Teremos Laranja (Cor Secundária)")
        print("Agora com o Laranja, podemos misturar com o Vermelho e teremos uma cor Terciária: Vermelho-Alaranjado!")
    else:
        print("Opção inválida")
elif aleatorio == 1:  # Azul
    if escolha == 0:
        print("Teremos Roxo (Cor Secundária)")
        print("Agora com o Roxo, podemos misturar com o Azul e teremos uma cor Terciária: Azul-Arroxeado!")
    elif escolha == 1:
        print("Teremos Azul (Cor Primária)")
    elif escolha == 2:
        print("Teremos Verde (Cor Secundária)")
        print("Agora com o Verde, podemos misturar com o Azul e teremos uma cor Terciária: Azul-Esverdeado!")
    else:
        print("Opção inválida")
elif aleatorio == 2:  # Amarelo
    if escolha == 0:
        print("Teremos Laranja (Cor Secundária)")
        print("Agora com o Laranja, podemos misturar com o Amarelo e teremos uma cor Terciária: Amarelo-Alaranjado!")
    elif escolha == 1:
        print("Teremos Verde (Cor Secundária)")
        print("Agora com o Verde, podemos misturar com o Amarelo e teremos uma cor Terciária: Amarelo-Esverdeado!")
    elif escolha == 2:
        print("Teremos Amarelo (Cor Primária)")
    else:
        print("Opção inválida")

print('\n')

print('-------------------------------------------------------------------------------------------------------------')
