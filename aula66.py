'''
Argumento nomeados e não nomeados em funções Python
Argumento nomeado tem com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''
def soma(x, y, z): # definição
    print(f'{x=} {y=} {z=}', '|', 'x + y = ', x + y + z)

soma(1, 2, 3)
soma(y=2, x=1, z=8)

print(1, 2, 3, sep='#')