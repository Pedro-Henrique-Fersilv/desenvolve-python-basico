import random
import math

resultado = 0
n = int(input("Digite um número: "))

for i in range(n):
    r = random.randint(1,100)
    resultado += r
resultado = math.sqrt(resultado)

print(round(resultado,2))