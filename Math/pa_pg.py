print('\033[32m—\033[m' * 18, '\033[33mPA\033[m', '\033[32m—\033[m' * 18)  # Progressão aritmética
prim = int(input('\nInforme o primeiro termo da PA: '))
raz = int(input('\nInforme a razão: '))
setimo_termo = prim + (7 - 1) * raz  # Sétimo termo da pa (Fórmula termo geral: an = a1 + (n - 1) * r)
for i in range(prim, setimo_termo + raz, raz):
    # Looping: (primeiro termo até o sétimo termo mais a razão com passo de acordo com o número digitado da razão)
    print(f'\n\033[32m{i}\033[m')

print()
print('\033[33m—\033[m' * 18, '\033[31mPG\033[m', '\033[33m—\033[m' * 18, '\n')

print('\033[31m—\033[m' * 18, '\033[35mFÓRMULA DO TERMO GERAL\033[m', '\033[31m—\033[m' * 18)

prim_seq = int(input("\nInforme o primeiro termo da PG: "))  # Progressão geométrica
razao = int(input("\nInforme a razão: "))
vigesimo_termo = prim_seq * (razao ** (20 - 1))  # Vigésimo termo da pg:
# (Fórmula termo geral: an = a1 * q elevado a n - 1)
for i in range(prim_seq, vigesimo_termo + razao, razao):
    # Looping: (primeiro termo até o vigésimo termo mais a razão com passo de acordo com o número digitado da razão)
    print(f'\n{i}')
print(f'\nO vigésimo termo da PG é: {vigesimo_termo}\n')

print('\033[35m—\033[m' * 18, '\033[36mSOMA DOS TERMOS\033[m', '\033[35m—\033[m' * 18)
primeiro_seq = int(input("\nInforme o primeiro termo da PG: "))
q = int(input("\nInforme a razão: "))
n = int(input("\nInforme a quantidade de elementos da PG: "))
S = (primeiro_seq * ((q ** n) - 1)) / (q - 1)  # Soma dos termos fórmula: Sn = a1 * (q elevado a n - 1) / q - 1
print(f'\nSoma dos {n} primeiros elementos é igual a: \033[97m{S}\033[m\n')

print('\033[34m—\033[m' * 55)
