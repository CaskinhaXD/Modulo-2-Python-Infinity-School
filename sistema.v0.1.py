# Pre-Def do Desafio
itens = ['Celular', 'Batedeira', 'Televisão', 'Notebook', 'Aparelo DVD']
valores = [1000.0, 350.0, 3450.0, 6700.0, 200.0]

# Resolução
dic_produtos = dict.fromkeys(itens, valores) # Adiciona os valores no dicionário e cria diconário

while True: # Cria um looping
    nome = input("Digite o nome do produto (Para sair digite 'Sair'): ") # Pede o nome de algum produto ao cliente
        
    if (itens.any(nome)): # Confere se o item existe
        preco = dic_produtos.get(nome) # Pega o preço do item no dicionário
        print(f"Nome do produto: {nome}") # Envia o nome do produto
        print(f"Preço do produto: R${preco}") # Envia o proço do produto
        
    elif (nome.lower() == "sair"): # Confere se o cliente digitou sair
        break; # Termina o looping
    
    else: # Caso não ocorra nada que está em cima
        print("Nome inválido.") # Avisa que nome é inválido
        opcao = input("Deseja adicionar o produto? (Sim/Nao) ") # Pergunta se quer adicionar algum item
        
        if (opcao.lower() == "sim"): # Se for sim a escolha roda o código
            novo_nome = input("Qual o nome do novo produto? ") # Pede um novo nome
            novo_preco = int(input("Qual o preço do novo produto? ")) # Pede um novo preço
            
            dic_produtos.update(novo_nome, novo_preco) # Adiciona ao dicionário
            
        else: # Se for não
            for produto, preco in dic_produtos.items(): # Cria um looping for com 2 váriaveis na seguinte formatação {produto, preço} e pega dentro do dicionário 
                print(f"Nome: {produto}") # Envia o produto que foi pego dentro do dicionário
                print(f"Preço: R$ {preco}\n") # Envia o preço que foi pego dentro do dicionário
            
# Começa parte final
# Envia a lista formatada novamente
for produto, preco in dic_produtos.items(): # Mesma explicação a cima
    print(f"Nome: {produto}") # Mesma explicação a cima
    print(f"Preço: R$ {preco}\n") # Mesma explicação a cima

# Confere se o cliente quer mudar algum preço          
opcao0 = input("Deseja modificar algum preço (Sim/Nao)? ") # Pergunta se o cliente quer mudar algum preço
            
if (opcao0.lower() == "sim"): # Se for sim roda o código
    while True: # Cria um looping
        mod_produto = input("Qual produto você deseja modificar? ('Finalizar' para sair) ") # Pergunta qual produto quer modificar
        
        if (mod_produto.lower() == "finalizar"):
            break; # Finaliza o looping

        elif (dic_produtos.get(mod_produto)): # Ve se o produto existe no dicionário
            novo_preco = int(input("Qual o novo preço? ")) # Pergunta o novo preço para o cliente
            
            dic_produtos.update(mod_produto, novo_preco) # Muda o preço do item
            
            for produto, preco in dic_produtos.items(): # Mesma explicação a cima
                print(f"Nome: {produto}") # Mesma explicação a cima
                print(f"Preço: R$ {preco}\n") # Mesma explicação a cima
            
        else: # Caso não exista
            print("Produto inválido.") # Envia que o produto é inválido
else: # Caso seja não
    print("Obrigado por utilizar o programa.") # Agradece pelo uso
            