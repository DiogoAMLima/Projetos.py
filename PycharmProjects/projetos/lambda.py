print('——————————————————————\033[36mLAMBDA-EXEMPLOS\033[m——————————————————————\n')

l = lambda x: (x ** 2) + (x ** 3)
l2 = lambda x: (x ** 3) - (x ** 2) - x
x = 3

print(f'O valor na \033[32mprimeira\033[m expressão é: \033[31m{l(x)}\033[m')
print(f'O valor na \033[31msegunda\033[m expressão é: \033[32m{l2(x)}\033[m')

for i in range(1, 5):
    print(f'\nO \033[37m{i}°\033[m valor para a \033[35mprimeira\033[m expressão é: \033[33m{l(i)}\033[m')
    print(f'\nO \033[37m{i}°\033[m valor para a \033[36msegunda\033[m expressão é: \033[34m{l2(i)}\033[m')


# Um valor para uma expressão (interação com o usuário):

z = float(input('\nInforme um valor para z: '))

desconto = lambda z: z - (z * 0.2)

print(f'\nO valor \033[33mR${z}\033[m com desconto é: \033[35mR${desconto(z):.2f}\033[m')
