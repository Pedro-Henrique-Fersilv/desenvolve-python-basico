idade    = int(input("Digite sua idade: "))
jogo_tab = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
jogos_v  = int(input("Quantos jogos já venceu? "))

print ("Apto para ingressar no clube de jogos de tabuleiro:",(idade >= 16 and idade <= 18)
and (jogo_tab == True)
and (jogos_v >= 1))