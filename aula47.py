'''
Faça um jogo para usuário adivinhae qual a palavra secreta.
- Voçê vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar um letra, voçê vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra.
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
'''

palavra_secreta = 'multimetro'
letras_acertadas = ''
tentativas = 0

while True:

    letra_digitada = input('Digite um letra: ')
    tentativas += 1
   
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
   
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavras formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        
        print('VOÇÊ GANHOU!! PARABENS!')
        print('A palavra era', palavra_secreta)
        print('Seu numero de tentativa foi:', tentativas)
        break