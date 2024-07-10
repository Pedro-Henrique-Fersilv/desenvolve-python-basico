#Solicitando e testando se o valor digitado atende aos requisitos
cpf = input("Digite o CPF, Ex:(XXX.XXX.XXX-XX): ")
if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-" or len(cpf) != 14:
    print("Cpf digitado incorretamente, forma correta Ex: XXX.XXX.XXX-XX")
    exit()

#Tirando caracteres do cpf e criando lista com os valores
cpf = cpf.replace(".", "").replace("-", "")
cpf_int = [int(d) for d in cpf[0:9]]

def verificadigito(multiplicador):
    #Multiplicando cada um dos número da direita para a esquerda por números crescentes a partir do número 2
    soma = 0
    for d in range(len(cpf_int)):
        soma += (cpf_int[d] * multiplicador)
        multiplicador -= 1

    #Verificando resto
    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto
    return digito

#Adicionando o digito1 ao cpf
cpf_int.append(verificadigito(10))
#Adicionando o digito2 ao cpf
cpf_int.append(verificadigito(11))

#Criando "cpf_valido" para transformar o cpf int em string
cpf_valido = ""
for i in cpf_int:
    cpf_valido += str(i)

#Exibindo resultado
if cpf == cpf_valido:
    print("Válido")
else:
    print("Inválido")