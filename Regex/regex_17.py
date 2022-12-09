import re

# RG:

rg = str(input('Informe um RG: '))

p = re.compile(r'\d{2}\.\d{3}\.\d{3}-{1}\d{1}')
ocorrencias = p.finditer(rg)
for ocorrencia in ocorrencias:
    print(ocorrencia)
