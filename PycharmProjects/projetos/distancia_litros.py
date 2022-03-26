print('-----------------------------CARRO ECONÔMICO-----------------------------\n')

ds = int(input("Informe a distância em Km: "))
print('\n')
l_gasolina = float(input("Informe a quantidade de litros de gasolina consumidos: "))
kmL = ds / l_gasolina
print(f'Carro faz {kmL} kilometros por litro(s)')

if kmL < 8:
    print("Venda o carro!")
if 8 <= kmL <= 14:
    print("Econômico!")
if kmL > 15:
    print("Super Econômico!")
print('\n')
print('---------------------------------------------------------------------------')
