import re

# \s - Qualquer caracter que SEJA vazio
# \S - Qualquer caracter que NÃO SEJA vazio

# texto = '''
#
# socos 2000
#
# '''
#
# p1 = re.compile(r'\s')  # Mostra as quebras de lina (\n) e o espaço vazio entre socos e 2000
# p2 = re.compile(r'\S')  # Mostra os caracteres não vazios
# check1 = p1.findall(texto)
# check2 = p2.findall(texto)
# print(check1)
# print(check2)

vazio = '   '

palavra = str(input('Informe uma palavra: '))

vazio2 = '         '

juncao = vazio + palavra + vazio2

p1 = re.compile(r'\s')
p2 = re.compile(r'\S')
check1 = p1.findall(juncao)
check2 = p2.findall(juncao)
print(check1)
print(check2)
