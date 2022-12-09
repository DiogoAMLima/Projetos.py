print("-------------------------------CONVERSOR DA MOEDA REAL PARA OUTRAS MOEDAS-------------------------------")
# Cotações dia 11/03/2022

# Cotação do dólar = 5,08
# Cotação do euro = 5,54
# Cotação da libra = 6,61

# Forma 1 (Mais simples e menos variáveis...)

valor = float(input("Informe um valor em reais: "))

print("Valor em reais {:.2f} convertido para dólar: {:.2f}, convertido para euro: {:.2f} e convertido para libra {:.2f}"
      .format(valor, valor*5.08, valor*5.54, valor*6.61))


# Forma 2 (Simples, porém, com muitas variáveis desnecessárias como visto na forma 1...)

# valor = float(input("Informe um valor em reais: "))
#
# dolar = 5.08
# euro = 5.54
# libra = 6.61
#
# conversao1 = valor * dolar
# conversao2 = valor * euro
# conversao3 = valor * libra
#
# print('Valor de reais em dólar: ' "{:.2f}".format(conversao1))
# print('Valor de reais em euro: ' "{:.2f}".format(conversao2))
# print('Valor de reais em libra: ' "{:.2f}".format(conversao3))

print("\n")

print("--------------------------------------------------------------------------------------------------------")
