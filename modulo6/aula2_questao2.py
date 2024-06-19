import random
elementos = list()
num_elementos = random.randint(5, 20)
print(num_elementos)

for i in range(num_elementos):
    n = random.randint(1, 10)
    elementos.append(n)

media = sum(elementos)/len(elementos)

print(elementos)
print(sum(elementos))
print(f"{media:.2f}")