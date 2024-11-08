'''
Iterável -> str, range, etc (____iter____)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
'''
texto = ('Claudinei')
#iteratador = iter(texto)

#while True:
#    try:
#        print(next(iteratador))
#    except StopIteration:
#        break

for letra in texto:
    print(letra)