import re
import time

# Função RG aleatório com interação com o(a) usuário(a):


def regex():  # Iniciando a função
    while True:  # Looping para verificarmos quantos RG quisermos
        op = str(input('\nPara continuarmos o procedimento, pressione qualquer tecla ou s para sair... ')).strip().lower()
        if op == 's':
            print('\n\033[33mFinalizando...\033[m')
            break
        else:
            try:  # Tratamento de erros
                rg = str(input('\nInforme um RG (deve-se ter em sequência, (2.3.3-1): '))
                print('\n\033[31mVerificando o RG digitado...\033[m\n')
                time.sleep(4)
                print(f'\033[34mO RG digitado foi:\033[m \033[35m{rg}\033[m')
                p = re.compile(r'\d{2}\.\d{3}\.\d{3}-\d')  # Fazendo a verificação com o regex
                # (explicação como funciona os comandos nos códigos de regex)
                print(f'\n\033[34mVerificando o RG digitado:\033[m \033[35m{rg}\033[m')
                time.sleep(2)
                ocorrencias = p.finditer(rg)  # Virá um objeto iterador para trazer todas as ocorrências do padrão texto
                for ocorrencia in ocorrencias:
                    print(f'\nTivemos um match: \033[35m{ocorrencia}\033[m')
                p2 = re.search(r'\d{2}\.\d{3}\.\d{3}-\d', rg)  # Fazendo a verificação para ver se é um RG
                if p2:
                    print('\n\033[33mTemos um RG!\033[m')
                else:
                    print("\n\033[31mNenhum match\033[m")
            except (ValueError, TypeError):
                print('\033[31mTivemos um problema com os tipos de dados que você digitou! '
                      'Necessário que seja um número inteiro!\033[m')


regex()
