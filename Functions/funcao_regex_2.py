import re
import time

# Função RG aleatório com interação com o(a) usuário(a):


def regex():
    while True:
        op = str(input('\nPara continuarmos o procedimento, pressione qualquer tecla ou s para sair... ')).strip()
        if op == 's':
            print('\n\033[33mFinalizando...\033[m')
            break
        else:
            try:
                rg = str(input('\nInforme um RG (deve-se ter em sequência, (2.3.3-1): '))
                print('\n\033[31mVerificando o RG digitado...\033[m\n')
                time.sleep(4)
                print(f'\033[34mO RG digitado foi:\033[m \033[35m{rg}\033[m')
                p = re.compile(r'\d{2}\.\d{3}\.\d{3}-\d')
                print(f'\n\033[34mVerificando o RG digitado:\033[m \033[35m{rg}\033[m')
                time.sleep(2)
                ocorrencias = p.finditer(rg)
                for ocorrencia in ocorrencias:
                    print(f'\nTivemos um match: \033[35m{ocorrencia}\033[m')
            except (ValueError, TypeError):
                print('\033[31mTivemos um problema com os tipos de dados que você digitou! '
                      'Necessário que seja um número inteiro!\033[m')


regex()
