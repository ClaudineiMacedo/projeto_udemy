'''
Exercícios com funções

Crie uma função que multiplica todos argummentos
não nomeados recebidos.
Retorne o total para uma variavel e mostre o valor da variavel


Crie uma funão fala se um número é par ou impar
Retorne se o numero é par ou impar
'''


def multiplicar(*args):
     total = 1
     for numero in args:
          total *= numero
     return total

multiplacacao = multiplicar(5, 6, 9, 2, 10, 24, 39)
print(multiplacacao)

#----------------------------

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
         return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(13))
print(par_impar(87))
print(par_impar(120))
