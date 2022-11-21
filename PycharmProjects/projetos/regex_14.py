import re

# ()Grupos
# palavra = '''
# Mamam 2022
# mamam 2022
# '''
#
# p = re.compile(r'(M|m)?[a-z]{4} [0-9]+')  # Troque o am se for digitar uma palavra diferente de Mamam
# # A\a -> A maiúsculo ou a minúsculo
# # [a-z]{4} -> Caracter qualquer minúsculo que vai acontecer 4 vezes
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)
#     print(ocorrencia.group(0))  # Grupo da posição 0
#     print(ocorrencia.group(1))  # Grupo da posição 1

barra_n = '\n'
palavra = str(input('Informe uma palavra: '))
vazio = ' '
numero = str(input('Informe um número: '))
barra_n2 = '\n'
palavra2 = str(input('Informe a mesma palavra com letra minúscula: ')).lower()
vazio2 = ' '
numero2 = str(input('Informe outro número: '))
barra_n3 = '\n'

juncao = barra_n + palavra + vazio + numero + barra_n2 + palavra2 + vazio2 + numero2 + barra_n3

p = re.compile(r'(M|m)?[a-z]{4} [0-9]+')  # Troque o am se for digitar uma palavra diferente de Mamam
ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
    print(ocorrencia.group(0))
    print(ocorrencia.group(1))
