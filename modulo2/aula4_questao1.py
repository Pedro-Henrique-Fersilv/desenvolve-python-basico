#Solicitando dados
comprimento = int(input("Comprimento em m²: "))
largura = int(input("Largura em m²: "))
preco_m = float(input("Valor por m²: "))

#Calculando area 
area = comprimento * largura

#Calculando preço
vtotal = preco_m * area

#Exibindo resultado
print (f"O terreno possui {area}m² e custa R${vtotal:,.2f}")