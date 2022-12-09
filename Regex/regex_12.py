import re

# {2} - Número exato de repetições

# palavra = '''
# Mamam
# '''
#
# p = re.compile(r'[am]{2}')
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)

vazio = ' '
palavra = str(input('Informe uma palavra: '))
vazio2 = ' '

juncao = vazio + palavra + vazio2

p = re.compile(r'[am]{2}')  # Troque o am se for digitar uma palavra diferente de Mamam
ocorrencias = p.finditer(palavra)
for ocorrencia in ocorrencias:
    print(ocorrencia)
