b = float(input("Informe a base do triângulo: "))
h = float(input("Informe a altura triângulo: "))
try:
    if b <= 0 or h <= 0:
        print("Não pode haver valores para base ou altura menores ou iguais a 0...")
except ZeroDivisionError:
    print("Não pode haver divisão por 0...")
area = (b * h) / 2
print(f'A área do triângulo é: ' "{:.2f}".format(area))
