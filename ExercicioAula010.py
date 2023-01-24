#Condições Aninhadas
nome = str(input('Qual é seu nome? ')).strip()
if nome == 'Vitor':
    print('Que nome bonito!')
elif nome == 'Pedro':
    print('Seu nome é muito popular no Brasil.')
elif nome == 'Alfredo':
    print("Que nome feio você tem.")
elif nome == 'Raimundo':
    print('Que zuado em cara, é meme?')
else:
    print('Seu nome é bem normal.')
print('Tenha um ótimo dia, {}'.format(nome))
