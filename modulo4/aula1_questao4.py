n = int(input("Quantos números você que testar? "))
maior = 0

while n > 0:
    x = int(input("Digite um número: "))

    while x > maior:
        maior = x
    n = n - 1

print(f"O maior número deles é: {maior}")