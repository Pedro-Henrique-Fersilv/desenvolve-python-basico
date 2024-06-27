#Forma que encontrei de fazer sem ver a resposta
import random

lista = list()
n_negativo = list()
maior_negativo = list()

for i in range(20):
    lista.append(random.randint(-10,10))

#Teste da maior fatia
for i in range(len(lista)):
    if lista[i] < 0:
        n_negativo.append(i)
    else:
        if len(n_negativo) > len(maior_negativo):
            maior_negativo = n_negativo
        n_negativo = []

if len(n_negativo) > len(maior_negativo):
    maior_negativo = n_negativo

#Definindo índice
inicio = maior_negativo[0]
fim = maior_negativo[-1]

#Exibindo resultado
print(lista)
del lista[inicio:(fim+1)]
print(lista)