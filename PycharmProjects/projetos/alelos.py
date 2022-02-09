print("Alelos podem ser dominantes ou recessivos.\n")
print("Alelo Dominante = Alelo que sozinho consegue expressar alguma característica.\n")
print("Alelo Recessivo = Alelo que só expressa-se uma característica aos pares.\n")
print("Para exemplos, podemos ter AA,Aa,aa\n")
print("Informe seus alelos: ")
alelo1: str = str(input())
if alelo1 == 'AA':
    print("Homozigoto")
if alelo1 == 'Aa':
    print("Heterozigoto")
if alelo1 == 'aa':
    print('Homozigoto')
else:
    print("Isto não é um alelo...")
print(f'Seus alelos são: {alelo1}')
print("Informe os alelos de outro indivíduo: ")
alelo2: str = str(input())
if alelo2 == 'AA':
    print("Homozigoto")
if alelo2 == 'Aa':
    print("Heterozigoto")
if alelo2 == 'aa':
    print('Homozigoto')
else:
    print("Isto não é um alelo...")
print(f'Os alelos deste indivíduo são: {alelo2}\n')
print("Exemplo para cor dos olhos a seguir...\n")
print("Alelo recessivo para olhos azuis: aa\n")
print("Vamos ver a probabilidade de você e o indivíduo com os alelos citados acima "
      "terem um filho(a) com olhos azuis (aa)... \n")
print("Caso os alelos do primeiro e segundo indíviduos sejam diferentes de AA ou Aa ou aa, não será possível ver a"
      " probabilidade... ")
try:
    if alelo1 == 'AA' and alelo2 == 'AA':
        print("Chance de terem um filho com olhos azuis = 0%")
    else:
        if alelo1 == 'aa' and alelo2 == 'aa':
            print("chance de terem um filho com olhos azuis = 100%")
        else:
            if alelo1 == 'AA' and alelo2 == 'aa':
                print("Chance de terem um filho com olhos azuis = 0%")
            else:
                if alelo1 == 'Aa' and alelo2 == 'aa':
                    print("Chance de terem um filho com olhos azuis = 50%")
                else:
                    if alelo1 == 'Aa' and 'Aa':
                        print("Chance de terem um filho com olhos azuis = 25%")
except ValueError:
    print("Isto não é um alelo...")
