ano = 1996
func = 2000
porct = 1.5

while ano <= 2022:
    func = func + (func / 100) * porct
    ano += 1
    porct += porct

print(f'O funcionário recebe atualmente: {func}')
