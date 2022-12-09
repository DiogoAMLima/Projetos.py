def raiz_qdr_cub():
    num = float(input('Informe um número para sabermos a raiz quadrada e cúbica: '))
    print(f'O {num} tem como raiz quadrada e cúbica respectivamente: \033[31m{num**(1/2)}\033[m e '
          f'\033[34m{num**(1/3):.2f}\033[m')


raiz_qdr_cub()
