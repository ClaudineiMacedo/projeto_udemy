'''
for in com listas
'''
lista = ['Claudinei', 'Ana', 'Miguel']
lista.append('Lais')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))