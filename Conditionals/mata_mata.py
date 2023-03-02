from random import randint
from time import sleep
time = str(input('Informe o nome do seu time: '))
print('\033[31mTIMES CLASSIFICADOS\033[m: '
      '\033[33mBoca Juniors'
      '        Santos'
      '        Fluminense'
      '        Internaiconal'
      '        Bahia'
      '        Palmeiras'
      '        River Plate\033[m')
confronto = randint(1, 7)
if confronto == 1:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print(f'{time} x Boca Juniors')
    print()
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x Palmeiras')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Santos\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mSANTOS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Bahia')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Palmeiras\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mPALMEIRAS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x Intenracional')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x River Plate\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mRIVER PLATE É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')
elif confronto == 2:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print(f'{time} x Santos')
    print()
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x Fluminense')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Internacional\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mINTERNACIONAL É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Boca Juniors')
            sleep(0.5)
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Bahia\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mBAHIA É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x River Plate')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Fluminense\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mFLUMINENSE É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')
elif confronto == 3:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print(f'{time} x Fluminense')
    print()
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x Palmeiras')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Boca Juniors\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mBOCA JUNIORS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Internacional')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Palmeiras\033[34m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mPALMEIRAS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x River Plate')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Internacional\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mINTERNACIONAL É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')
elif confronto == 4:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print(f'{time} x Internacional')
    print()
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x Santos')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Bahia\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mBAHIA É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Fluminense')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Santos\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mSANTOS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x Bahia')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Fluminense\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mFLUMINENSE É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')
elif confronto == 5:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    print(f'{time} x Bahia')
    print()
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x River Plate')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Boca Juniors\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mBOCA JUNIORS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Boca Juniors')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x River Plate\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mRIVER PLATE É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x Santos')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Palmeiras\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mPALMEIRAS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')
elif confronto == 6:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print(f'{time} x Palmeiras')
    print()
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x Fluminense')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Santos\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mSANTOS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Bahia')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Internacional\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mINTERNACIONAL É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x Boca Juniors')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x River Plate\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mRIVER PLATE É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')
elif confronto == 7:
    print('\033[37mSorteando confronto das quartas...\033[m')
    sleep(0.5)
    print(f'{time} x River Plate')
    print()
    print('EQUIPES ENFRENTANDO-SE...')
    sleep(0.5)
    aleatorio_2 = randint(1, 2)
    if aleatorio_2 == 1:
        print('Seu time avançou, \033[31mPARABÉNS\033[m')
        print()
        print('Sorteando confronto da semi final...')
        sleep(0.5)
        aleatorio_3 = randint(1, 3)
        if aleatorio_3 == 1:
            print(f'{time} x Boca Juniors')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Fluminense\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mFLUMINENSE É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 2:
            print(f'{time} x Santos')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Bahia\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mBAHIA É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
        elif aleatorio_3 == 3:
            print(f'{time} x Palmeiras')
            print()
            print('EQUIPES ENFRENTANDO-SE...')
            sleep(0.5)
            aleatorio_4 = randint(1, 2)
            if aleatorio_4 == 1:
                print(f'O {time} venceu e está na \033[35mFINAL\033[m')
                print()
                print(f'A final será entre \033[34m{time} x Santos\033[m')
                print()
                print('EQUIPES ENFRENTANDO-SE...')
                sleep(0.5)
                aleatorio_5 = randint(1, 2)
                if aleatorio_5 == 1:
                    print(f'\033[34m{time}\033[m foi campeão')
                elif aleatorio_5 == 2:
                    print('Foi por muito pouco, O \033[36mSANTOS É O CAMPEÃO\033[m')
            elif aleatorio_4 == 2:
                print('Mais sorte na próxima...')
    elif aleatorio_2 == 2:
        print('Seu time foi eliminado, \033[31mTENTE NA PRÓXIMA\033[m')

# Escolhendo um time e colocando ele para disputar com outros com o objetivo de ser campeão.
# Laços de repetição aninhados para fazermos as comparações entre os times para os confrontos.
