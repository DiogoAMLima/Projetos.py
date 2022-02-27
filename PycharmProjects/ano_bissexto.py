anoB = int(input("Informe um ano: "))

if (anoB % 4 == 0 and anoB % 100 != 0) or anoB % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano comum")
