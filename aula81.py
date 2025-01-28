'''
Exercício
Crie um função que encontra o primeiro duplicador considerando o segundo 
número como a duplicação. Retorne a duplicacação considerada.
Requisitos:

A ordem número duplicado é considerada a partir da segunda
ocorrência do número, ou seja, o número duplicado em si.
Exemplo:
[1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
[1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
Se não encontrar duplicados na lista, retorne -1 
'''
lista_de_listas_de_inteiros = [
    [1, 2, 3, 5, 9, 2, 9, 10, 5],
    [9, 2, 3, 8, 7, 4, 2, 7, 10],
    [1, 3, 2, 2, 7, 9, 1, 5, 8, 9],
    [6, 8, 8, 9, 10, 1, 7, 8, 9, 2],
    [10, 6, 7, 4, 3, 4, 9, 7, 2, 1],
    [3, 4, 8, 7, 9, 6, 3, 1, 2, 7],
    [10, 9, 6, 8, 7, 1, 2, 3, 10, 7],
    [5, 9, 8, 3, 2, 1, 6, 5 ,5, 10,],
    [8, 7, 9, 6, 3, 5, 6, 8, 9, 7, 4],
]

def encontra_primeiro_duplicado(lista_de_interios):
    numero_checados = set()
    primeiro_duplicado = -1
    
    for numero in lista_de_interios:
        if numero in numero_checados:
            primeiro_duplicado = numero
            break

        numero_checados.add(numero)

    return primeiro_duplicado    

for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
        )