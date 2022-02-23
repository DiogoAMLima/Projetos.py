cont = 1
soma = 0
while cont != 11:
    num = int(input("Informe um valor: "))
    if num < 0:
        print("Número inválido. Apenas números positivos...")
        soma = soma - num
    soma = soma + num
    cont += 1
print(f'A soma dos números é: {soma}')
media = soma / 10
print(f'A média dos números é: {media}')
