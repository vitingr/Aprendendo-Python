from datetime import date
nome = str(input("Digite o nome do atleta: ")).strip()
ano = int(input('Ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
if idade <= 5:
    print('O atleta {}, possui {} anos, por isso pertence a categoria Baby'.format(nome, idade))
elif idade <= 11:
    print('O atleta {}, possui {} anos, por isso pertence a categoria Kid'.format(nome, idade))
elif idade <= 18:
    print('O atleta {}, possui {} anos, por isso pertence a categoria Junior'.format(nome, idade))
elif idade <= 40:
    print('O atleta {}, possui {} anos, por isso pertence a categoria Adulto'.format(nome, idade))
elif idade <= 100:
    print('O atleta {}, possui {} anos, por isso pertence a categoria Masters'.format(nome, idade))
elif idade <= 200:
    print('O atleta {}, possui {} anos, por isso pertence a categoria Mortos-Vivos'.format(nome, idade))
