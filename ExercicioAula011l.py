idade = 0
mulhermaior = 0
mulhermenor = 0
homemmaior = 0
homemmenor = 0
idades = 0
nomevelho = ''
for d in range(1, 7):
    print('----- {}ª Pessoa -----'.format(d))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    print('''
    [ 1 ] Masculino
    [ 2 ] Feminino
    ''')
    gen = int(input('Qual o Genêro da pessoa? '))
    print(''*30)
    if gen == 1:
        if idade <= 20:
            homemmenor += 1
            homemmaior = idade
            nomevelho = nome
        else:
            homemmaior += 1
            if idade > homemmaior:
                homemmaior = idade
                nomevelho = nome
    elif gen == 2:
        if idade <= 20:
            mulhermenor += 1
        else:
            mulhermaior += 1
    mulheres = mulhermaior + mulhermenor
    idades += idade
    media = idades / 6
print('Há um total de {} mulheres, sendo que a mais nova delas possui {} anos de idade'.format(mulheres, mulhermenor))
print('O homem mais velho é {}'.format(nomevelho))
print('A média de idade é de {:.1f} anos'.format(media))
