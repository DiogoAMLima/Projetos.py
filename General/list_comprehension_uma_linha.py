# soma = []
# for i in range(5):
#     soma.append(i+i)
#
# print(soma)


soma = [i+i for i in range(5)]
print(f'\033[31m{soma}\033[m')


# mult = []
# for i in range(7):
#     if i % 2 == 1:
#         mult.append(i*3)
#
# print(mult)

mult = [i*3 for i in range(7) if i % 2 == 1]
print(f'\033[31m{mult}\033[m')
