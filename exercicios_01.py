#1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
'''
numeros = list(range(1, 11))
for numero in numeros:
    print(numero**2)

'''
#2 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
'''
linguagem = ["Python", "Java", "C++", "JavaScript"]
indice = linguagem.index("C++") #descubro a posição do C++
linguagem[indice] = "Ruby" #substituo diretamente na posição do C++
print(linguagem)
'''
#4.Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
'''
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem
print(contar_caracteres("engenharia de dados"))'
'''
#5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

frutas = ["maçã", "banana", "cereja"]
preco = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}


total = sum(preco[fruta] for fruta in frutas)

print(f'Preco total: R$ {total:.2f}')