import random
r = 0
n = random.randint(1,10)

while r != n:
    r = int(input("Adivinhe o número entre 1 e 10: "))
    
    if r > n: print("Muito alto, tente novamente!")
    elif r < n: print("Muito baixo, tente novamente!")

print(f"Correto! O número é {n}")