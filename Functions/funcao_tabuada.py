def tabuada():
    while True:
        num = int(input("\nDigite um número para mostrar a tabuada ou um número negativo para sair: "))
        print()
        if num < 0:  # Se for menor que zero o valor informado, nem mostrará a tabuada
            print('\033[31mAté a próxima...\033[m')
            break
        for cont in range(1, 11):  # Looping para termos os resultados de 1 a 10 (último valor não é incluído no for)
            print(f'\033[32m{num}\033[m \033[31mx\033[m \033[34m{cont}\033[m = \033[97m{num * cont}\033[m')
            # Multiplicando os valores


tabuada()
