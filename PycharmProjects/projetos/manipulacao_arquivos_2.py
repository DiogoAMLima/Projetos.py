# Utilizar para Acentos e Caractéres especiais o encoding="utf-8"

# Utilizar o r -> (read) para arquivos mais simples:

with open("arquivo.txt", "w") as arquivo:  # Criando o arquivo
    arquivo.write("Rio de Janeiro")
# print(arquivo)


with open("arquivo.txt", "r", encoding="utf-8") as arquivo:  # Lendo e printando no terminal
    file = arquivo.read()
print(file)

# # Utilizar o a -> (append) para adicionar algo no arquivo:

with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\nSão Paulo")

# Podemos utilizar o readlines() para arquivos maiores

with open("arquivo2.txt", "r", encoding="utf-8") as arquivo:  # Arquivo criado anteriormente
    arquivo = arquivo.readlines()
print(arquivo)
