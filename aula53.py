'''
Faça um alista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores de sua lista
Não permite que o programa quebre com erros de índices inexistentes na lista.
'''
import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, item in enumerate(lista):
            print(i, item)
    else:
        print('Por favor, escolha i, a ou l.')