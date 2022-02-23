bMaior = float(input("Informe o valor da Base maior: "))
bMenor = float(input("Informe o valor da Base menor: "))
H = float(input("Informe a altura: "))
A = ((bMaior + bMenor) * H) / 2
if bMaior <= 0 or bMenor <= 0:
    print("Valor da Base maior e Base menor devem ser maiores que 0.")
else:
    print(f'A Área do trapézio é: {A}')
