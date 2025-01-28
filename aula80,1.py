'''
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados
de interáveis.
- eles não tem índexes;
- eles não garantem ordem;
- eles são interáveis (for, in, not in)

Métodos úteis:
add, update, clear, discard
'''

s1 = set() # vazio
s1 = {'Claudinei', 1, 2, 3} # com dados
print(s1)