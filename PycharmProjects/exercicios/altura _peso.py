H = float(input("Informe a altura de uma pessoa: "))
P = float(input("Informe o peso dessa pessoa: "))

if H < 1.20 and P <= 60:
    print("Classificação A")
if H < 1.20 and 60 < P <= 90:
    print("Classificação D")
if H < 1.20 and P > 90:
    print("Classificação G")
if 1.20 <= H <= 1.70 and P <= 60:
    print("Classificação B")
if 1.20 <= H <= 1.70 and 60 < P <= 90:
    print("Classificação E")
if 1.20 <= H <= 1.70 and P > 90:
    print("Classificação H")
if H > 1.70 and P <= 60:
    print("Classificação C")
if H > 1.70 and 60 < P <= 90:
    print("Classificação F")
if H > 1.70 and P > 90:
    print("Classificação I")
