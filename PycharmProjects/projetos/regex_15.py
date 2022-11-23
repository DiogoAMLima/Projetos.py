import re

# Sites:
# sites = '''
# Sites diversos:
# https://google.com/
# https://www.youtube.com/
# https://www.linkedin.com/
# https://github.com/
# '''
#
# p = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com.br|com)')
# ocorrencias = p.finditer(sites)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)
#     # print(ocorrencia.group(0))
#     # print(ocorrencia.group(1))
#     # print(ocorrencia.group(2))
#     # print(ocorrencia.group(3))

barra_n = '\n'
site = str(input('Informe um site: '))
barra_n2 = '\n'
site2 = str(input('Informe um site: '))
barra_n3 = '\n'
site3 = str(input('Informe um site: '))
barra_n4 = '\n'
site4 = str(input('Informe um site: '))
barra_n5 = '\n'

juncao = barra_n + site + barra_n2 + site2 + barra_n3 + site3 + barra_n4 + site4 + barra_n5

p = re.compile(r'https?://(www\.)?([a-zA-Z0-9]+\.)+(com.br|com)')
ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
    # print(ocorrencia.group(0))
    # print(ocorrencia.group(1))
    # print(ocorrencia.group(2))
    # print(ocorrencia.group(3))
