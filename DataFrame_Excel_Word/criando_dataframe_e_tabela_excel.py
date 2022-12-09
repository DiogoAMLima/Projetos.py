import pandas as pd

nomes = []
idades = []
sexo = []
cores = []
m = 0
f = 0

while True:
    try:
        nome = str(input('\nInforme um nome para a coluna "Nomes": '))
        nomes.append(nome)
        idade = str(input(f'Informe a idade do(a) {nome} para a coluna "Idades": '))
        idades.append(idade)
        cor = str(input(f'Informe a cor favorita do(a) {nome} para a coluna "Cores": ')).upper()
        cores.append(cor)
        s = str(input(f'Informe o sexo do(a) {nome} para a coluna "Sexo": [m/f] ')).upper()
        sexo.append(s)
        if s == 'M':
            m += 1
        elif s == 'F':
            f += 1
        elif s not in 'MF':
            print('\n\033[35mNão encontramos o sexo informado...\033[m')
            break
        resp = str(input('\nQuer inserir os dados de outra pessoa? \033[32m[S/N]\033[m '))
        if resp not in 'sS':
            break
        else:
            continue
    except KeyboardInterrupt:
        print('\n\033[31mO usuário interrompeu a entrada de informações...\033[m')
        break

print(f'\nA lista contém \033[33m{len(nomes)}\033[m nome(s) e eles são por ordem de inserção: \033[34m{nomes}\033[m')
print(f'\nA lista contém \033[34m{len(idades)}\033[m idade(s) e elas são por ordem de inserção: \033[33m{idades}\033[m')
print(f'\nA lista contém \033[35m{len(sexo)}\033[m sexo(s) informados e '
      f'são eles por ordem de inserção: \033[35m{sexo}\033[m. A quantidade de sexo '
      f'Feminino e Masculino respectivamente é: \033[37m{f}\033[m e \033[36m{m}\033[m')
print(f'\nA lista contém \033[31m{len(cores)}\033[m cor(es) e elas são por ordem de inserção: \033[31m{cores}\033[m')

print()

dados = {'Nomes': nomes, 'Idades': idades, 'Cores': cores, 'Sexo': sexo}

tabela = pd.DataFrame(data=dados)
print(tabela)

nome_tabela = str(input('\nInforme o nome do seu arquivo em excel: '))

extensao = '.xlsx'

nome_final = nome_tabela + extensao

print(f'\nEsta será sua planilha: \033[34m{nome_final}\033[m')

folha = str(input('\nInforme o nome da aba do excel: '))

tabela.to_excel(f'{nome_final}', sheet_name=f'{folha}')
