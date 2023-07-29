import requests  # Importa a API Requests


def obter_informacoes_endereco(cep):  # Função para obter o CEP
  cep_formatado = cep.replace('.', '').replace('-', '').replace(
      ' ', '')  # Remover eventuais pontos, traços ou espaços do CEP

  if len(cep_formatado) != 8:  # Verificar se o CEP possui oito caracteres
    print(
        "CEP inválido. Certifique-se de digitar exatamente oito caracteres numéricos."
    )  # Caso não tenha pede para o usuário conferir se está correto
    return  # Retorna o código (Sai da função)

  if not cep_formatado.isdigit():  # Verificar se o CEP possui apenas números
    print("CEP inválido. Certifique-se de digitar apenas números."
          )  # Se possuir letras envia a mensagem
    return  # Retorna o código (Sai da função)

  url = f'https://viacep.com.br/ws/{cep_formatado}/json/'  # URL do site para pegar o CEP
  requisicao = requests.get(url)  # Faz a requisição para o CEP

  if requisicao.status_code != 200:  # Confere se não deu nenhum erro
    print("Erro ao obter informações do endereço. Tente novamente mais tarde."
          )  # Fala que deu erro
    return  # Retorna o código (Sai da função)''

  return requisicao.json()  # Retorna a informações do endereço para ser adicionado no dicionário

informacoes_endereco = {}  # Dicionário para armazenar os endereços

while True: # Looping infinito
    cep_informado = input("Digite o CEP (00000-000, 00000.000 ou 00.000-000) ('Fim' para sair): ") # Pede para digitar o CEP ou para sair 

    if cep_informado.lower() == "fim": # Ve se o usuário não quer sair do programa
        break # Caso queira, finaliza o looping
    else: # Se o usuário não quiser sair
        endereco = obter_informacoes_endereco(cep_informado) # cria a variavel endereço levando em conta o CEP informado
        if endereco: # Verifica se não é nulo
            informacoes_endereco[cep_informado] = endereco # Adiciona endereço no dicionário

# Exibindo as informações dos endereços formatadas de forma criativa
print("Informações dos Endereços:\n") # Envia falando que vai enviar as informações
for cep, endereco in informacoes_endereco.items(): # Cria um looping for com 2 váriaveis na seguinte formatação {cep, endereco} e pega dentro do dicionário 
    print(f"CEP para Informações (Identificador): {cep}") # Envia o identificador da chave
    for chave, valor in endereco.items(): # Cria um looping for com 2 váriaveis na seguinte formatação {chave, valor} e pega dentro do dicionário
        print(f"{chave.capitalize()}: {valor}") # Envia a chave e o valor dessa chave
    print() # Da espaço