import re
# Regular Expressions (Regex) - Python
# Documentação : https://docs.python.org/3/howto/regex.html

# Caracteres:

# . - Entende qualquer valor exceto uma nova linha
# \. - Para buscar o caracter "."

# texto = 'matam'
# padrao = re.compile('ma.am')  # Compile -> permite compilar o padrão
# # Explicando o padrão acima -> procurar o padrão am . (o ponto pode ser qualquer valor como explicado antes), m .
# # (ponto novamente) e a
# check = padrao.findall(texto)  # Variável para pegar o padrão criado e procurar todos no texto
# print(check)  # Retorna uma lista vazia se não encontrar

texto2 = str(input('Informe uma palavra: '))
pd1 = str(input('Informe o primeiro padrão: '))
pd2 = str(input('Informe o segundo padrão: '))
padrao = re.compile(f'{pd1}.{pd2}')
check = padrao.findall(texto2)
print(check)
