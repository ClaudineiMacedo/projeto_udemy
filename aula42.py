frase = 'ghdfxbkjvxckbh,nmkjlhgfm,jkbvfbvmn,mfnbxvc'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letral_atual = frase[i]
    
    if letral_atual == ' ':
         i += 1
         continue
        
    
    qtd_apareceu_mais_vezes_atual = frase.count(letral_atual)
    
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
         letra_apareceu_mais_vezes = letral_atual

    i += 1    

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)