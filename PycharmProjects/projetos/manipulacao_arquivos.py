# Manipulação de arquivos simples:

# Estrutura com o with:
with open("arquivo.txt", 'w') as arquivo:
    arquivo.write("Python")

# Para ler o arquivo no terminal:
with open("arquivo.txt", 'r') as arquivo:
    print(arquivo.read())
