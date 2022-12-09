# Exemplo de generator:

works = [("trabalho", 70), ("trabalho", 60), ("trabalho", 100)]
work_time = (work[1] for work in works if work[0] == "trabalho")
# print(sum(work_time))  # Podemos fazer sem colocar mais uma variável
worked_time = sum(work_time)
print(f'\n\033[36mTempo trabalhado foi de: {worked_time}\033[m')
