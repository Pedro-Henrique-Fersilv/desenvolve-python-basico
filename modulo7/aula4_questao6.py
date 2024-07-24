with open('spotify-2023.csv','r', encoding='latin-1') as f:
    arquivo = f.readlines()

count = 0
for linha in arquivo:
    #print(linha.rstrip())
    count += 1
    if count == 5:
        break

top10 = []
count = 0
for linha in arquivo[1:]:
    top = []
    coluna = linha.strip().split(',')
    #Testando se tem mais de um artista ou músicas com caracteres especiais
    if len(coluna) == 24:
        if (int(coluna[3]) >= 2012 and int(coluna[3]) <= 2022):
            top.append(coluna[0])
            top.append(coluna[1])
            top.append(coluna[3])
            top.append(coluna[8])
            top10.append(top)
            count += 1
            if count == 10:
                break

for top in top10:
    print(top)
#Não consegui colocar a musica mais tocada de cada ano, tentei por 4 horas e não consegui