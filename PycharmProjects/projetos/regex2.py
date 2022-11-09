import re

# ^ - Irá testar o início da string
# [^] -Irá considerar todos os caracteres EXCETO o indicado
# texto = 'matam'
# p1 = re.compile('^m')  # Se a string começar com m, retorna o valor dela
# p2 = re.compile('[^m]')  # Todos os valores exceto o m
# check1 = p1.findall(texto)
# check2 = p2.findall(texto)
# print(check1)
# print(check2)

palavra = str(input('Informe uma palavra: '))
p1 = re.compile(f'^{palavra[0]}')
p2 = re.compile(f'[^{palavra[0]}]')
check1 = p1.findall(palavra)
check2 = p2.findall(palavra)
print(check1)
print(check2)
