from docx2python import docx2python

arquivo = str(input('Informe o nome do arquivo: '))

word = docx2python(f'{arquivo}')

# print(word)  # Retorno de alguns atributos em um dicionário

print(word.body)  # Nomes na mesma linha

print(word.text)  # Nomes em linhas separadas

print(word.properties)  # Informações do documento
