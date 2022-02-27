cont = 1
l = []
soma = 0
while cont < 51:
    if cont % 2 == 0:
        l.append(cont)
        soma = soma + cont
    cont = cont + 1
print(f'A soma dos 50 primeiros pares é: {soma}')
