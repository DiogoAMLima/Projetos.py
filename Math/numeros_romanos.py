print('———————————————————————————NÚEMROS ROMANOS———————————————————————————\n')
print('Lista de números: 1, 5, 10, 20, 50, 100, 500, 1000\n')
num_rom = [1, 5, 10, 20, 50, 100, 500, 1000]
while True:
    num = int(input('Informe um número que esteja na lista mostrada acima: '))
    if num in num_rom:
        if num == 1:
            print(f'O {num} em números romanos é: I\n')
        elif num == 5:
            print(f'O {num} em números romanos é: V\n')
        elif num == 10:
            print(f'O {num} em números romanos é: X\n')
        elif num == 20:
            print(f'O {num} em números romanos é: XX\n')
        elif num == 50:
            print(f'O {num} em números romanos é: L\n')
        elif num == 100:
            print(f'O {num} em números romanos é: C\n')
        elif num == 500:
            print(f'O {num} em números romanos é: D\n')
        elif num == 1000:
            print(f'O {num} em números romanos é: M\n')
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
            if resp in 'SN':
                break
            print('Responda apenas S ou N.')
        if resp == 'N':
            print('ATÉ A PRÓXIMA')
            break
    else:
        print('Erro, digite um número que esteja nesta lista: 1, 5, 10, 20, 50, 100, 500, 1000\n')
