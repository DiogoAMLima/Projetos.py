print("------------------CARDÁPIO------------------")
print("Código: 100 - Cachorro Quente - Valor: 1.20\n"
      "Código: 101 - Bauru Simples - Valor: 1.30\n"
      "Código: 102 - Bauru com Ovo - Valor: 1.50\n"
      "Código: 103 - Hamburguer - Valor: 1.20\n"
      "Código: 104 - Cheesenurguer - Valor: 1.70\n"
      "Código: 105 - Suco - Valor: 2.20\n"
      "Código: 106 - Refrigerante - Valor: 1.00\n")

cd = int(input("Informe o código do produto: "))
qnt = int(input("Informe a quantidade desejada: "))

if cd == 100:
    print("Cachorro quente escolhido")
    pagar = qnt * 1.20
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if cd == 101:
    print("Bauru Simples escolhido")
    pagar = qnt * 1.30
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if cd == 102:
    print("Bauru com Ovo escolhido")
    pagar = qnt * 1.50
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if cd == 103:
    print("Hamburguer escolhido")
    pagar = qnt * 1.20
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if cd == 104:
    print("Cheeseburguer escolhido")
    pagar = qnt * 1.70
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if cd == 105:
    print("Suco escolhido")
    pagar = qnt * 2.20
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if cd == 106:
    print("Refrigerante escolhido")
    pagar = qnt * 1.00
    print(f'Você terá que pagar: '"{:.2f}".format(pagar))
if 100 < cd >= 107:
    print("Código inválido...")
