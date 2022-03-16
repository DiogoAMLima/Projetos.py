print("--------------------------------------------------STRINGS--------------------------------------------------")
print("------------------------------------ALGUMAS FUNCIONALIDADES DE STRINGS-------------------------------------")

print('\n')

palavra = str(input("Digite uma palavra: ")).strip() # Acabar com os espaços antes e depois (Espaços entre palavras,
# prossegue existindo)
# Método len para saber o tamanho de uma string.
# utilizar count para eliminar os espaços restantes (entre as palavras)
print('A palavra tem ao todo {} letras'.format(len(palavra) - palavra.count(' ')))

# Verificar se a palavra digitada tem em alguma comparação...
#Nome
# print(palavra[:4] == 'João')
# Desse jeito podemos ter um erro, pois, o usuário pode digitar joão ou JOÃO e aí não será reconhecido.
# print(palavra[:4].lower() == 'joão') # ou, utilizar: print(palavra[:4].upper() == 'JOÃO')

#Time
# print(palavra[:8].upper() == 'FLAMENGO')

# Cidade
# print(palavra[:3].lower() == 'rio')

# Emprego
# print(palavra[:6].lower() == 'médico')

# Podemos separar uma sequencia de strings com o split()
string_separada = palavra.split()
print(f'Primeira palavra é: {string_separada[0]}')

print('\n')

# Descobrir quantas vezes aparece alguma letra em uma sequencia de strings...
palavra2 = str(input("Digite outra palavra: ")).lower()
print('Letra o repetiu {} vezes '.format(palavra2.count('o')))

print('\n')

palavra3 = str(input("Digite mais uma palavra: ")).upper()
print('Letra R repetiu {} vezes '.format(palavra3.count('R')))

print('\n')

print('-----------------------------------------------------------------------------------------------------------')
