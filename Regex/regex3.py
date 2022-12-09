import re

# \d - Qualquer caracter que SEJA um algarismo  de 0 a 9
# \D - Qualquer caracter que NÃO SEJA um algarismo de 0 a 9

# texto = 'matam1998'
# p1 = re.compile(r'\d')  # Usar o r de raw string antes
# p2 = re.compile(r'\D')
# check1 = p1.findall(texto)
# check2 = p2.findall(texto)
# print(check1)
# print(check2)

palavra = str(input('Informe uma palavra: '))
numero = str(input('Informe números (quantos quiser): '))
juncao = palavra + numero

p1 = re.compile(r'\d')
p2 = re.compile(r'\D')
check1 = p1.findall(juncao)
check2 = p2.findall(juncao)
print(check1)
print(check2)
