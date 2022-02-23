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

print(f'O menor valor lido é: {menor}')
print(f'O maior valor lido é: {maior}')
print(f'A soma dos números é: {soma}')
