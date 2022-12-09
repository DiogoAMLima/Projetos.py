import numpy as np

print("--------------SOMA DE VETORES DIVERSOS--------------")

print("O vetor 1 é: [1, 1, 1, 1, 1]")
print("O vetor 2 é: [5, 5, 6, 6, 13]")
print("O vetor 3 é: [2, 3, 4, 1, 1]")

print("\n")

vetor_1 = np.array([1, 1, 1, 1, 1])
vetor_2 = np.array([5, 5, 6, 6, 13])
vetor_3 = np.array([2, 3, 4, 1, 1])
vetor_4 = vetor_1 + vetor_2 + vetor_3
print("A soma dos 3 primeiros vetores resultando em um quarto vetor que será: {}".format(vetor_4))

print("\n")

print("O vetor 5 é: [67, 77, 87, 97, 8]")
print("O vetor 6 é: [3, 11, 8, 8, 8]")
print("O vetor 7 é: [1000, 12, 12, 1000, 1]")

print("\n")

vetor_5 = np.array([67, 77, 87, 97, 8])
vetor_6 = np.array([3, 11, 8, 8, 8])
vetor_7 = np.array([1000, 12, 12, 1000, 1])
vetor_8 = vetor_5 + vetor_6 + vetor_7
print("A soma dos vetores 5, 6 e 7 resulta em um oitavo vetor que será: {}".format(vetor_8))

print("\n")

print("O vetor 9 é: [12, 13, 14, 15, 16]")
print("O vetor 10 é: [0, 0, 0, 0, 6]")
print("O vetor 11 é: [-1, -8, -3, -10, -11]")

vetor_9 = np.array([12, 13, 14, 15, 16])
vetor_10 = np.array([0, 0, 0, 0, 6])
vetor_11 = np.array([-1, -8, -3, -10, -11])
vetor_12 = vetor_9 + vetor_10 + vetor_11
print("A soma dos últimos vetores (9, 10 e 11) resulta em um décimo segundo vetor que será: {}".format(vetor_12))

print("----------------------------------------------------")
