from random import randint

print('—' * 18, '\033[35mCORES\033[m', '—' * 18, '\n')

primarias = ('\033[31mVermelho\033[m', '\033[34mAzul\033[m', '\033[33mAmarelo\033[m')
aleatorio = randint(0, 2)  # Número aleatório entre 0 e 2
print("Escolha uma cor:\n"
      "[0] = Vermelho\n"
      "[1] = Azul\n"
      "[2] = Amarelo\n")
escolha = int(input("Qual a sua escolha? "))

print(f"\nCor escolhida aleatoriamente {primarias[aleatorio]}")

print(f"\nSua escolha foi {primarias[escolha]}")

if aleatorio == 0:  # Vermelho
    if escolha == 0:
        print("\nTeremos Vermelho (Cor Primária)")
    elif escolha == 1:
        print("\nTeremos Roxo (Cor Secundária)")
        print("\nAgora com o Roxo, podemos misturar com o Vermelho e teremos uma cor Terciária: Vermelho-Arroxeado!\n")
    elif escolha == 2:
        print("\nTeremos Laranja (Cor Secundária)")
        print("\nAgora com o Laranja, podemos misturar com o Vermelho e teremos uma cor Terciária: Vermelho-Alaranjado!\n")
    else:
        print("\n\033[31mOpção inválida\033[m")
elif aleatorio == 1:  # Azul
    if escolha == 0:
        print("\nTeremos Roxo (Cor Secundária)")
        print("\nAgora com o Roxo, podemos misturar com o Azul e teremos uma cor Terciária: Azul-Arroxeado!\n")
    elif escolha == 1:
        print("\nTeremos Azul (Cor Primária)")
    elif escolha == 2:
        print("\nTeremos Verde (Cor Secundária)")
        print("\nAgora com o Verde, podemos misturar com o Azul e teremos uma cor Terciária: Azul-Esverdeado!\n")
    else:
        print("\n\033[31mOpção inválida\033[m")
elif aleatorio == 2:  # Amarelo
    if escolha == 0:
        print("\nTeremos Laranja (Cor Secundária)")
        print("\nAgora com o Laranja, podemos misturar com o Amarelo e teremos uma cor Terciária: Amarelo-Alaranjado!\n")
    elif escolha == 1:
        print("\nTeremos Verde (Cor Secundária)")
        print("\nAgora com o Verde, podemos misturar com o Amarelo e teremos uma cor Terciária: Amarelo-Esverdeado!\n")
    elif escolha == 2:
        print("\nTeremos Amarelo (Cor Primária)")
    else:
        print("\n\033[31mOpção inválida\033[m")

print('\033[36m—\033[m' * 80)
