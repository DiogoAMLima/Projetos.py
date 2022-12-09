import re

# palavra = '''
# Socos 2022
# Socos2022
# '''

# p = re.compile(r'[a-zA-Z]+ [0-9]+')  # O + faz com que o caracter que apareça pelo menos uma vez, permite que pegue
# todas as ocorrências

# Meu padrão: Letra minúscula e letra maiúscula, o símbolo +, espaço, número de 0 a 9, o símbolo +
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)

# Resposta: span=(1, 11), match='Socos 2022'
# O Socos2022 não será mostrado, pois, não tem o espaço no padrão que queremos: r'[a-zA-Z]+ [0-9]+'

barra_n = '\n'
palavra = str(input('Informe uma palavra: '))
vazio = ' '
num = str(input('Informe um número: '))
barra_n2 = '\n'
palavra2 = str(input('Informe outra palavra: '))
num2 = str(input('Informe outro número: '))

juncao = barra_n + palavra + vazio + num + barra_n2 + num2

p = re.compile(r'[a-zA-Z]+ [0-9]+')

ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
