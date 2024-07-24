import os

with open("frase.txt", 'w') as f:
    f.write(input("Digite uma frase: "))

print("Frase salva em", os.path.abspath('frase.txt'))