numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + numero

numero = numero[0:5] + "-" + numero[5:9]
print(numero)