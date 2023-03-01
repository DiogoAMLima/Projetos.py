import numpy as np

print("\033[31m--------------SOMA DE VETORES DIVERSOS--------------\033[m")  # Título e cor

# Mostrando os valores dos vetores definidos:

print("\nO vetor 1 é: [1, 1, 1, 1, 1]")
print("O vetor 2 é: [5, 5, 6, 6, 13]")
print("O vetor 3 é: [2, 3, 4, 1, 1]")

# Colocando os valores dentro de um vetor:

vetor_1 = np.array([1, 1, 1, 1, 1])
vetor_2 = np.array([5, 5, 6, 6, 13])
vetor_3 = np.array([2, 3, 4, 1, 1])
vetor_4 = vetor_1 + vetor_2 + vetor_3  # Somando os 3 vetores em uma variável nova
print(f"\nA soma dos 3 primeiros vetores resultando em um quarto vetor que será: \033[35m{vetor_4}\033[m")

# Mostrando os valores de outros vetores definidos:

print("\nO vetor 5 é: [67, 77, 87, 97, 8]")
print("O vetor 6 é: [3, 11, 8, 8, 8]")
print("O vetor 7 é: [1000, 12, 12, 1000, 1]")

vetor_5 = np.array([67, 77, 87, 97, 8])
vetor_6 = np.array([3, 11, 8, 8, 8])
vetor_7 = np.array([1000, 12, 12, 1000, 1])
vetor_8 = vetor_5 + vetor_6 + vetor_7
print(f"\nA soma dos vetores 5, 6 e 7 resulta em um oitavo vetor que será: \033[32m{vetor_8}\033[m")

# Mostrando os valores dos últimos vetores definidos:

print("\nO vetor 9 é: [12, 13, 14, 15, 16]")
print("O vetor 10 é: [0, 0, 0, 0, 6]")
print("O vetor 11 é: [-1, -8, -3, -10, -11]")

vetor_9 = np.array([12, 13, 14, 15, 16])
vetor_10 = np.array([0, 0, 0, 0, 6])
vetor_11 = np.array([-1, -8, -3, -10, -11])
vetor_12 = vetor_9 + vetor_10 + vetor_11
print("\nA soma dos últimos vetores (9, 10 e 11) resulta em um décimo segundo vetor que será: "
      "\033[33m{}\033[m".format(vetor_12))

# Permanecendo a linha 41 e 42 com o .format apenas para exemplo

print("\n\033[31m----------------------------------------------------\033[m")
