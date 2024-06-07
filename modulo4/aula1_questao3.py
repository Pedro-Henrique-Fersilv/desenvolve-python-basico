n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
m = (n1 +n2 +n3)/3

while m >= 60:
    print("Aprovado!")

while m>= 40:
    print("Recuperação!")

print("Reprovado")
print("Fim")