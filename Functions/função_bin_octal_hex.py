def bin_octal_hex():
    num = int(input("Informe um número inteiro: "))
    print(f'O número {num} em binário, octal e hexadecimal respectivamente são: \033[31m{format(bin(num)[2:])}\033[m, '
          f'\033[34m{format(oct(num)[2:])}\033[m e \033[35m{format(hex(num)[2:]).upper()}\033[m')


bin_octal_hex()
