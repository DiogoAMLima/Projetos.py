print('--------------------PA--------------------\n')
prim = int(input('Informe o primeiro termo da PA: '))
raz = int(input('Informe a razão: '))
setimo_termo = prim + (7 - 1) * raz
for i in range(prim, setimo_termo + raz, raz):
    print(f'{i}\n')

print('-------------------PG---------------------\n')

print("-------------FÓRMULA DO TERMO GERAL------------\n")

prim_seq = int(input("Informe o primeiro termo da PG: "))
razao = int(input("Informe a razão: "))
vigesimo_termo = prim_seq * (razao ** (20 - 1))
for i in range(prim_seq, vigesimo_termo + razao, razao):
    print(f'{i}')
print(f'O vigésimo termo da PG é: {vigesimo_termo}')

print('\n')

print("-------------SOMA DOS TERMOS-------------\n")
primeiro_seq = int(input("Informe o primeiro termo da PG: "))
q = int(input("Informe a razão: "))
n = int(input("Informe a quantidade de elementos da PG: "))
S = (primeiro_seq * ((q ** n) - 1)) / (q - 1)
print(f'Soma dos {n} primeiros elementos é igual a: {S}')

print('\n')

print('------------------------------------------------')
