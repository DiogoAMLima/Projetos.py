from PySimpleGUI import PySimpleGUI as sg

sg.theme('Dark')

layout_temas = [
    [sg.Text('Lista dos temas disponíveis a seguir...')],
    [sg.Text('Escolha um dos temas para pré-visualização')],
    [sg.Listbox(values=sg.theme_list(),
                size=(20, 14),
                key='———LISTA———',
                enable_events=True)],
    # [sg.Button('Saída')]
]

window = sg.Window('Lista de temas', layout_temas)

while True:
    eventos, valores = window.read()

    if eventos in (None, 'Saída'):
        break
    sg.theme(valores['———LISTA———'][0])
    sg.popup_get_text(f'Este é o tema: {valores["———LISTA———"][0]}')
    if eventos == sg.WIN_CLOSED:
        print('\n\033[32mAté a próxima...\033[m')
        break

lista_nomes = sg.theme_list()  # Variável para mostrar todos os nomes
print(lista_nomes)  # Printando os nomes para escolher

op = str(input('\nEscolha uma das opções acima: '))
if op in lista_nomes:
    print('\n\033[33mTema escolhido com sucesso!\033[m')

    texto_1 = str(input('\nInforme o nome que aparecerá no login: '))
    texto_2 = str(input('Informe o nome que aparecerá na senha: '))
    resposta = str(input(f'\nInforme a resposta certa para o campo \033[35m{texto_1}:\033[m '))
    resposta2 = str(input(f'Informe a resposta certa para o campo \033[35m{texto_2}:\033[m '))

    # Layout:
    sg.theme(f'{op}')  # Escolhendo o tema
    layout = [
        [sg.Text(f'{texto_1}'), sg.Input(key='usuário', size=(23, 1))],  # Size = (largura e altura)
        [sg.Text(f'{texto_2}'), sg.Input(key='senha', password_char='*', size=(23, 1))],  # Senha não será exibida
        [sg.Checkbox('Deseja salva o login para próximas vezes?')],
        [sg.Button('Entrar')],
    ]

    # Window:
    janela = sg.Window('Tela de login', layout)
    
    # Lendo os eventos:

    while True:
        events, values = janela.read()
        if events == sg.WIN_CLOSED:
            print('\n\033[32mAté a próxima...\033[m')
            break
        if events == 'Entrar':
            if values['usuário'] == f'{resposta}' and values['senha'] == f'{resposta2}':
                sg.popup("Login efetuado com sucesso!", title='Caixa', text_color='green')
                print('\n\033[31mLogin efetuado com sucesso!\033[m')
            else:
                sg.popup('Login ou senha inválidos...', title='Caixa', text_color='red')
                print('\n\033[97mLogin ou senha inválidos...\033[m')
else:
    print('\n\033[34mNão temos essa tema...\033[m')
    
