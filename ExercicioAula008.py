#if = se / if carro.esquerda(): -> True. Bloco Verde
#else = senão / else carro.esquerda(): -> False. Bloco Vermelho
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('=' * 30)
    print('Seu Carro é Novo')
else:
    print('=' * 30)
    print('Seu Carro é Velho')
print ('='*30)

#print('Carro Novo' if tempo <= 3 else 'Carro Velho')
