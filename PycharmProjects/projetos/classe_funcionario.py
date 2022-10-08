class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        print(f'\nO nome do funcionário é: \033[31m{nome_func}\033[m')

    def id(self, idade):
        self.idade = idade
        print(f'A idade do \033[31m{nome_func}\033[m é: \033[32m{idade_func}\033[m')

    def prof(self, profissao):
        self.profissao = profissao
        print(f'A profissão do \033[31m{nome_func}\033[m é: \033[33m{prof_func}\033[m')

    def tempo(self, tempo_carreira):
        self.tempo_carreira = tempo_carreira
        print(f'O tempo de carreira do \033[31m{nome_func}\033[m é: \033[34m{tempo_carr_func}\033[m')

    def tempo2(self, tempo_empresa):
        self.tempo_empresa = tempo_empresa
        print(f'O tempo que o \033[31m{nome_func}\033[m tem na empresa é: \033[35m{tempo_empr_func}\033[m')

    def id_funcional_empresa(self, id_funcional):
        self.id_funcional = id_funcional
        print(f'O ID funcional do \033[31m{nome_func}\033[m é \033[36m{id_func}\033[m')

    def sal(self, salario):
        self.salario = salario
        print(f'O salário do \033[31m{nome_func}\033[m é: \033[37mR$ {salario_mensal:.2f}\033[m')

    def _aumenta_sal(self):
        self.msg = f'\nO salário de: \033[97m{salario_mensal}\033[m permanecerá o mesmo...'
        if self.salario <= 2000:
            novo_salario = salario_mensal + ((salario_mensal / 100) * 25)
            self.msg = f'\nO salário só aumentará em 6 meses. O novo salário será: \033[34mR$ {novo_salario:.2f}\033[m'
        elif self.salario >= 4500:
            novo_salario = salario_mensal + ((salario_mensal / 100) * 15)
            self.msg = f'\nO salário aumentará no mês que vem. O novo salário será: \033[30mR$ {novo_salario:.2f}\033[m'
        return self.msg

    def verifica_aumento(self):
        print(f'O salário recebido de: \033[32m{salario_mensal}\033[m é um bom salário')
        print(self._aumenta_sal())


while True:
    try:
        nome_func = str(input('\nInforme o nome do funcionário: '))
        idade_func = int(input('Informe a idade do funcionário: '))
        prof_func = str(input('Informe a profissão do funcionário: '))
        tempo_carr_func = str(input('Informe o tempo de carreira do funcionário: '))
        tempo_empr_func = str(input('Informe o tempo na empresa do funcionário: '))
        id_func = str(input('Informe o ID funcional: '))
        salario_mensal = float(input('Informe o salário do funcionário: '))
        res = Funcionario(nome_func)
        res.id(idade_func)
        res.prof(prof_func)
        res.tempo(tempo_carr_func)
        res.tempo2(tempo_empr_func)
        res.id_funcional_empresa(id_func)
        res.sal(salario_mensal)
        res.verifica_aumento()
    except (ValueError, KeyboardInterrupt):
        print('\n\033[36mHouve um problema com o tipo de dado informado ou o usuário interrompeu a entrada de '
              'informações, tente novamente...\033[m')
    esc = str(input('\nDeseja continuar? [S/N]? ')).strip().upper()
    if esc in 'S':
        continue
    else:
        print('\n\033[33mAté a próxima...\033[m')
        break
