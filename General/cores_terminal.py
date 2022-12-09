# Estilo: 0 = normal, 1 = negrito, 4 = sublinhado e 7 = inverter (negativo)

# Texto: 30 = preto, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = roxo, 36 = azul piscina, 37 = cinza,
# 97 = branco

# Fundo: 40 = preto, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = roxo, 46 = azul piscina, 47 = cinza,
# branco = 107

print('-------------------------------------CORES TERMINAL-------------------------------------\n')

print('\033[0;31;47mVermelho!\033[m\n')

print('\033[1;33;44mAmarelo!\033[m\n')

print('\033[4;35;41mRoxo!\033[m\n')

print('\033[7;32;46mAzul piscina!\033[m\n')

print('\033[0;34;40mAzul!\033[m\n')

valor_1 = float(input("Informe um valor: "))
valor_2 = float(input("Informe outro valor: "))
res = valor_1 * valor_2
print('\n')
print(f'O resultado de \033[31m{valor_1}\033[m * \033[32m{valor_2}\033[m é: \033[34m{res}\033[m')
print('\n')

numero = float(input("Informe um número: "))
print('O {}{}{} está em Azul!'.format('\033[1;34m', numero, '\033[m'))

print('\n')

print('-----------------------------------------------------------------------------------------')
