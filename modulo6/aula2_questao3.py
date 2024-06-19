import random
lista1 = list()
lista2 = list()
interseccao = list()
repeticao = 0

for i in range(10):
    n1 = random.randint(0, 50)
    lista1.append(n1)

    n2 = random.randint(0, 50)
    lista2.append(n2)

for i in lista1:
    if i in lista2 and i not in interseccao:
        interseccao.append(i)

print(f"lista1- {lista1}")
print(f"lista2- {lista2}")
print(f"Interseccao- {sorted(interseccao)}")

print("Contagem")
for i in interseccao:
    print(f"{i}: (lista1= {lista1.count(i)}, lista2= {lista2.count(i)})")