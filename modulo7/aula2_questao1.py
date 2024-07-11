data = input("Em qual data você nasceu (Ex: dd/mm/aaaa)? ")
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

print("Você nasceu em",data[0:2],"de", meses[int(data[3:5])- 1], "de", data[6:10])