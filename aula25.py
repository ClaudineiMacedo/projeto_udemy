'''
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex: 0>-100,.1f
Convesion flags - !r !s !a
'''
variavel = 'Dinei'
print(f'{variavel}')
print(f'{variavel:0>10}')
print(f'{variavel:0<10}')
print(f'{variavel:0^10}')
print(f'{1000.54865645456:.2f}')
print(f'O Hexadecimal de 1500 é {1500:04X}')