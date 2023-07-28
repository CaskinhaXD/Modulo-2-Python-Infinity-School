def maior_idade(dicionario):

    if not dicionario:

        return None



    pessoa_maior_idade = max(dicionario, key=dicionario.get)

    return pessoa_maior_idade



pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}



idade_joao = pessoas["João"]

print(idade_joao)



pessoas["Ana"] = 31

print(pessoas)



nome_pessoa_maior_idade = maior_idade(pessoas)

print(f"A pessoa com maior idade é: {nome_pessoa_maior_idade}")

