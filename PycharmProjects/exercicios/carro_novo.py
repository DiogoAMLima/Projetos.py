custo_fabrica = float(input("Informe o custo de fábrica: "))

if custo_fabrica <= 12000:
    custo_cnsd = custo_fabrica + ((custo_fabrica/100) * 5)
    print(f'O custo ao consumidor é: {custo_cnsd}')
if 12000 <= custo_fabrica <= 25000:
    custo_cnsd = custo_fabrica + ((custo_fabrica/100) * 10) + ((custo_fabrica/100) * 15)
    print(f'O custo ao consumidor é: {custo_cnsd}')
if custo_fabrica > 25000:
    custo_cnsd = custo_fabrica + ((custo_fabrica/100) * 15) + ((custo_fabrica/100) * 20)
    print(f'O custo ao consumidor é: {custo_cnsd}')
