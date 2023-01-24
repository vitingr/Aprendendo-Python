print('{:=^40}'.format('\033[92mBanco de Dados\033[m'))
print(''*30)
dados = list()
save = list()
pesos = list()
idades = list()
qtd = 0
adultos = 0
print('Será necessário digitar pelo menos 3 valores.')
print('Primeiro, gostariamos que você digitasse alguns dados:')
print(' '*30)
while True:
    save.append(str(input('Nome da Pessoa: ')))
    qtd += 1
    save.append(int(input('Idade da Pessoa: ')))
    save.append(int(input('Peso da Pessoa: ')))
    dados.append(save[:])
    pesos.append(save[2])
    idades.append(save[1])
    save.clear()
    print(dados)
    for p in idades:
        if p >= 18:
            adultos += 1
    if qtd >= 3:
        c = str(input('Deseja continuar? [S/N]: '))
        print(' ' * 30)
        if c in 'Nn':
            break
criancas = qtd - adultos
print('='*30)
print(' '*30)
print(f'Você cadastrou um total de {qtd} pessoas')
print(f'Sendo dessas pessoas, {adultos} são adultas e {criancas} crianças/adolescentes')
print(' '*40)
pesos.sort()
print(f'Os menores pesos foram: {pesos[0]}Kg, {pesos[1]}Kg e {pesos[2]}Kg')
pesos.sort(reverse=True)
print(f'E os maiores pesos foram: {pesos[0]}Kg, {pesos[1]}Kg e {pesos[2]}Kg')
print(' '*40)
while True:
    cont = str(input('Deseja consultar o perfil de alguém já cadastrado? [S/N]: '))
    if cont in 'Ss':
        busca = int(input('Digite o código do usuário (ordem que foi digitado): '))
        print(' '*30)
        print('='*40)
        print(f'Nome: {dados[busca][0]}')
        print(f'Idade: {dados[busca][1]} Anos')
        print(f'Peso: {dados[busca][2]}Kg')
    else:
        break
print('='*40)
