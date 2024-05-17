ano = int(input("Qual o ano? "))

if (ano % 4 == 0) and (not ano % 100 == 0) or (ano % 400 == 0):
    print ("Bissexto")
else:
    print("Não Bissexto")