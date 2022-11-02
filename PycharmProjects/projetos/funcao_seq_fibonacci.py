def seq_fibonacci():
    num = int(input("Informe o número de termos da sequência que devem aparecer: "))
    ant = 0  # Primeiro termo da sequência
    suce = 1  # Segundo termo da sequência
    if num < 0:
        print("\n\033[31mNúmero inválido...\033[m")
    else:
        print(f'\n\033[33m{ant} \n{suce}\033[m')
        cont = 3  # Terceiro termo da sequência
        while cont <= num:  # Looping até o contador igualar-se ao número digitado
            seq = suce + ant
            print(f'\033[33m{seq}\033[m')
            ant = suce
            suce = seq
            cont += 1
    print('\n\033[36mTerminou...\033[m')


seq_fibonacci()
