# Operadores logicos 
# and (e)    or (ou)    not(não)
# and - Todas as condições prescisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira séra avaliada, naquela valor
# são considerados falsy (que vc ja viu).
# 0 0.0 '' false 
# Tambem existe o tipo nome que é usado para representar um não valor.
entrada = input('[E] entrada ou [S] saida: ')
senha_digitada = input('senha: ')
senha_permitida = '12345'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrada')
else:
    print('Sair')
