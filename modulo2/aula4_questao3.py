#Solicitando dados
nome = str(input("Digite o nome do produto 1: "))
preco_u = float(input("Digite o preço unitário do produto 1: "))
quant = float(input("Digite a quantidade do produto 1: "))
preco_t = preco_u * quant

nome = str(input("Digite o nome do produto 2: "))
preco_u = float(input("Digite o preço unitário do produto 2: "))
quant = float(input("Digite a quantidade do produto 2: "))
preco_t += preco_u * quant

nome = str(input("Digite o nome do produto 3: "))
preco_u = float(input("Digite o preço unitário do produto 3: "))
quant = float(input("Digite a quantidade do produto 3: "))
preco_t += preco_u * quant

#Exibindo resultados
print (f"Total: R$ {preco_t:,.2f}")