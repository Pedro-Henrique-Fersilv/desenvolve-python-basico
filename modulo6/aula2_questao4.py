#Ficou extenso mas foi a forma que consegui fazer
lista1 = list()
lista2 = list()

def lista_maior_ou_menor(lista1,lista2):
    #Adicionando à lista os valores de cada lista enquanto a menor lista tiver valor
    listas = list()
    if len(lista1) > len(lista2):
        for i in range(len(lista2)):
            listas.append(lista1[i])
            listas.append(lista2[i])
        
        #Definindo range do final da lista menor para a lista maior
        for i in range(len(lista2), len(lista1)):
            listas.append(lista1[i])
        
        return listas
    else:
        for i in range(len(lista1)):
            listas.append(lista1[i])
            listas.append(lista2[i])
        
        #Definindo range do final da lista menor para a lista maior
        for i in range(len(lista1), len(lista2)):
            listas.append(lista2[i])
        
        return listas

q1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {q1} elementos da lista 1: ")
for i in range(q1):
    resposta1 = int(input())
    lista1.append(resposta1)

q2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {q2} elementos da lista 2: ")
for i in range(q2):
    resposta2 = int(input())
    lista2.append(resposta2)

lista_intercalada = lista_maior_ou_menor(lista1,lista2)
print(f"Lista intercalada: {lista_intercalada}")