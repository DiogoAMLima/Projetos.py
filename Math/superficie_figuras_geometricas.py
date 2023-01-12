print('\033[30;41mSURFACE CYLINDER\033[m')

pi_cy = 3.14

r_cy = float(input('\nInforme o raio do cilindro: '))

h_cy = float(input('\nInforme a altura do cilindro: '))

sf_cy = 2 * pi_cy * r_cy * (h_cy + r_cy)

print(f'\nA superfície da área do cilindro é: \033[31m{sf_cy:.2f}\033[m')

print('\n\033[30;42mSURFACE CONE\033[m')

pi_cn = 3.14

r_cn = float(input('\nInforme o raio do cone: '))

l_cn = float(input('\nInforme o comprimento do cone: '))

sf_cn = pi_cn * r_cn * (l_cn + r_cn)

print(f'\nA superfície da área do cone é: \033[32m{sf_cn:.2f}\033[m')

print('\n\033[30;43mSURFACE SPHERE\033[m')

pi_sp = 3.14

r_sp = float(input('\nInforme o raio da esfera: '))

sf_sp = 4 * pi_sp * r_sp * r_sp

print(f'\nA superfície da área do esfera é: \033[33m{sf_sp:.2f}\033[m')

print('\n\033[30;44mSURFACE CUBE\033[m')

l_cb = float(input('\nInforme o lado do cubo: '))

sf_cb = 6 * l_cb * l_cb

print(f'\nA superfície da área do cubo é: \033[34m{sf_cb:.2f}\033[m')

print('\n\033[30;45mSURFACE CUBOID\033[m')

l_cbd = float(input('\nInforme o comprimento do cuboide: '))

h_cbd = float(input('\nInforme a altura do cuboide: '))

b_cbd = float(input('\nInforme a largura do cuboide: '))

sf_cbd = 2 * (l_cbd * b_cbd + b_cbd * h_cbd + l_cbd * h_cbd)

print(f'\nA superfície da área do cubóide é: \033[35m{sf_cbd:.2f}\033[m')

print('\n\033[30;46mCURVED SURFACE CYLINDER\033[m')

pi_cc = 3.14

r_cc = float(input('\nInforme o raio do cilindro circular: '))

h_cc = float(input('\nInforme a altura do cilindro circular: '))

sf_cc = 2 * pi_cc * r_cc * h_cc

print(f'\nA superfície da área do cilindro circular é: \033[36m{sf_cc:.2f}\033[m')

print('\n\033[30;47mCURVED SURFACE CONE\033[m')

pi_cnc = 3.14

r_cnc = float(input('\nInforme o raio do cone circular: '))

l_cnc = float(input('\nInforme o comprimento do cone circular: '))

sf_cnc = pi_cnc * r_cnc * l_cnc

print(f'\nA superfície da área do cone circular é: \033[37m{sf_cnc:.2f}\033[m')
