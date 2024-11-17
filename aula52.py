'''
enumerate - enumera iteráveis (índices)
'''
lista = ['Claudinei', 'Ana', 'Miguel']
lista.append('Lais')

#for item in enumerate(lista):
#    indice, nome = item  
#    print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice,nome)