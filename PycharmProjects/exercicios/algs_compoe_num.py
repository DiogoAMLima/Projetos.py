while True:
    num = (int(input("Informe um número entre 100 e 999: ")))
    if 100 > num <= 999:
        break
    aux = str(num)
    for cont, n in enumerate(aux):
        print(n)
