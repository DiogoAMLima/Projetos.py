from visual_automata.fa.dfa import VisualDFA
from automata.fa.dfa import DFA
import time

dfa = VisualDFA(
    states={"q0", "q1", "q2", "q3", "q4", "q5"},  # Estados
    input_symbols={"0", "1"},  # Símbolso de entrada
    transitions={  # Estados de transições
        "q0": {"0": "q3", "1": "q1"},
        "q1": {"0": "q3", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q4", "1": "q1"},
        "q4": {"0": "q4", "1": "q5"},
        "q5": {"0": "q5", "1": "q3"}
    },
    initial_state="q0",  # Estado inicial
    final_states={"q3", "q5"},  # Estados finais
)

print(dfa.table)

dfa.show_diagram()

# Interação com o usuário:

while True:
    try:
        palavra_checar = str(input('\nInforme a quantidade de caracteres da sequência de dígitos com 0 e 1: '))
        print(f'\n\033[35mSequência escolhida: {palavra_checar}\033[m')
        print('\nChecando sua sequência...')
        time.sleep(2)
        print(dfa.input_check(f"{palavra_checar}"))
    except KeyError:
        print('\n\033[36mDeveria ser uma sequência de 0 ou 1...\033[m\n')
    op = str(input('\nQuer continuar testando sequências? [S/N] '))
    if op in "Nn":
        print('\n\033[33mFinalizando...\033[m\n')
        break


# AFD:
dfa2 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q3'},
        'q3': {'0': 'q3', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q1', 'q3'}
)

print('\033[37mEstados: q0, q1, q2, q3\033[m')
print('\033[33mSímbolos de entradas: 0 e 1\033[m')
print('\033[34mTransições: q0: {"0": "q0", "1": "q1"}')
print('Transições: q1: {"0": "q0", "1": "q2"}')
print('Transições: q2: {"0": "q2", "1": "q3"}')
print('Transições: q3: {"0": "q3", "1": "q0"}\033[m')
print('\033[32mEstado inicial: →q0\033[m')
print('\033[32mEstados finais: q1, q3\033[m')

# Interação com o usuário:

while True:
    palavra_checar2 = str(input('\nInforme uma sequência de digitos com 0 e 1: '))
    print(f'\n\033[35mSequência escolhida: {palavra_checar2}\033[m')
    print('\nChecando sua sequência...')
    time.sleep(2)
    if dfa2.accepts_input(palavra_checar2):
        print('\n\033[31mAceito\033[m')
    else:
        print('\n\033[31mRejeitado\033[m')
    op2 = str(input('\nQuer continuar testando sequências? [S/N] '))
    if op2 in "Nn":
        print('\n\033[33mFinalizando...\033[m\n')
        break

# Testando entradas:

print(dfa2.read_input('0111'))  # Retornará q3

print(list(dfa2.read_input_stepwise('0111')))  # Retornará o caminho do automato '['q0', 'q0', 'q1', 'q2', 'q3']'
