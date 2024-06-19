import random
n_aleatorios = list()

for i in range(20):
    n = random.randint(-100, 100)
    n_aleatorios.append(n)

print(sorted(n_aleatorios))
print(n_aleatorios)
print(n_aleatorios.index(max(n_aleatorios)))
print(n_aleatorios.index(min(n_aleatorios)))