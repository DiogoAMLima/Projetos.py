cont = 1
soma = 0
l = []
while cont != 11:
    num = int(input("Informe um valor: "))
    l.append(num)
    soma = soma + num
    cont += 1
menor = min(l)
maior = max(l)

print(f'O menor valor lido é: \033[34m{menor}\033[m')
print(f'O maior valor lido é: \033[35m{maior}\033[m')
print(f'A soma dos números é: \033[36m{soma}\033[m')
