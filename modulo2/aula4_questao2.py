#Solicitando temperatura em Fahrenheit
temp_f = int(input("Temperatura em graus Fahrenheit: "))

#Convertendo Fahrenheit em Celsius
temp_c = int((temp_f - 32) * 5 / 9)

#Exibindo o resultado
print (f"São {temp_c}°C")