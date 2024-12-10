'''
Higher Order Funvtions
Funções de primeira classe
'''
def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Miguel')
)
print(
    executa(saudacao, 'Boa noite', 'Ana')
)