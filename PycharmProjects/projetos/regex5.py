import re

# \w - Qualquer caracter que SEJA alfanumérico
# \W - Qualquer caracter que NÃO SEJA Alfanumérico

# texto = '''
#
# _socos$ 2022_
#
# '''
#
# p1 = re.compile(r'\w')
# p2 = re.compile(r'\W')
# check1 = p1.findall(texto)
# check2 = p2.findall(texto)
# print(check1)
# print(check2)

vazio = '   '

palavra = str(input('Informe uma palavra: '))

vazio2 = '         '

linha = '\n'

juncao = vazio + palavra + vazio2 + linha

p1 = re.compile(r'\w')
p2 = re.compile(r'\W')
check1 = p1.findall(juncao)
check2 = p2.findall(juncao)
print(check1)
print(check2)
