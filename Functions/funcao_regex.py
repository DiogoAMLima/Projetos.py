import re
import random
import time

# Função RG aleatório:


def regex():  # Iniciando a função e declarando as variáveis para formação
    num = "0123456789"
    num2 = "0123456789"
    num3 = "0123456789"

    juncao = num + num2  # Juntando para a primeira parte do RG

    juncao2 = num + num2 + num3  # Juntando para a primeira parte do RG

    juncao3 = num + num2 + num3  # Juntando para a primeira parte do RG

    while True:  # Looping para vermos quantos RG aleatórios quisermos
        op = str(input('\nPara continuarmos o procedimento, pressione qualquer tecla ou s para sair... ')).strip().lower()
        if op == 's':
            print('\n\033[33mFinalizando...\033[m')
            break
        else:
            try:  # Tratamento de erros
                tamanho_do_rg = 2
                rg = "".join(random.sample(juncao, tamanho_do_rg))  # Juntando os números relacionadas
                # com o método sample que de acordo com o tamanho, geram os caracteres para o RG
                tamanho_do_rg2 = 3
                rg2 = "".join(random.sample(juncao2, tamanho_do_rg2))
                rg3 = "".join(random.sample(juncao3, tamanho_do_rg2))
                tamanho_do_rg3 = 1
                rg4 = "".join(random.sample(num, tamanho_do_rg3))
                print('\n\033[31mEstamos gerando um RG, por favor aguarde...\033[m\n')
                time.sleep(4)
                rg_completo = rg + "." + rg2 + "." + rg3 + "-" + rg4  # Juntando os números gerados para
                # formar o RG completo
                print(f'\033[34mO RG gerado foi:\033[m \033[35m{rg_completo}\033[m')
                p = re.compile(r'\d{2}\.\d{3}\.\d{3}-\d')  # Fazendo a verificação com o regex
                # (explicação como funciona os comandos nos códigos de regex)
                print(f'\n\033[34mVerificando o RG gerado:\033[m \033[35m{rg_completo}\033[m')
                time.sleep(2)
                ocorrencias = p.finditer(rg_completo)
                for ocorrencia in ocorrencias:
                    print(f'\nTivemos um match: \033[35m{ocorrencia}\033[m')
            except (ValueError, TypeError):
                print('\033[31mTivemos um problema com os tipos de dados que você digitou! '
                      'Necessário que seja um número inteiro!\033[m')


regex()
