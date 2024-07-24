import os

def remove_nao_alfabetico(conteudo):
    texto_limpo = ""
    for palavra in conteudo:
        for caracter in palavra:
            if ord(caracter) >= 65 and ord(caracter) <= 90 or ord(caracter) >= 97 and ord(caracter) <= 122:
                texto_limpo += caracter
        texto_limpo += " "
    return texto_limpo.split()

with open ('frase.txt', 'r') as f:
    conteudo = f.read().split()
    conteudo = remove_nao_alfabetico(conteudo)

with open ('palavras.txt', 'w') as f:
    for palavra in conteudo:
        if palavra != conteudo[-1]:
            f.write(palavra + '\n')
        else:
            f.write(palavra)