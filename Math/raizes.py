import math

a: float = float(input("Informe um valor para a: "))
b: float = float(input("Informe um valor para b: "))
c: float = float(input("Informe um valor para c: "))

delta = b**2 - 4 * a * c

print(f"O valor de delta é {delta}")

x1 = 0
x2 = 0

# Forma 1
if a == 0:
    print("O valor de a tem que ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    y = math.sqrt(delta)
    x1 = (-b + y) / (2 * a)
    x2 = (-b - y) / (2 * a)

print('O valor de x1 é {:.2f}'.format(x1))
print('O valor de x2 é {:.2f}'.format(x2))

# Forma 2
# if a == 0:
#    print("O valor de a tem que ser diferente de 0")
# elif delta < 0:
#    print("Sem raízes reais")
# else:
# x1 = (-b + delta ** (1 / 2)) / (2 * a)  # Elevar um número a 1/2 é o mesmo que tirar sua raiz quadrada...
# x2 = (-b - delta ** (1 / 2)) / (2 * a)

# print("x1: {}, x2: {}".format(x1, x2))

if delta > 0:
    print("Delta tem duas raízes reais")
elif delta == 0:
    print("Delta tem uma única raiz real")
else:
    print("Delta não tem raiz")
