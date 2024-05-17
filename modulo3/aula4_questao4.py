distancia_km = int(input("Qual a distancia em quilômetros da entrega? "))
peso = float(input("Quanto pesa o pacote em quilogramas? "))

if distancia_km <= 100:
    print ("O valor do frete será de R$", peso + 10) if peso > 10 else ("O valor do frete será de R$", peso)
if distancia_km >= 101 and distancia_km <= 300:
    print ("O valor do frete será de R$", 1.50 * peso)
if distancia_km > 300:
    print ("O valor do frete será de R$", 2 * peso)