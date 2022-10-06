def tabuada():
    while True:
        num = int(input("\nDigite um número para mostrar a tabuada ou um número negativo para sair: "))
        print()
        if num < 0:
            print('\033[31mAté a próxima...\033[m')
            break
        for cont in range(1, 11):
            print(f'\033[32m{num}\033[m x \033[34m{cont}\033[m = \033[97m{num * cont}\033[m')


tabuada()
