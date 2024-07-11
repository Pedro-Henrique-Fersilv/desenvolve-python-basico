def validador_senha(senha):
    requisitos = 0
    if len(senha) >= 8:
        requisitos += 1
        #Números
        for c in senha:
            if c in "1234567890":
                requisitos += 1
                break
        #Letras maiúsculas
        for c in senha:
            if ord(c) in range(65,91):
                requisitos += 1
                break
        #Letras minúsculas
        for c in senha:
            if ord(c) in range(97,123):
                requisitos += 1
                break
        #Caracteres especiais
        for c in senha:
            if ord(c) in range(33,48) or ord(c) in range(91,97) or ord(c) in range(123,126) or ord(c) in range(63,65):
                requisitos += 1
                break
    if requisitos == 5:
        return True
    else:
        return False

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))