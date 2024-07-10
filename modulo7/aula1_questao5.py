frase = input("Digite uma frase: ")
indices = []

for letra in range(len(frase)):
    if frase[letra] in "AEIOUaeiou":
        indices.append(letra)

print(len(indices), "Vogais")
print("Índices", indices)