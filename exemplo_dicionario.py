#exemplo_dicionario
'''é um modelo de banco de dados que armazena dados em pares de chave e valor.'''
import json

lista: list = ['Sapato', 39, 10.38, True]

produto_01: dict = {
    "nome" : "Sapato",
    "quantidade" : 39,
    "preco" : 10.38,
    "disponibilidade" : True
}

produto_02: dict = {
    "nome" : "Televisão",
    "quantidade" : 10,
    "preco" : 700.48,
    "disponibilidade" : False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)

