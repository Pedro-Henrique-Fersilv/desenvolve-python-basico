import random

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave_aleatoria = random.randint(1,10)

def encrypt(nome):
    nome_criptografado = ""
    for c in nome:
        n = ord(c)
        if n + chave_aleatoria > 126:
            criptografado = 33 + (n + chave_aleatoria - 127)
        else:
            criptografado = n + chave_aleatoria
        nome_criptografado += chr(criptografado)
    return nome_criptografado

print("Nomes criptografados:",list(map(encrypt, nomes)))