from math import factorial
print("-------------------------------COMBINAÇÃO E ARRANJO-------------------------------")

print("\n")

n = int(input("Informe a quantidade total de elementos em algum conjunto: "))
p = int(input("Informe a quantidade de elementos: "))

print("\n")

print("Lembrando que p não pode ser menor que n, pois, não podemos ter fatorial negativo. \n")

A = factorial(n) / factorial(n - p)

print("O resultado do arranjo simples é: {:.1f}".format(A))

print("\n")

n2 = int(input("Informe total de elementos de um conjunto: "))
p = int(input("Informe total de elementos de um subconjunto: "))

C = factorial(n2) / (factorial(p) * factorial(n2 - p))

print("O resultado da combinação simples é: {:.1f}".format(C))

print("\n")

print("----------------------------------------------------------------------------------")
