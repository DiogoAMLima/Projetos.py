from random import randint

print("------------------------------------------PONTUAÇÃO E CLASSIFICAÇÃO------------------------------------------\n")

time1 = str(input("Informe o nome do primeiro time: ")).strip().upper()
time2 = str(input("Informe o nome do segundo time: ")).strip().upper()
time3 = str(input("Informe o nome do terceiro time: ")).strip().upper()

pont1 = 0
pont2 = 0
pont3 = 0

i = 0
while i <= 10:
    aleat = randint(0, 2)
    confr = int(input("Informe o confronto desejado: "
                      "[0 = time1 x time2 / 1 = time1 x time 3 / 2 = time2 x time3]: "))
    if confr == 0 and aleat == 0:
        print(f'O {time1} e o {time2} empataram\n')
        pont1 += 1
        pont2 += 1
    if confr == 0 and aleat == 1:
        print(f'O {time1} venceu o {time2}\n')
        pont1 += 3
    if confr == 0 and aleat == 2:
        print(f'O {time2} venceu o {time1}\n')
        pont2 += 3
    if confr == 1 and aleat == 0:
        print(f'O {time1} e o {time3} empataram\n')
        pont1 += 1
        pont3 += 1
    if confr == 1 and aleat == 1:
        print(f'O {time1} venceu o {time3}\n')
        pont1 += 3
    if confr == 1 and aleat == 2:
        print(f'O {time3} venceu o {time1}\n')
        pont3 += 3
    if confr == 2 and aleat == 0:
        print(f'O {time2} e o {time3} empataram\n')
        pont2 += 1
        pont3 += 1
    if confr == 2 and aleat == 1:
        print(f'O {time2} venceu o {time3}\n')
        pont2 += 3
    if confr == 2 and aleat == 2:
        print(f'O {time3} venceu o {time2}\n')
        pont3 += 3
    i += 1

print(f'\033[0;34mO {time1} terminou com {pont1} pontos\033[m\n')
print(f'\033[0;31mO {time2} terminou com {pont2} pontos\033[m\n')
print(f'\033[0;30mO {time3} terminou com {pont3} pontos\033[m\n')

if pont2 < pont1 > pont3:
    print(f'O {time1} ficou em primeiro\n')
    if pont2 > pont3:
        print(f'O {time2} ficou em segundo\n')
        print(f'O {time3} ficou em terceiro\n')
    else:
        print(f'O {time3} ficou em segundo\n')
        print(f'O {time2} ficou em terceiro\n')
elif pont1 < pont2 > pont3:
    print(f'O {time2} ficou em primeiro\n')
    if pont1 > pont3:
        print(f'O {time1} ficou em segundo\n')
        print(f'O {time3} ficou em terceiro\n')
    else:
        print(f'O {time3} ficou em segundo\n')
        print(f'O {time1} ficou em terceiro\n')
elif pont1 < pont3 > pont2:
    print(f'O {time3} ficou em primeiro\n')
    if pont2 > pont1:
        print(f'O {time2} ficou em segundo\n')
        print(f'O {time1} ficou em terceiro\n')
    else:
        print(f'O {time1} ficou em segundo\n')
        print(f'O {time2} ficou em terceiro\n')

print("--------------------------------------------------------------------------------------------------------------")
