import random

def imprime_enforcado(n):
    if erros == 8:
            print("Você Perdeu!")
            print("Palavra correta:", palavra)
            exit()
    for estagio in estagio_lista[erros]:
        print(estagio.rstrip())

#Escolhendo palavra aleatória
with open('gabarito_forca.txt', 'r') as f:
    palavras = f.readlines()
    palavra = random.choice(palavras).strip()

#Lendo os estagios do gabarito enforcado
with open('gabarito_enforcado.txt', 'r') as f:
    estagios = f.readlines()
    estagio_lista = []
    estagio_lista.append(estagios[0:5])
    estagio_lista.append(estagios[6:11])
    estagio_lista.append(estagios[12:17])
    estagio_lista.append(estagios[18:23])
    estagio_lista.append(estagios[24:29])
    estagio_lista.append(estagios[18:23])
    estagio_lista.append(estagios[30:35])
    estagio_lista.append(estagios[36:41])

for estagio in estagio_lista[0]:
    print(estagio.rstrip())
print(f"A palavra tem {len(palavra)} letras")
estado_atual = ['_' for _ in palavra]
erros = 0

while True:
    print(" ".join(estado_atual))
    letra = input("Insira uma letra: ").lower()
    if letra in palavra:
        #Daqui não consegui fazer com o que foi ensinado até agora, peguei no chatgpt
        for i, char in enumerate(palavra):
            if char == letra:
                estado_atual[i] = letra
        if "_" not in estado_atual:
            print("Parabéns, você adivinhou a palavra!")
            exit()
        #Até aqui--------------------------------------------------------------------------
    else:
        erros += 1
        imprime_enforcado(erros)