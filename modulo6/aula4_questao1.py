n_pares_20a50 = [n for n in range(20,51) if n % 2 == 0]
quadrado_n = [n**2 for n in range(1,10)]
div_7 = [n for n in range(1,101) if n % 7 == 0]
par_impar = ["Par" if n % 2 == 0 else "Ímpar" for n in range(0,30,3)]

print(n_pares_20a50)
print(quadrado_n)
print(div_7)
print(par_impar)