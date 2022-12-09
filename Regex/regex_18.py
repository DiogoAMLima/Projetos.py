import re
import random
import time

print('\033[33m——————————————RG ALEATÓRIO——————————————\033[m')

# RG aleatório:

num = "0123456789"
num2 = "0123456789"
num3 = "0123456789"

juncao = num + num2

juncao2 = num + num2 + num3

juncao3 = num + num2 + num3

while True:
    op = str(input('\nPara continuarmos o procedimento, pressione qualquer tecla ou s para sair... ')).strip()
    if op == 's':
        print('\n\033[33mFinalizando...\033[m')
        break
    else:
        try:
            tamanho_da_senha = 2
            senha = "".join(random.sample(juncao, tamanho_da_senha))
            tamanho_da_senha2 = 3
            senha2 = "".join(random.sample(juncao2, tamanho_da_senha2))
            senha3 = "".join(random.sample(juncao3, tamanho_da_senha2))
            tamanho_da_senha3 = 1
            senha4 = "".join(random.sample(num, tamanho_da_senha3))
            print('\n\033[31mEstamos gerando um RG, por favor aguarde...\033[m\n')
            time.sleep(4)
            senha_completa = senha + "." + senha2 + "." + senha3 + "-" + senha4
            print(f'\033[34mO RG gerado foi:\033[m \033[35m{senha_completa}\033[m')
            p = re.compile(r'\d{2}\.\d{3}\.\d{3}-{1}\d{1}')
            print(f'\n\033[34mVerificando o RG gerado:\033[m \033[35m{senha_completa}\033[m')
            time.sleep(2)
            ocorrencias = p.finditer(senha_completa)
            for ocorrencia in ocorrencias:
                print(f'\nTivemos um match: \033[35m{ocorrencia}\033[m')
        except (ValueError, TypeError):
            print('\033[31mTivemos um problema com os tipos de dados que você digitou! '
                  'Necessário que seja um número inteiro!\033[m')
