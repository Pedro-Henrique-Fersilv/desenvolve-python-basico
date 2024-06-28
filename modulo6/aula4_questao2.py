frase = str(input("Digite uma frase: "))
vogais = ["a","e","i","o","u"]

vogais_frase = [l for l in frase if l in vogais]
consoantes_frase = [l for l in frase if l not in vogais and not l == " "]

print("Vogais:", sorted(vogais_frase))
print("Consoantes:", consoantes_frase)