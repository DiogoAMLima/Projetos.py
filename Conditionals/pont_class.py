from random import randint

print("------------------------------------------PONTUAÇÃO E CLASSIFICAÇÃO------------------------------------------\n")

# Declarando as variáveis:

time1 = str(input("Informe o nome do primeiro time: ")).strip().upper()
time2 = str(input("Informe o nome do segundo time: ")).strip().upper()
time3 = str(input("Informe o nome do terceiro time: ")).strip().upper()

pont1 = 0
pont2 = 0
pont3 = 0

i = 0
while i <= 11:  # Laço de repetição
    aleat = randint(0, 2)  # Sorteando um valor
    confr = int(input("\nInforme o confronto desejado: "
                      "[0 = time1 x time2 / 1 = time1 x time 3 / 2 = time2 x time3]: "))  # Escolhendo um valor
    if confr == 0 and aleat == 0:  # Fazendo as comparações e pontuando os times
        print(f'\nO {time1} e o {time2} \033[31mempataram\033[m')
        pont1 += 1
        pont2 += 1
    if confr == 0 and aleat == 1:
        print(f'\nO {time1} \033[32mvenceu\033[m o {time2}')
        pont1 += 3
    if confr == 0 and aleat == 2:
        print(f'\nO {time2} \033[33mvenceu\033[m o {time1}')
        pont2 += 3
    if confr == 1 and aleat == 0:
        print(f'\nO {time1} e o {time3} \033[34mempataram\033[m')
        pont1 += 1
        pont3 += 1
    if confr == 1 and aleat == 1:
        print(f'\nO {time1} \033[35mvenceu\033[m o {time3}')
        pont1 += 3
    if confr == 1 and aleat == 2:
        print(f'\nO {time3} \033[36mvenceu\033[m o {time1}')
        pont3 += 3
    if confr == 2 and aleat == 0:
        print(f'\nO {time2} e o {time3} \033[97mempataram\033[m')
        pont2 += 1
        pont3 += 1
    if confr == 2 and aleat == 1:
        print(f'\nO {time2} \033[30mvenceu\033[m o {time3}')
        pont2 += 3
    if confr == 2 and aleat == 2:
        print(f'\nO {time3} \033[32mvenceu\033[m o {time2}')
        pont3 += 3
    i += 1

# Mostrando os pontos:

print(f'\n\033[0;34mO {time1} terminou com {pont1} pontos\033[m\n')
print(f'\033[0;31mO {time2} terminou com {pont2} pontos\033[m\n')
print(f'\033[0;30mO {time3} terminou com {pont3} pontos\033[m\n')

# Fazendo a classificação:

if pont2 < pont1 > pont3:
    print(f'O \033[31m{time1}\033[m ficou em primeiro\n')
    if pont2 > pont3:
        print(f'O \033[32m{time2}\033[m ficou em segundo\n')
        print(f'O \033[33m{time3}\033[m ficou em terceiro\n')
    else:
        print(f'O \033[34m{time3}\033[m ficou em segundo\n')
        print(f'O \033[35m{time2}\033[m ficou em terceiro\n')
elif pont1 < pont2 > pont3:
    print(f'O \033[36m{time2}\033[m ficou em primeiro\n')
    if pont1 > pont3:
        print(f'O \033[37m{time1}\033[m ficou em segundo\n')
        print(f'O \033[97m{time3}\033[m ficou em terceiro\n')
    else:
        print(f'O \033[97m{time3}\033[m ficou em segundo\n')
        print(f'O \033[37m{time1}\033[m ficou em terceiro\n')
elif pont1 < pont3 > pont2:
    print(f'O \033[36m{time3}\033[m ficou em primeiro\n')
    if pont2 > pont1:
        print(f'O \033[35m{time2}\033[m ficou em segundo\n')
        print(f'O \033[34m{time1}\033[m ficou em terceiro\n')
    else:
        print(f'O \033[33m{time1}\033[m ficou em segundo\n')
        print(f'O \033[32m{time2}\033[m ficou em terceiro\n')

print("--------------------------------------------------------------------------------------------------------------")
