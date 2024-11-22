'''
split e join com list e str
split - divide um string
join - une uma string
'''
frase = '      Olha só que,     coisa interresante        '
lista_palavras = frase.split(',')

listas_frases = []
for i, frase in enumerate(lista_palavras):
    listas_frases.append(lista_palavras[i].strip())

#print(listas_frases)
#print(lista_palavras)

frases_unidas = '-'.join(listas_frases)
print(listas_frases)