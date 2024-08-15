<h1 align="center">🛒 SUPERMERCADO MINEIRO</h1>

# Introdução
Bem-vindo ao Supermercado Mineiro, um sistema de gerenciamento completo para um supermercado fictício. Este sistema foi desenvolvido para facilitar a administração e o controle das operações diárias do supermercado, oferecendo funcionalidades tanto para o setor administrativo quanto para os clientes.

## Tipos de Usuários

### O sistema é projetado para atender a três tipos principais de usuários:

### Gerente:
Tem acesso completo a todas as funcionalidades do sistema, incluindo a gestão de usuários e produtos. Permitindo-o adicionar, remover e atualizar tanto usuários quanto produtos, além de realizar buscas e listar informações de forma detalhada.

### Funcionário:
Possui permissões limitadas em comparação ao gerente. É capaz de atualizar informações de usuários e produtos, buscar dados e listar informações de forma ordenada, mas não pode adicionar ou remover itens do banco de dados.

### Cliente:
Tem acesso restrito ao sistema, focado principalmente na visualização de produtos. Pode buscar produtos, listar todos os produtos disponíveis e visualizar produtos ordenados por nome ou preço.

## Produtos e Serviços

### O Supermercado Mineiro oferece uma grande diversidade de produtos que podem ser gerenciados pelo sistema, incluindo:

**Produtos Alimentícios:** Diversos itens de supermercado, desde alimentos frescos até produtos embalados.

**Produtos de Limpeza:** Itens necessários para a higiene e limpeza doméstica.

**Bebidas e Laticínios:** Variedade de bebidas e produtos lácteos.

# Implementação

## Usuário

### Estrutura de Dados
Arquivo CSV ('usuarios.csv')<br>
Colunas: Nome, Senha, CPF e Telefone.

### Funcionalidades:

- **Criar: 'cadastrar_usuario()'** - É utilizado para realizar o cadastro de um novo usuário.

- **Ler: 'buscar_usuario()', 'listar_usuarios()', 'listar_usuarios_ordenados()'** - Consulta a base de dados e exibe as informações solicitadas.

- **Atualizar: 'atualizar_usuario()'** - Modifica as informações de um usuário existente.

- **Excluir: 'remover_usuario()'** - Remove o usuário solicitado da base de dados.

## Produto

### Estrutura de Dados
Arquivo CSV ('produtoss.csv')<br>
Colunas: Nome, Preço, Quantidade e ID.

### Funcionalidades:

- **Criar: 'cadastrar_produto()'** - É utilizado para realizar o cadastro de um novo produto.

- **Ler: 'buscar_produto()', 'listar_produtos()', 'listar_produtos_ordenados_nome()', 'listar_produtos_ordenados_preco()'** - Consulta a base de dados e exibe as informações solicitadas.

- **Atualizar: 'atualizar_produto()'** - Modifica as informações de um produto existente.

- **Excluir: 'remover_produto()'** - Remove o produto solicitado da base de dados.

# Conclusão

### Dificuldades Encontradas
#### Organização
Como estou conhecendo a liguagem ainda, e não tive muito conhecimento de projetos grandes, a organização foi uma parte que me incomodou bastante, mesmo separando várias execuções repetidas em funções e tentando compactar ao máximo o código eu ainda acredito que poderia ficar mais organizado e reduzido.

### Escolhas bem sucedidas

#### Listas de Menu
Para compactar o código que várias vezes iria precisar printar Menus na tela de modos variados, consegui criar uma função que imprimia o mesmo menu (Contendo todas as opções possíveis) e que o enumerava conforme a quantidade de opções permitida a diferentes tipos de usuários.

### O que poderia ser feito

#### Login
Logo na primeira interação com o sistema ja é solicitado ao usuario para que selecione em qual setor irá fazer login (Setor Administrativo ou Cliente) ao entrar como cliente, o usuário pode criar uma nova conta, mas não é possível fazer isso no setor administrativo. Entretando seria interessante os gerentes terem a possibilidade de criar, remover e atualizar os usuários administrativos.

#### Não permitir a criação de usuários duplicados
Ao cadastrar um usuário ou produto, não tem nenhuma checagem para verificar se já existe no sistema algum usuário ou produto com as mesmas características, tais como Nome, CPF e ID do produto.