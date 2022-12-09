import time
from visual_automata.fa.nfa import VisualNFA
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

# AFN:
nfa = VisualNFA(
    states={"q0", "q1", "q2", "q3"},  # Estados
    input_symbols={"0", "1"},  # Símbolso de entrada
    transitions={  # Estados de transições
        "q0": {"0": {"q2"}, "1": {"q1"}},
        "q1": {"1": {"q2"}, "0": {"q0", "q2"}},
        "q2": {"0": {"q2"}, "1": {"q0", "q3"}},
        "q3": {},
    },
    initial_state="q0",  # Estado inicial
    final_states={"q0"},  # Estado final
)

print(nfa.table)

print(nfa.show_diagram())  # Olhar no anaconda (colocar display no anaconda e não print)

print('\n')

# Interação com o usuário:

while True:
    try:
        palavra_checar = str(input('\nInforme a sequência de caracteres com dígitos de 0 ou 1: '))
        print(f'\n\033[35mSequência escolhida: {palavra_checar}\033[m')
        print('\nChecando sua sequência...')
        time.sleep(2)
        print(nfa.input_check(f"{palavra_checar}"))
    except KeyError:
        print('\n\033[36mDeveria ser uma sequência de 0 ou 1...\033[m\n')
    op = str(input('\nQuer continuar testando sequências? [S/N] '))
    if op in "Nn":
        print('\n\033[33mFinalizando...\033[m\n')
        break

# Converter AFN para AFD:

nfa2 = NFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": {"q2"}, "1": {"q1"}},
        "q1": {"1": {"q2"}, "0": {"q0", "q2"}},
        "q2": {"0": {"q2"}, "1": {"q0", "q3"}},
        "q3": {},
    },
    initial_state="q0",
    final_states={"q0"},
)

dfa = DFA.from_nfa(nfa2)  # returns an equivalent NFA

dfa2 = VisualDFA(dfa)

print(dfa2.table)

print('\n')

# Interação com o usuário:

while True:
    try:
        palavra_checar = str(input('\nInforme a sequência de caracteres com dígitos de 0 ou 1: '))
        print(f'\n\033[35mSequência escolhida: {palavra_checar}\033[m')
        print('\nChecando sua sequência...')
        time.sleep(2)
        print(dfa2.input_check(f"{palavra_checar}"))
    except KeyError:
        print('\n\033[36mDeveria ser uma sequência de 0 ou 1...\033[m\n')
    op = str(input('\nQuer continuar testando sequências? [S/N] '))
    if op in "Nn":
        print('\n\033[33mFinalizando...\033[m\n')
        break

# print(dfa2.show_diagram())  # Olhar no anaconda (colocar display no anaconda e não print)

minimal_dfa = VisualDFA.minify(dfa2)
minimal_dfa.show_diagram()
