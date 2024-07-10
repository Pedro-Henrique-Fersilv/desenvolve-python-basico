frase = input("Digite uma frase: ")
palavras = frase.lower().split()
objetivo = (list(input("Digite a palavra objetivo: ")))

for palavra in palavras:
    if sorted(palavra) == sorted(objetivo):
        print(palavra) 