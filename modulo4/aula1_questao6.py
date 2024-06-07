#VENDO A CORREÇÃO PERCEBI QUE PODERIA PERGUNTAR A QUANTIDADE E TIPO SEPARADAMENTE, MAS QUANDO FIZ O EXERCÍCIO PESQUISEI COMO FAZIA ISSO, E ME DERAM UMA SOLUÇÃO QUE ERA ESSE COMANDO ".split()"
N = int(input("Quantos experimentos foram realizados? "))

t_cobaias = 0
t_sapos = 0
t_ratos = 0
t_coelhos = 0

count = 0
while count < N:
    resposta = input().split()
    quant = int(resposta[0])
    tipo = (resposta[1])

    if tipo == 'S':
        t_sapos += quant
    
    elif tipo == 'R':
        t_ratos += quant
    
    elif tipo == 'C':
        t_coelhos += quant
    
    t_cobaias += quant
    count += 1

#Total
print (f"Total: {t_cobaias} cobaias")
print (f"Total de coelhos: {t_coelhos}")
print (f"Total de ratos: {t_ratos}")
print (f"Toatal de sapos: {t_sapos}")

#Percentuais
print (f"Percentual de coelhos: {(t_coelhos / t_cobaias) * 100: .2f}%")
print (f"Percentual de ratos: {(t_ratos / t_cobaias) * 100: .2f}%")
print (f"Percentual de sapos: {(t_sapos / t_cobaias) * 100: .2f}%")
