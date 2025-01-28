# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

#s1 = set() # vazio
#s1 = {'Claudinei', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados
# de interáveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são interáveis (for, in, not in)

#l1 = [1, 2, 3, 3, 3, 2, 3, 1]
#s1 = set(l1)
#l2 = list(s1)
#s1 = {1, 2, 3}
#print(3 not in s1)
#for numero in s1:
#    print(numero)

# Métodos úteis:
# add, update, clear, discard

#s1 = set()
#s1.add('Claudinei')
#s1.add(1)
#s1.update(('Olá mundo', 1, 2, 3, 4))
#s1.clear()
#s1.discard('Claudinei')
#s1.discard('Olá mundo')
#print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Intes presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

#s1 = {1, 2, 3}
#s2 = {2, 3, 4}
#s3 = s1 | s2
#s3 = s1 & s2
#s3 = s1 - s2
#s3 = s1 ^ s2
#print(s3)

#Exemplo de uso dos sets

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())


    if 'l' in letras:
        print('PARABÉNS')
        break
    print(letras)


