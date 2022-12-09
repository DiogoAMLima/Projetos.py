# Mostrando vogais acentuadas ou não em palavras:

lista_palavras = ['Álbum', 'Crachá', 'Piauí', 'Grajaú', 'Sótão', 'Jacarés', 'Tórax', 'Célebre']

opcoes = str(input('Sem ideias para testar? Deseja ver uma lista de sugestões de palavras? [S/N]? ')).strip().upper()
if opcoes in 'S':
    print(f'\033[97m{lista_palavras}\033[m')
else:
    print('\n\033[33mTudo bem!\033[m')

palavra_1 = str(input('\nInforme uma palavra: '))
palavra_2 = str(input('Informe outra palavra: '))
palavra_3 = str(input('Informe mais uma palavra: '))

palavras = (f'{palavra_1}', f'{palavra_2}', f'{palavra_3}')

for palavra in palavras:
    print(f'\nNa palavra \033[31m{palavra.upper()}\033[m temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aáãâeéêiíoóuú':
            print(f'\033[36m{letra}\033[m', end=' ')
