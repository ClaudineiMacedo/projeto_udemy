# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentri de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},   
# ]

#lista = [6, 2, 9, 10, 60, 23, 14, 22, 33, 5, 3, 4, 6]
#lista.sort()
#lista.sort(reverse=True)
# lista.sorted(lista)

lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},   
        ]

print(lista)


def ordena(item):
    return item['sobrenome']

lista.sort(key=ordena)

for item in lista:
    print(item)
    