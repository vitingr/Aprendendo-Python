from random import randint
escola = dict()
boletim = list()
escola['Nome'] = str(input('Digite o nome do aluno: '))
escola['Idade'] = int(input('Idade do aluno: '))
escola['N1'] = float(input('Digite a nota do 1 Bimestre: '))
escola['N2'] = float(input('Digite a nota do 2 Bimestre: '))
escola['N3'] = float(input('Digite a nota do 3 Bimestre: '))
escola['N4'] = float(input('Digite a nota do 4 Bimestre: '))
media = (escola['N1'] + escola['N2'] + escola['N3'] + escola['N4']) / 4
escola['Média'] = media
escola.copy()
boletim.append(escola)
print(' ' * 40)
print('-=' * 40)
print(' ' * 40)
if escola['Média'] >= 7:
    escola['Situaçao'] = '\033[92mAprovado\033[m'
elif escola['Média'] <= 6:
    escola['Situaçao'] = '\033[91mReprovado\033[m'
#for a, m in escola.items():
    #print(f'{a} é igual a {m}')
nome = escola['Nome']
id = int(randint(1111, 9999))
idade = escola['Idade']
b1 = escola['N1']
b2 = escola['N2']
b3 = escola['N3']
b4 = escola['N4']
situacao = escola['Situaçao']
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'ID: {id}')
print(' ' * 40)
print(f'1 Bimestre: {b1}')
print(f'2 Bimestre: {b2}')
print(f'3 Bimestre: {b3}')
print(f'4 Bimestre: {b4}')
print(f'Média: {media}')
print(f'Situação: {situacao}')
print(' ' * 40)
print('-=' * 40)
