primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print('primeiro valor maior que o segundo.')
elif segundo_valor > primeiro_valor:
    print('Segundo valor maior que o primeiro. ')
elif primeiro_valor == segundo_valor:
    print('Os dois valores são iguais.')