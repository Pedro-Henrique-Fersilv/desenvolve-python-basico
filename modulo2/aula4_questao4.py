#Solicitando dados
valor_t = int((input("Valor que será convertido em notas: ")))

#Verificando quanto falta depois da maior nota e armazenando quantas notas são necessárias
nota100 = valor_t // 100
valor_t = valor_t % 100

nota50 = valor_t // 50
valor_t = valor_t % 50

nota20 = valor_t // 20
valor_t = valor_t % 20

nota10 = valor_t // 10
valor_t = valor_t % 10

nota5 = valor_t // 5
valor_t = valor_t % 5

nota2 = valor_t // 2
valor_t = valor_t % 2

nota1 = valor_t // 1
valor_t = valor_t % 1

#Exibindo resultado
print (nota100, " Nota(s) de R$100,00")
print (nota50,  " Nota(s) de R$50,00")
print (nota20, " Nota(s) de R$20,00")
print (nota10, "Nota(s) de R$10,00")
print (nota5, "Nota(s) de R$5,00")
print (nota2, "Nota(s) de R$2,00")
print (nota1, "Nota(s) de R$1,00")