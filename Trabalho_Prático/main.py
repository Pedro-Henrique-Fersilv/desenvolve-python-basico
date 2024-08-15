import os

#----------------------------USUARIOS----------------------------

def cadastrar_usuario(): #solicita os dados e os adiciona ao 'usuarios.csv'(somente clientes)
    os.system("cls")
    nome = input("Nome do Usuário: ")
    cpf = input("Cpf: ")
    telefone = input("Telefone: ")
    senha = input("Senha: ")
    with open('data/usuarios.csv', 'a') as f:
        f.write(f"{nome},{senha},{cpf},{telefone},\n")
    os.system("cls")
    print("Usuário Cadastrado com sucesso!")

def remover_usuario():
    os.system("cls")
    cpf = input("Digite o Cpf do usuário: ")
    encontrado = False
    with open('data/usuarios.csv', 'r') as f:
        linhas = f.readlines()

    os.system("cls")
    #Reescreve o csv removendo o usuario encontrado
    with open('data/usuarios.csv', 'w') as f: 
        for linha in linhas:
            if cpf != linha.split(",")[2]: #Se não for o Cpf solicitado reescreve a linha
                f.write(linha)
            else:
                encontrado = True
    if not encontrado:
        print("O Cpf informado não foi encontrado.")
    else:
        print("Usuário removido com sucesso!")

def atualizar_usuario():
    os.system("cls")
    cpf = input("Digite o Cpf do usuário a ser atualizado: ")

    os.system("cls")
    print("Digite os dados para que sejam atualizados:")
    nome_atualizado = input("Nome do Usuário: ")
    cpf_atualizado = input("Cpf: ")
    telefone_atualizado = input("Telefone: ")
    senha_atualizada = input("Senha: ")

    encontrado = False
    with open('data/usuarios.csv', 'r') as f:
        linhas = f.readlines()

    os.system("cls")
    #Reescreve o csv renomeando o usuario encontrado
    with open('data/usuarios.csv', 'w') as f: 
        for linha in linhas:
            if cpf != linha.split(",")[2]:    #Se não for o Cpf solicitado reescreve a linha
                f.write(linha)
            else:                             #Se for escreve a linha com os dados atualizados
                f.write(f"{nome_atualizado},{senha_atualizada},{cpf_atualizado},{telefone_atualizado},\n")
                encontrado = True
    if not encontrado:
        print("O Cpf informado não foi encontrado.")
    else:
        print("Usuário atualizado com sucesso!")

def buscar_usuario():
    os.system("cls")
    encontrado = False
    busca = input("Digite o nome desejado: ")
    with open('data/usuarios.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    os.system("cls")
    for linha in linhas[1:]:
        if busca.lower() in linha.lower(): #Se a pesquisa estiver presente na linha printa ela
            print(linha.rstrip())
            encontrado = True
    if not encontrado:
        print("O nome informado não foi encontrado.")

def listar_usuarios():
    os.system("cls")
    with open('data/usuarios.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    for linha in linhas[1:]: #Printa todas as linhas
        print(linha.rstrip())

def listar_usuarios_ordenados():
    os.system("cls")
    with open('data/usuarios.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    #Ordena os usuarios por nome usando a key nome.lower()
    linhas_ordenadas = sorted(linhas[1:], key=lambda linha: linha.split(',')[0].lower())
    for linha in linhas_ordenadas:
        print(linha.rstrip())

#----------------------------PRODUTOS----------------------------

def cadastrar_produto(): #solicita os dados e os adiciona ao 'produtos.csv'(somente clientes)
    os.system("cls")
    nome = input("Nome do Produto: ")
    preco = input("Preço: R$")
    preco = preco.replace(",", ".")
    quantidade = input("Quantidade: ")
    id = input("ID do produto: ")
    with open('data/produtos.csv', 'a') as f:
        f.write(f"{nome},{preco},{quantidade},{id},\n")
    os.system("cls")
    print("Produto Cadastrado com sucesso!")

def remover_produto():
    os.system("cls")
    id = (input("Digite o ID do produto: "))
    encontrado = False
    with open('data/produtos.csv', 'r') as f:
        linhas = f.readlines()

    os.system("cls")
    #Reescreve o csv removendo o produto encontrado
    with open('data/produtos.csv', 'w') as f:
        for linha in linhas:
            if id != linha.split(",")[3]: #Se não for o ID solicitado reescreve a linha
                f.write(linha)
            else:
                encontrado = True
    if not encontrado:
        print("O ID de produto informado não foi encontrado.")
    else:
        print("Produto removido com sucesso!")

def atualizar_produto():
    os.system("cls")
    id = input("Digite o ID do produto a ser atualizado: ")

    os.system("cls")
    print("Digite os dados para que sejam atualizados:")
    nome_atualizado = input("Nome do Produto: ")
    preco_atualizado = input("Preço: R$")
    quantidade_atualizada = input("Quantidade: ")
    id_atualizado = input("Id do produto:")

    encontrado = False
    with open('data/produtos.csv', 'r') as f:
        linhas = f.readlines()

    os.system("cls")
    #Reescreve o csv renomeando o produto encontrado
    with open('data/produtos.csv', 'w') as f:
        for linha in linhas:
            if id != linha.split(",")[3]:   #Se não for o ID solicitado reescreve a linha
                f.write(linha)
            else:                           #Se for escreve a linha com os dados atualizados
                f.write(f"{nome_atualizado},{preco_atualizado},{quantidade_atualizada},{id_atualizado}\n")
                encontrado = True
    if not encontrado:
        print("O ID de produto informado não foi encontrado.")
    else:
        print("Produto atualizado com sucesso!")

def buscar_produto():
    os.system("cls")
    encontrado = False
    busca = input("Digite o produto desejado: ")
    with open('data/produtos.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    os.system("cls")
    for linha in linhas[1:]:
        if busca.lower() in linha.lower():
            #Se a pesquisa estiver presente na linha
            #Será printado de acordo com o usuario (cliente, ou adiministração)
            if tag == "gerente" or tag == "funcionario": 
                print(linha.rstrip()) #Gerente ou funcionario
            else:
                print(f"{linha.split(",")[0]} R${linha.split(",")[1]}") #Clientes
            encontrado = True
    if not encontrado:
        print("O produto informado não foi encontrado.")

def listar_produtos():
    os.system("cls")
    with open('data/produtos.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    #Será printado de acordo com o usuario (cliente, ou adiministração)
    if tag == "gerente" or tag == "funcionario":
        for linha in linhas[1:]:
            print(linha.rstrip())
    else:
        for linha in linhas[1:]: #Printa o nome e valor de cada item
            print(f"{linha.split(",")[0]} R${linha.split(",")[1]}")

def listar_produtos_ordenados_nome():
    os.system("cls")
    with open('data/produtos.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    #Ordena os produtos por nome usando a key nome.lower()
    linhas_ordenadas = sorted(linhas[1:], key=lambda linha: linha.split(',')[0].lower())

    #Será printado de acordo com o usuario (cliente, ou adiministração)
    if tag == "gerente" or tag == "funcionario":
        for linha in linhas_ordenadas:
            print(linha.rstrip())
    else:
        for linha in linhas_ordenadas: #Printa o nome e valor de cada item
            print(f"{linha.split(",")[0]} R${linha.split(",")[1]}")

def listar_produtos_ordenados_preco():
    os.system("cls")
    with open('data/produtos.csv', 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    #Ordena os produtos por preço usando a key float(preco)
    linhas_ordenadas = sorted(linhas[1:], key=lambda linha: float(linha.split(',')[1]))

    #Será printado de acordo com o usuario (cliente, ou adiministração)
    if tag == "gerente" or tag == "funcionario":
        for linha in linhas_ordenadas:
                print(linha.rstrip())
    else:
        for linha in linhas_ordenadas: #Printa o nome e valor de cada item
            print(f"{linha.split(",")[0]} R${linha.split(",")[1]}")

#---------------------------VOLTAR,TENTAR-NOVAMENTE-OU-SAIR---------------------------

def voltar_ou_sair():
    opcoes = []
    i = 1
    for linha in menu_produtos[7:]:          #["voltar ao menu", "sair"]
        opcoes.append(str(i) + ". " + linha) #Enumera as opções ["1. voltar ao menu", "2. sair"]
        i += 1
    print("\nComo deseja continuar?\n----------------------")
    print("".join(opcoes).rstrip())
    escolha = input("\nSeleciona uma opção: ")
    if escolha == "1":
        True
    else:
        os.system("cls")
        exit()

def tentarnovamente_ou_sair():
    #Essa função é acionada quando o usuário digita o usuario ou senha incorreta
    if setor == "1": #Setor administrativo
        print("1. Tentar novamente\n2. Sair")
        escolha = input("\nEscolha uma opção: ")
        os.system("cls")
        if escolha == "1":
            return 1 #Tentar novamente
        else:
            return 0 #Sair

    elif setor == "2": #Clientes
        print("1. Tentar novamente\n2. Não tem um conta? Registre-se \n3. Sair")
        escolha = input("\nEscolha uma opção: ")
        os.system("cls")
        if escolha == "1":
            return 1 #Tentar novamente
        elif escolha == "2":
            return 2 #Registra-se
        else:
            return 0 #Sair

#----------------------------MENU----------------------------

#Essa função recebe qual o menu, e de qual indíce começara a printar
def painel_numerado(menu,inicio):
    os.system("cls")
    opcoes = []
    i = 1
    if tag == "gerente" or tag == "funcionario":
        for linha in menu[inicio:]:
            opcoes.append(str(i) + ". " + linha)
            i += 1
    else:
        for linha in menu[inicio:]:
            if linha != menu[7]: #printa o menu sem a opção "Voltar ao menu"
                opcoes.append(str(i) + ". " + linha)
                i += 1
    print("".join(opcoes).rstrip())

menu_produtos = ["Adicionar Produto\n",
                "Remover Produto\n",
                "Atualizar Produto\n",
                "Buscar Produto por Nome\n",
                "Listar Produtos\n",
                "Listar Produtos Ordenados por Nome\n",
                "Listar Produtos Ordenados por Preço\n",
                "Voltar ao Menu Principal\n",
                "Sair\n"]

menu_usuarios = ["Adicionar Usuário\n",
                "Remover Usuário\n",
                "Atualizar Usuário\n",
                "Buscar Usuário por Nome\n",
                "Listar Usuários\n",
                "Listar Usuários Ordenados por Nome\n",
                "Voltar ao Menu Principal\n",
                "Sair\n"]

menu_gerencia = ["Gerenciar usuários\n",
                "Gerenciar produtos\n",
                "Sair\n"]

#------------------------LOGIN------------------------
os.system("cls")
print("Bem-vindo ao Supermercado Mineiro!")
print("Em qual dessas opções você se encaixa?\n\n\
1. Setor Administrativo\n\
2. Cliente")
setor = input("\nEscolha uma opção: ")
if setor == "1":
    with open('data/administrativo.csv', 'r') as f: #login para administradores
        linhas = f.readlines()
else:
    with open('data/usuarios.csv', 'r', encoding='utf-8') as f: #login para clientes
        linhas = f.readlines()
os.system("cls")

#procura por usuario no arquivo csv
senha_correta = False
usuario_encontrado = False
print("Por favor faça o Login")
while True:
    if senha_correta == True:
        break
    usuario = input("Usuário: ")
    for linha in linhas[1:]:
        if usuario == linha.split(",")[0]:       #Confere se o usuário está no 'usuarios.csv
            usuario_encontrado = True
            while True:
                senha = input("Senha: ")
                if senha == linha.split(",")[1]: #Confere se a senha está correta
                    tag = linha.split(",")[2]    #Pega a tag do usuario(somente administradores)
                    senha_correta = True         #senha == True, quebra o while e completa o login
                    break
                else:                                  #Senha incorreta
                    print("Senha incorreta, por favor digite novamente!")
                    if tentarnovamente_ou_sair() == 1: #1 para tentar novamente
                        continue
                    else:                              #Qualquer outro caractere para sair
                        os.system("cls")
                        exit()

    if usuario_encontrado == False:               #Caso usuário não esteja no 'usuarios.csv'
        os.system("cls")
        print("Usuário não encontrado!")
        retorno_login = tentarnovamente_ou_sair()
        if retorno_login == 1:                    #Tentar novamente
            continue
        elif retorno_login == 2:                  #Cadastrar usuario
            cadastrar_usuario()
            exit()
        else:                                     #Sair
            os.system("cls")
            exit()

while True:
    #------------------------GERENTE------------------------
    if tag == "gerente":
        painel_numerado(menu_gerencia, 0)
        modo_trabalho = input("\nEscolha uma opção: ")
        os.system("cls")
        if modo_trabalho == "1": #gerenciar usuarios
            painel_numerado(menu_usuarios, 0)
            opcao_escolhida = input("\nEscolha uma opção: ")

            if opcao_escolhida == "1": #adicionar usuario
                cadastrar_usuario()
            elif opcao_escolhida == "2": #remover usuario
                remover_usuario()
            elif opcao_escolhida == "3": #atualizar usuario
                atualizar_usuario()
            elif opcao_escolhida == "4": #buscar usuario por nome
                buscar_usuario()
            elif opcao_escolhida == "5": #listar usuarios
                listar_usuarios()
            elif opcao_escolhida == "6": #listar usuarios ordenados
                listar_usuarios_ordenados()
            elif opcao_escolhida == "7": #voltar ao menu
                os.system("cls")
                continue
            elif opcao_escolhida == "8": #Sair
                os.system("cls")
                exit()
                
        elif modo_trabalho == "2":
            painel_numerado(menu_produtos, 0)
            opcao_escolhida = input("Escolha uma opção: ")

            if opcao_escolhida == "1": #adicionar produto
                cadastrar_produto()
            elif opcao_escolhida == "2": #remover produto
                remover_produto()
            elif opcao_escolhida == "3": #atualizar produto
                atualizar_produto()
            elif opcao_escolhida == "4": #buscar produto por nome
                buscar_produto()
            elif opcao_escolhida == "5": #listar produtos
                listar_produtos()
            elif opcao_escolhida == "6": #listar produtos ordenados por nome
                listar_produtos_ordenados_nome()
            elif opcao_escolhida == "7": #listar produtos ordenados por preco
                listar_produtos_ordenados_preco()
            elif opcao_escolhida == "8": #voltar ao menu
                os.system("cls")
                continue
            elif opcao_escolhida == "9": #sair
                os.system("cls")
                exit()

        elif modo_trabalho == "3":
            os.system("cls")
            exit()

    #------------------------FUNCIONARIO------------------------

    elif tag == "funcionario":
        painel_numerado(menu_gerencia, 0)
        modo_trabalho = input("Escolha uma opção: ")
        if modo_trabalho == "1": #gerenciar usuarios
            painel_numerado(menu_usuarios, 2)
            opcao_escolhida = input("\nEscolha uma opção: ")

            if opcao_escolhida == "1": #atualizar usuario
                atualizar_usuario()
            elif opcao_escolhida == "2": #buscar usuario por nome
                buscar_usuario()
            elif opcao_escolhida == "3": #listar usuarios
                listar_usuarios()
            elif opcao_escolhida == "4": #listar usuarios ordenados
                listar_usuarios_ordenados()
            elif opcao_escolhida == "5": #voltar ao menu
                os.system("cls")
                continue
            elif opcao_escolhida == "6": #Sair
                os.system("cls")
                exit()
                
        elif modo_trabalho == "2":
            painel_numerado(menu_produtos, 2)
            opcao_escolhida = input("Escolha uma opção: ")

            if opcao_escolhida == "1": #atualizar produto
                atualizar_produto()
            elif opcao_escolhida == "2": #buscar produto por nome
                buscar_produto()
            elif opcao_escolhida == "3": #listar produtos
                listar_produtos()
            elif opcao_escolhida == "4": #listar produtos ordenados por nome
                listar_produtos_ordenados_nome()
            elif opcao_escolhida == "5": #listar produtos ordenados por preco
                listar_produtos_ordenados_preco()
            elif opcao_escolhida == "6": #voltar ao menu
                os.system("cls")
                continue
            elif opcao_escolhida == "9": #sair
                os.system("cls")
                exit()

        elif modo_trabalho == "3":
            os.system("cls")
            exit()

    #------------------------CLIENTE------------------------

    else:
        painel_numerado(menu_produtos, 3)
        opcao_escolhida = input("Escolha uma opção: ")

        if opcao_escolhida == "1": #buscar produto por nome
            buscar_produto()
        elif opcao_escolhida == "2": #listar produtos
            listar_produtos()
        elif opcao_escolhida == "3": #listar produtos ordenados por nome
            listar_produtos_ordenados_nome()
        elif opcao_escolhida == "4": #listar produtos ordenados por preco
            listar_produtos_ordenados_preco()
        elif opcao_escolhida == "5": #sair
            os.system("cls")
            exit()

    voltar_ou_sair()