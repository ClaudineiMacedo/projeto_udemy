'''
Desempacotamento em chamadas
de métodos e funções
'''
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

a, b, *_, ap, c = lista

salas = [
    ['Maria', 'Helena',  ], # 0
    ['Elaine', ], # 1
    ['Luiz', 'João', 'Eduarda', ], # 2
]

#print(a, ap, c)

#print(['Maria', 'Helena', 1, 2, 3, 'Eduarda'])
#print(*lista)
#print(*string)
#print(*tupla)

print(*salas, sep='\n')