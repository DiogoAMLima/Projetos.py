print('\033[30;41mVOLUME OF CUBE\033[m')

l = float(input('\nInforme o lado do cubo: '))

vol_cb = l * l * l

print(f'\nO volume od cubo é: \033[31m{vol_cb:.2f}\033[m')

print('\n\033[30;42mVOLUME OF CONE\033[m')

pi_cn = 3.14

r = float(input('\nInforme o raio do cone: '))

h = float(input('\nInforme a altura do cone: '))

vol_cn = (pi_cn * r * r * h) / 3

print(f'\nO volume do cone é: \033[32m{vol_cn:.2f}\033[m')

print('\n\033[30;43mVOLUME OF CUBOID\033[m')

l_cuboid = float(input('\nInforme o comprimento do cuboide: '))

b_cuboid = float(input('\nInforme a largura do cuboide: '))

h_cuboid = float(input('\nInforme a altura do cuboide: '))

vol_cbd = l_cuboid * b_cuboid * h_cuboid

print(f'\nO volume do cubóide é: \033[33m{vol_cbd:.2f}\033[m')

print('\n\033[30;44mVOLUME OF CYLINDER\033[m')

pi_cy = 3.14

r_cy = float(input('\nInforme o raio do cilindro: '))

h_cy = float(input('\nInforme a altura do cilindro: '))

vol_cy = pi_cy * r_cy * r_cy * h_cy

print(f'\nO volume do cilindro é: \033[34m{vol_cy:.2f}\033[m')

print('\n\033[30;45mVOLUME OF SPHERE\033[m')

pi_sp = 3.14

r_sp = float(input('\nInforme o raio da esfera: '))

vol_sp = (4 * pi_sp * r_sp * r_sp * r_sp) / 3

print(f'\nO volume da esfera é: \033[35m{vol_sp:.2f}\033[m')

print('\n\033[30;46mVOLUME OF HEMI-SPHERE\033[m')

pi_hsp = 3.14

r_hsp = float(input('\nInforme o raio do semi-círculo: '))

vol_hsp = (2 * pi_hsp * r_hsp * r_hsp * r_hsp) / 3

print(f'\nO volume do semi-círculo é: \033[36m{vol_hsp:.2f}\033[m')