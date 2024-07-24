import os

#O texto das primeiras 25 linhas
with open('estomago.txt', 'r') as f:
    texto = f.readlines()

nao_vazia = 0
for linha in texto:
    if nao_vazia == 25:
        break
    elif linha.strip():
        print(linha.strip())
        nao_vazia += 1

#O número de linhas do arquivo
n_linhas = 0
for linha in texto:
    if linha.strip():
        n_linhas += 1
print("Número de linhas:",n_linhas)

#A linha com maior número de caracteres
linha_anterior = 0
for linha in texto:  
    if len(linha) > linha_anterior:
        linha_maior = linha.strip()
        linha_anterior = len(linha)
    else:
        linha_anterior = len(linha)
print(f"Linha maior:",linha_maior)

#Número de menções "Nonato" e "Íria"
n_mencoes = 0
for linha in texto:
    if "nonato" in linha.lower() or "íria" in linha.lower():
        n_mencoes += 1
print("Número de menções:", n_mencoes)