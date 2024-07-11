while True:
    frase = input("Digite uma frase (digite \"fim\" para encerrar): ")
    if frase == "fim":
        exit()
    frase_limpa	= frase.lower()
    frase_limpa = [letra for letra in frase_limpa if ord(letra) >= 97 and ord(letra) <= 122]
    frase_inv = []

    for i in range(len(frase_limpa), 0, -1):
        frase_inv.append(frase_limpa[i-1])

    if frase_limpa == frase_inv:
        print(f"\"{frase}\" é palíndromo")
    else:
        print(f"\"{frase}\" não é palíndromo")