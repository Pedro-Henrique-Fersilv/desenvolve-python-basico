#Solicitando dados
genero     = str(input("Digite seu gênero M (Masculino) ou F (Feminino): "))
idade      = int(input("Qual sua idade? "))
tempo_serv = int(input("Quanto tempo de serviço você tem em anos? "))

#Verificando se é possível se aposentar
print (

((genero == "M")
and ( idade > 65)
or  ( tempo_serv >= 30 ))
or  ( idade == 60 and tempo_serv >= 25)

or

((genero == "F")
and ( idade > 60)
or  ( tempo_serv >= 30 ))
or  ( idade == 60 and tempo_serv >= 25)

)