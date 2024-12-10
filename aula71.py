'''
args - Argumentos não nomeados
*  -  *args (empacotamento e desempacotamento)
'''
# Lembre-te de desempacotamento

#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)


# def soma(x, y):
#    return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    

soma1 = soma(1, 2, 3)
print(soma1)

soma2 = soma(1, 2, 3, 4, 5, 12)
print(soma2)

soma3 = soma(10, 38, 19, 47, 69)
print(soma3)