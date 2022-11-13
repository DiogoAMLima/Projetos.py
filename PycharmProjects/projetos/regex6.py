import re

# []Character set
# texto = '''
# Reviver 2000 rir
# '''
#
# p = re.compile(r'[a-zA-Z0-9]')  # De a até z minúsculas e vai considerar como possíveis neste padrão, A-Z:
# # De A até Z maiúsculas
# # 0-9: De 0 até 9
# ocorrencias = p.finditer(texto)  # Virá um objeto iterador para trazer todas as ocorrências do padrão texto
# for ocorrencia in ocorrencias:
#     print(ocorrencia)


palavra = str(input('Informe uma palavra: '))
vazio = ' '
num = str(input('Informe um número: '))
palavra2 = str(input('Informe outra palavra: '))
vazio2 = ' '

juncao = palavra + vazio + num + vazio2 + palavra2

p = re.compile(r'[a-zA-Z0-9]')  # Podemos substituir o 0-9 por \d
ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
