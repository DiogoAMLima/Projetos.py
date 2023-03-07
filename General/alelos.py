print("Alelos podem ser dominantes ou recessivos.\n")
print("Alelo Dominante = Alelo que sozinho consegue expressar alguma característica.\n")
print("Alelo Recessivo = Alelo que só expressa-se uma característica aos pares.\n")
print("Para exemplos, podemos ter AA,Aa,aa\n")
alelo1 = str(input("Informe seus alelos: "))  # Informando o alelo 1
# Verificando se é homozigoto ou heterozigoto
if alelo1 == 'AA': 
    print("\n\033[32mHomozigoto\033[m")
elif alelo1 == 'Aa':
    print("\n\033[33mHeterozigoto\033[m")
elif alelo1 == 'aa':
    print('\n\033[34mHomozigoto\033[m')
else:
    print("\n\033[31mIsto não é um alelo...\033[m")
print(f'\n\033[35mSeus alelos são: {alelo1}\033[m')
alelo2 = str(input("\nInforme os alelos de outro indivíduo: "))  # Informando o alelo 2
# Verificando se é homozigoto ou heterozigoto
if alelo2 == 'AA':
    print("\n\033[32mHomozigoto\033[m")
elif alelo2 == 'Aa':
    print("\n\033[33mHeterozigoto\033[m")
elif alelo2 == 'aa':
    print('\n\033[34mHomozigoto\033[m')
else:
    print("\n\033[31mIsto não é um alelo...\033m")
print(f'\nOs alelos deste indivíduo são: {alelo2}\n')
print("Exemplo para cor dos olhos a seguir...\n")
print("Alelo recessivo para olhos azuis: aa\n")
print("Vamos ver a probabilidade de você e o indivíduo com os alelos citados acima "
      "terem um filho(a) com olhos azuis (aa)... \n")
print("Caso os alelos do primeiro e segundo indíviduos sejam diferentes de AA ou Aa ou aa, não será possível ver a"
      " probabilidade... ")
try:  # Tratamento de erros
    # Verificando a probabilidade:
    if alelo1 == 'AA' and alelo2 == 'AA':
        print("\n\033[31mChance de terem um filho com olhos azuis = 0%\033[m")
    elif alelo1 == 'aa' and alelo2 == 'aa':
        print("\n\033[32mchance de terem um filho com olhos azuis = 100%\033[m")
    elif alelo1 == 'AA' and alelo2 == 'aa':
        print("\n\033[33mChance de terem um filho com olhos azuis = 0%\033[m")
    elif alelo1 == 'Aa' and alelo2 == 'aa':
        print("\n\033[34mChance de terem um filho com olhos azuis = 50%\033[m")
    elif alelo1 == 'Aa' and 'Aa':
        print("\n\033[35mChance de terem um filho com olhos azuis = 25%\033[m")
    elif alelo1 == 'aa' and 'Aa':
        print("\n\033[36mChance de terem um filho com olhos azuis = 50%\033[m")
except ValueError:
    print("\n\033[31mIsto não é um alelo...\033[m")
