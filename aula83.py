# Empacotamento e desempacotamenti de dicionários
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.7,
}

pessoa_completa = {**pessoa, **dados_pessoa}
#print(pessoa_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


#mostro_argumentos_nomeados(nome= 'Jessica', qlq=123)
mostro_argumentos_nomeados(**pessoa_completa)

#a, b = pessoa.values()
#a, b = pessoa.items()
#(a1, a2), (b1, b2) = pessoa.items()

#print(a1, a2)
#print(b1, b2)

#for chave, valor in pessoa.items():
#    print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
