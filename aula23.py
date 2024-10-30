# Operadores in e not in
# String são iteraveis
#  0 1 2 3 4 5 6 7 8
#  c l a u d i n e i
# -9-8-7-6-5-4-3-2-1
#nome = 'claudinei'
#print(nome[7])
#print(nome[-6])

#print(15 * '-')

#print('e' in nome)
#print('f' in nome)

#print(15 * '-')

#print('zero' not in nome)
#print('nei' not in nome)

nome = input('Digite seu nome? ')
encontrar = input('Digite oque deseja encontra no nome? ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')