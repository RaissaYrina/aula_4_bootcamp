#Crie um dicionario para armazenar informações de um livro, incluindo titulo, autor e ano de publicação; 
#Imprima cada informação

from typing import Dict, Any

livro_01 : Dict[str, Any]= {
    "Titulo": "Game of Thrones",
    "Autor": "Estagiario",
    "Ano": 2005
}

livro_02 : Dict[str, Any]= {
    "Titulo": "Game of Thrones 2",
    "Autor": "Estagiario",
    "Ano": 2007
}

lista_livros =[]

lista_livros.append(livro_01)
lista_livros.append(livro_02)



lista_livros_usando_dict: dict = {
    "livro_01": {"Titulo": "Game of Thrones",
    "Autor": "Estagiario",
    "Ano": 2005},
    "livro_02": {"Titulo": "Game of Thrones 2",
    "Autor": "Estagiario",
    "Ano": 2007}
}

print(lista_livros_usando_dict["livro_01"]["Titulo"])