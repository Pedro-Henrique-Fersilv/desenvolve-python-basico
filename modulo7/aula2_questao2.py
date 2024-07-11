frase = input("Digite uma frase: ")
sem_vogal = frase

for letra in sem_vogal:
    if letra in "AEIOUaeiou":
        sem_vogal = sem_vogal.replace(letra,"*")

print("Frase modificada:",sem_vogal)