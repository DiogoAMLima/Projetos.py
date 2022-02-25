# Ordem Crescente positiva e par
n = int(input("Informe um valor: "))
if n < 0:
    print("Valor inválido. Somente números positivos...")
cres = n - n
print(cres)
while cres < n:
    if cres % 2 == 0:
        cres += 2
    else:
        cres -= 1
    print(cres)

# Ordem Decrescente positiva e par
# n = int(input("Informe um valor: "))
# if n < 0:
#     print("Valor inválido. Somente números positivos...")
# decres = n + 1
# while 0 < decres:
#     if decres % 2 == 0:
#         decres -= 2
#     else:
#         decres -= 1
#     print(decres)
