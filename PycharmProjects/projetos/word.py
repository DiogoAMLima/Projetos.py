import docx2txt

# word = docx2txt.process("python.docx")  # Mostrando no terminal o conteúdo do documento word...
#
# print(word)
#
# word2 = docx2txt.process("python.docx", r"C:\Users\Pichau\PycharmProjects\projetos")  # Capturando e salvando
# a(s) imagen(s) do documento word na pasta deste código

# Interação com o usuário:

arquivo = str(input(r'Informe o nome do arquivo: '))  # Se não estiver na mesma pasta, informe o caminho

word = docx2txt.process(f"{arquivo}")

# print(word)

caminho = str(input('Informe o caminho do arquivo: '))

word2 = docx2txt.process(f"{arquivo}", fr"{caminho}")
