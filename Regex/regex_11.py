import re

# ? - 0 ou um -> Mostrará a sequência ra (e as vezes que não apareceram = vazios)
# -> Olhar as respostas de todos os exemplos de Quantificadores (regex 9) para entender a diferença exata.
# palavra = '''
# Mamam
# '''
#
# p = re.compile(r'[am]?')
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)

vazio = ' '
palavra = str(input('Informe uma palavra: '))
vazio2 = ' '

juncao = vazio + palavra + vazio2

p = re.compile(r'[am]?')  # Troque o am se for digitar uma palavra diferente de Mamam
ocorrencias = p.finditer(palavra)
for ocorrencia in ocorrencias:
    print(ocorrencia)
