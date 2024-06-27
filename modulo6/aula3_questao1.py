import random

lista = list()

for i in range(random.randint(4,10)):
    n = int(input("Digite um número: "))
    lista.append(n)

print(lista)
print(lista[:3])
print(lista[-2:])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])