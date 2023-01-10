print('\033[30;41mCIRCLE\033[m')

r = float(input('\nInforme o raio do círculo: '))

area_c = 3.14 * r * r

print(f'\nA área do círculo é: \033[31m{area_c:.2f}\033[m')

print('\n\033[30;42mSQUARE\033[m')

l = float(input('\nInforme o lado do quadrado: '))

area_q = l * l

print(f'\nA área do quadrado é: \033[32m{area_q:.2f}\033[m')

print('\n\033[30;43mRECTANGLE\033[m')

base = float(input('\nInforme o valor da base: '))
h = float(input('\nInforme o valor da altura: '))

area_r = base * h

print(f'\nA área do retângulo é: \033[33m{area_r:.2f}\033[m')

print('\n\033[30;44mPERIMETER OF RECTANGLE\033[m')

base = float(input('\nInforme o valor da base: '))
h = float(input('\nInforme o valor da altura: '))

pr_rct = (2 * base) + (2 * h)

print(f'\nO perímetro do retângulo é: \033[34m{pr_rct:.2f}\033[m')

print('\n\033[30;45mPARALLELOGRAM\033[m')

base = float(input('\nInforme o valor da base: '))
h = float(input('\nInforme o valor da altura: '))

area_prl = base * h

print(f'\nA área do paralelogramo é: \033[35m{area_prl:.2f}\033[m')

print('\n\033[30;46mRHOMBUS\033[m')

D = float(input('\nInforme a primeira diagonal: '))
d = float(input('\nInforme a primeira diagonal: '))

area_rh = (D * d) / 2

print(f'\nA área do losango é: \033[36m{area_rh:.2f}\033[m')

print('\n\033[30;47mPERIMETER OF RHOMBUS\033[m')

L = float(input('\nInforme o lado do losango: '))

pr_rh = L * 4

print(f'\nA área do losango é: \033[37m{pr_rh:.2f}\033[m')

print('\n\033[30;107mRIGHT TRIANGLE\033[m')

base = float(input('\nInforme o valor da base: '))
h = float(input('\nInforme o valor da altura: '))

area_tr = (base * h) / 2

print(f'\nA área do triângulo é: \033[97m{area_tr:.2f}\033[m')

print('\n\033[30;41mSCALENE TRIANGLE\033[m')
print('\n\033[30;41mFÓRMULA DE HERON\033[m')

a = float(input('\nInforme o primeiro lado: '))
b = float(input('\nInforme o segundo lado: '))
c = float(input('\nInforme o terceiro lado: '))

semi_per = (a + b + c) / 2

area_st = (semi_per * (semi_per - a) * (semi_per - b) * (semi_per - c)) ** 0.5

print(f'\nO semi perímetro é: \033[31m{semi_per:.2f}\033[m e a área do triângulo escaleno com a fórmula de heron é: '
      f'\033[31m{area_st:.2f}\033[m')

print('\n\033[30;42mEQUILATERAL TRIANGLE\033[m')

print('\n\033[30;42mRAIZ DE 3 = A 1.7\033[m')

lado = float(input('\nInforme o valor do lado: '))

area_et = (lado * lado) * 1.7 / 4

print(f'\nA área do triângulo equilátero é: \033[32m{area_et:.2f}\033[m')

print('\n\033[30;43mPERIMETER OF SQUARE\033[m')

lado_q = float(input('\nInforme o lado do quadrado: '))

pr_qua = lado_q * 4

print(f'\nO perímetro do quadrado é: \033[33m{pr_qua:.2f}\033[m')

print('\n\033[30;44mPERIMETER OF TRIANGLE\033[m')

a_pr = float(input('\nInforme o primeiro lado: '))
b_pr = float(input('\nInforme o segundo lado: '))
c_pr = float(input('\nInforme o terceiro lado: '))

pr_tri = a_pr + b_pr + c_pr

print(f'\nO perímetro do triângulo é: \033[34m{pr_tri}\033[m')

print('\n\033[30;45mPERIMETER OF PARALLELOGRAM\033[m')

a_pr_prl = float(input('\nInforme o primeiro lado: '))
b_pr_prl = float(input('\nInforme o segundo lado: '))

pr_prl = (2 * a_pr_prl) + (2 * b_pr_prl)

print(f'\nO perímetro do paralelogramo é: \033[35m{pr_prl}\033[m')
