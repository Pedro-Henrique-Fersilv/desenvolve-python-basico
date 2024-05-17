#Solicitando dados
classe = str(input("Escolha a classe (Guerreiro, Mago ou Arqueiro): "))
forca  = int(input("Digite os pontos de força (de 1 a 20): "))
magia  = int(input("Digite os pontos de magia (de 1 a 20): "))

#Testando as 3 classes e seus respectivos pontos, para verificar a validade
print ("Pontos de atributo consistentes com a classe escolhida: ",
((classe == "Guerreiro")
and (forca >= 15)
and (magia <= 10))

or

((classe == "Mago")
and (forca <= 10)
and (magia >= 15))

or

((classe == "Arqueiro")
and (forca > 5 and forca < 15)
and (magia > 5 and forca < 15))

)