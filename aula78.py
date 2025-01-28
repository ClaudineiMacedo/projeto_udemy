'''
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores 
itens - iterável com chaves e valores 
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave 
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
'''
pessoa = {
    'nome': 'Claudinei',
    'sobrenome': 'Possadas',
    'idade': 900,
}
pessoa.setdefault('idade', 32)
print(pessoa['idade'])
print(pessoa.get('nome'))
#print(pessoa.__len__())
#print(list(pessoa.keys()))
#print(pessoa.values())
#print(pessoa.items())
