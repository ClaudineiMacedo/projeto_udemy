'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler alterar, apagar = lista[i] (CRUD)
'''
#         01234
#        -54321
#string = 'ABCDE' # 5 caracteres
# print(bool([]))  # false
# print(lista, type(lista))


#.........0....1............2............3....4
#........-5....-4...........-3..........-2..-1
#lista = [123, True, 'Claudinei Macedo', 3.6, []]
#lista[-3] = 'Ana luiza'
#print(lista)
#print(lista[2], type(lista[2]))

#.........................................................

lista = [10, 20, 30, 40]
#lista[2] = 300
#del lista[0]
#print(lista)
#print(lista[2])
#lista.append(50)  # adiciona itens em lista
#lista.append(60)
#lista.append(70)
#lista.pop() # remove o ultimo item assima dele
#ultimo_valor = lista.pop()
#print(lista, 'Removido', ultimo_valor)

#lista.append('Claudinei')
#nome = lista.pop()
#lista.append(123)
#del lista[-1] # delete item da lista
#lista.insert(0, 5) # inserir um item na lista
#print(lista, nome)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)