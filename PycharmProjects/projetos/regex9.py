import re

# Quantificadores:
# * - 0 ou mais -> Nossa palavra = mamam, teremos a resposta da ocorrência am mais as vezes que não apareceram (vazios)
# palavra = '''
# Mamam
# '''
# p = re.compile(r'[am]*')
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)

barra_n = '\n'
palavra = str(input('Informe uma palavra: '))
barra_n2 = '\n'

juncao = barra_n + palavra + barra_n2

p = re.compile(r'[am]*')  # Troque o am se for digitar uma palavra diferente de Mamam

ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
