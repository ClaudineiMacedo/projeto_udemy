'''
Dicionários en Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de 'chave' e 'valor'.
Chaves podem ser consideradas como o 'indice'
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
'''


pessoa = {
    'nome': 'Claudinei',
    'sobrenome': 'Macedo pires de carvalho da silva',
    'idade': 32,
    'altura': 1.8,
    'endereços': 'casa:' 'rua fernado paes de almeida' 'numero: 99',
}

#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])
