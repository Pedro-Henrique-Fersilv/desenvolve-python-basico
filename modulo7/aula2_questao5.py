import random

def embaralhar_palavras(frase):
    frase = frase.split()
    frase_editada = ""
    for palavra in frase:
        embaralhadas = ""
        if len(palavra) >= 4:
            letras_meio = list(palavra[1:-1])
            for letra in range(len(letras_meio)):
                valor_escolhido = random.choice(letras_meio)
                embaralhadas += valor_escolhido
                letras_meio.remove(valor_escolhido)
                palavra_editada = palavra.replace(palavra[1:-1],embaralhadas)
            frase_editada += palavra_editada + " "
        else:
            frase_editada += palavra + " "

    return(frase_editada)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)