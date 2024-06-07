N = int(input("Quantos respondentes? "))
m_idade = 0

count = 0
while count < N:
    idade = int(input("Digite um número: "))
    m_idade += idade
    
    count += 1

m_idade /= N

print(f"A média de idade é de: {int(m_idade)}")