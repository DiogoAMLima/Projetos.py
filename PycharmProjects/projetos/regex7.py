import re

# palavra = '''
# Socos 2022
# '''
#
# p = re.compile(r'[a-zA-Z] [0-9]')  # Padrão agora é de letra, espaço, número
# ocorrencias = p.finditer(palavra)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)
# Resposta: span=(5, 8), match='s 2'  # Letra s, o espaço e número 2 (nos índices de 5 a 7, pois, o 8 último não conta)

barra_n = '\n'
palavra = str(input('Informe uma palavra: '))
vazio = ' '
num = str(input('Informe um número: '))

juncao = barra_n + palavra + vazio + num

p = re.compile(r'[a-zA-Z] [0-9]')  # Padrão agora é de letra, espaço, número
ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
