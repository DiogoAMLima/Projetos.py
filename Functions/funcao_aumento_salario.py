def aumento_salario():  # Definindo a função com tratamento de erros
    try:
        s_a = float(input('Informe o valor do salário atual do funcionário: '))
        t_s = int(input('Informe o tempo que o funcionário trabalha na empresa: '))
        # Condicionais para bonificação e aumento do salário
        if t_s <= 1:
            bonificao = 50
        elif t_s <= 2:
            bonificao = 100
        elif t_s <= 3:
            bonificao = 200
        else:
            bonificao = 350

        if s_a <= 1000:
            n_s = (s_a + (s_a / 100) * 30) + bonificao
            print(f'\nO salário atual é: \033[32mR${s_a:.2f}\033[m, o funcionário trabalha há \033[30m{t_s}\033[m '
                  f'ano(s) na empresa e o novo salário será de: \033[33mR${n_s:.2f}\033[m')
        elif s_a <= 2000:
            n_s = (s_a + (s_a / 100) * 25) + bonificao
            print(f'\nO salário atual é: \033[32mR${s_a:.2f}\033[m, o funcionário trabalha há \033[30m{t_s}\033[m '
                  f'ano(s) na empresa e o novo salário será de: \033[33mR${n_s:.2f}\033[m')
        elif s_a <= 3200:
            n_s = (s_a + (s_a / 100) * 20) + bonificao
            print(f'\nO salário atual é: \033[32mR${s_a:.2f}\033[m, o funcionário trabalha há \033[30m{t_s}\033[m '
                  f'ano(s) na empresa e o novo salário será de: \033[34mR${n_s:.2f}\033[m')
        elif s_a <= 4500:
            n_s = (s_a + (s_a / 100) * 15) + bonificao
            print(f'\nO salário atual é: \033[32mR${s_a:.2f}\033[m, o funcionário trabalha há \033[30m{t_s}\033[m '
                  f'ano(s) na empresa e o novo salário será de: \033[35mR${n_s:.2f}\033[m')
        elif s_a <= 6000:
            n_s = (s_a + (s_a / 100) * 10) + bonificao
            print(f'\nO salário atual é: \033[32mR${s_a:.2f}\033[m, o funcionário trabalha há \033[30m{t_s}\033[m '
                  f'ano(s) na empresa e o novo salário será de: \033[36mR${n_s:.2f}\033[m')
        else:
            n_s = (s_a + (s_a / 100) * 5) + bonificao
            print(f'\nO salário atual é: \033[32mR${s_a:.2f}\033[m, o funcionário trabalha há \033[30m{t_s}\033[m '
                  f'ano(s) na empresa e o novo salário será de: \033[97mR${n_s:.2f}\033[m')
    except(TypeError, ValueError, KeyboardInterrupt):
        print('\n\033[31mTivemos um problema com o tipo de dado que você digitou ou o(a) '
              'usuário(a) interrompeu a entrada de dados\033[m')


aumento_salario()
