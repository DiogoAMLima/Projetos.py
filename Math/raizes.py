import math

a = float(input("Informe um valor para a: "))
b = float(input("Informe um valor para b: "))
c = float(input("Informe um valor para c: "))

delta = b**2 - 4 * a * c  # Fórmula de delta na matemática

print(f"\nO valor de delta é \033[31m{delta}\033[m")

x1 = 0
x2 = 0

# Forma 1
if a == 0:
    print("\n\033[31mO valor de a tem que ser diferente de 0\033[m")
elif delta < 0:
    print("\n\033[31mSem raízes reais\033[m")
else:
    y = math.sqrt(delta)  # Raiz quadrada de delta
    x1 = (-b + y) / (2 * a)
    x2 = (-b - y) / (2 * a)

print(f'\nO valor de x1 é \033[35m{x1:.2f}\033[m')
print(f'\nO valor de x2 é \033[36m{x2:.2f}\033[m')

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
    print("\n\033[34mDelta tem duas raízes reais\033[m")
elif delta == 0:
    print("\n\033[33mDelta tem uma única raiz real\033[m")
else:
    print("\n\033[30mDelta não tem raiz\033[m")

# Código descobrindo o valor de delta e as raízes caso existam
# Fórmula do delta: Δ = b**2 – 4 * a * c
# Fórmula para descobrir as raízes: x = – b ± √Δ / 2 * a
