'''
Introdução as funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''
#def imprimir(a, b, c):
#    print(a, b, c)

#imprimir(1, 2, 3)
#imprimir(4, 3, 4)


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Claudinei')
saudacao('Milguel')
saudacao()
saudacao('Lais')