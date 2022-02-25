# Ordem Crescente positiva e impar
# n = int(input("Informe um valor: "))
# if n < 0:
#     print("Valor inválido. Somente números positivos...")
# cres = (n - n) + 1
# while cres < n:
#     if cres % 2 == 1:
#         cres += 2
#     else:
#         cres -= 1
#     print(cres - 2)

# Ordem Decrescente positiva e impar
n = int(input("Informe um valor: "))
if n < 0:
    print("Valor inválido. Somente números positivos...")
decres = n + 1
while 0 < decres:
    if decres % 2 == 1:
        decres -= 2
    else:
        decres -= 1
    if decres >= 1:
        print(decres)
