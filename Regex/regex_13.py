import re

# {3,4} - de 3 a 4 min e max

# palavra = '''
# Mamam
# '''
#
# p = re.compile(r'[am]{2,4}')
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)

vazio = ' '
palavra = str(input('Informe uma palavra: '))
vazio2 = ' '

juncao = vazio + palavra + vazio2

p = re.compile(r'[am]{3,4}')  # Troque o am se for digitar uma palavra diferente de Mamam
ocorrencias = p.finditer(palavra)
for ocorrencia in ocorrencias:
    print(ocorrencia)
