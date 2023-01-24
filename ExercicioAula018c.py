from random import randint
from time import sleep
from datetime import datetime
dados = dict()
print('-=' * 40)
print(' ' * 40)
dados['Nome'] = str(input('Digite seu nome: ')).strip()
ano = int(input('Ano de Nascimento: '))
dados['Idade'] = 2022 - ano
print('Possui carteira de trabalho?')
print('''
[ 1 ] Possuo
[ 2 ] Não possuo''')
print(' ' * 30)
resposta = int(input('Resposta: '))
if resposta == 1:
    dados['CTPS'] = int(input('Número da carteira de trabalho: '))
    dados['Ano de Contratação'] = int(input('Ano de contratação: '))
    dados['Cargo'] = str(input('Cargo: '))
    dados['Salário'] = int(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de Contratação'] + 35) - datetime.now().year)
    print(' ' * 40)
    print('\033[92mCadastro Concluído\033[m')
    sleep(2)
    print(' ' * 40)
    print('-=' * 40)
if resposta != 1:
    print('\033[91mInfelizmente não será possível prosseguir :C\033[m')
    print(' ' * 40)
    print('-=' * 40)
print(' ' * 30)
print('Informações Pessoais')
id = randint(1111, 9999)
for a, b in dados.items():
    print(f'  - {a} tem o valor de {b}')
print(f'ID do funcionário: {id}')
