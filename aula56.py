'''
Lista de listas e seus índices
'''
salas = [
    ['Maria', 'Helena',  ], # 0
    ['Elaine', ], # 1
    ['Luiz', 'João', 'Eduarda', ], # 2
]
#print(salas [2][0])
#print(salas [0][0])
#print(salas [2][2][3])

for sala in salas:
    print(f'A sala é formada por {sala}')
    for aluno in sala:
        print(aluno)