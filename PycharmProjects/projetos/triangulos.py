print('--------------------------TRIÂNGULO--------------------------\n')

A = int(input("Informe o primeiro valor para um lado do triângulo: "))
B = int(input("Informe o segundo valor para outro lado do triângulo: "))
C = int(input("Informe o terceiro valor para o último lado do triângulo: "))

print('\n')

if (B - C) < A < (B + C):
    if (A - C) < B < (A + C):
        if (A - B) < C < (A + B):
            print("É um triângulo")
            print('\n')
else:
    print("Não é um triângulo")
    print('\n')

if A == B and A == C and B == C:
    print("Triângulo equilátero")
    print('\n')
elif A == B or A == C or B == C:
    print("Triângulo isósceles")
    print('\n')
elif A != B and A != C and B != C:
    print("Triângulo escaleno")
    print('\n')
else:
    print("Apenas um triângulo comum")

print('-------------------------------------------------------------')
