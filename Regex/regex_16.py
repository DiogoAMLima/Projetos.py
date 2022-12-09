import re

# emails = '''
# Alguns e-mails:
# diogo123@gmail.com
# luffy.king@gmail.com.br
# joaoABC@gmail.com
# '''
#
# p = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+')
# ocorrencias = p.finditer(emails)
# for ocorrencia in ocorrencias:
#     print(ocorrencia)


barra_n = '\n'
email = str(input('Informe um e-mail: '))
barra_n2 = '\n'
email2 = str(input('Informe outro e-mail: '))
barra_n3 = '\n'
email3 = str(input('Informe mais um e-mail: '))
barra_n4 = '\n'

juncao = barra_n + email + barra_n2 + email2 + barra_n3 + email3 + barra_n4

p = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+')
ocorrencias = p.finditer(juncao)
for ocorrencia in ocorrencias:
    print(ocorrencia)
