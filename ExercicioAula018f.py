from time import sleep
datacenter = list()
nomesmulheres = list()
dados = dict()
tot = 0
homens = 0
mulheres = 0
soma = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Genero'] = str(input('Genêro [M/F]: ')).strip().upper()[0]
        if dados['Genero'] in 'Mm':
            homens += 1
            tot += 1
            break
        elif dados['Genero'] in 'Ff':
            mulheres += 1
            tot += 1
            nomesmulheres.append(dados['Nome'])
            break
        sleep(1)
        print('\033[91mErro! Digite somente F para feminino e M para masculino\033[m.')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    datacenter.append(dados.copy())
    while True:
        c = str(input('Deseja continuar? [N/S]: ')).upper()[0]
        if c in 'SN':
            break
        sleep(1)
        print('\033[91mErro! Digite somente N para interromper e S para continuar\033[m.')
    if c == 'N':
        break
media = soma / tot
print('-=' * 40)
print(' ' * 30)
print(f'Foram cadastradas um total de {tot} pessoas')
print(f'A média de idade das pessoas cadastradas é de {media:.1f} anos')
print(f'As mulheres cadastradas foram: {nomesmulheres}')
print(' ' * 30)
print('-=' * 40)
print(' ' * 30)
print(f'Pessoas acima da média de idade: ')
for p in datacenter:
    if p['Idade'] >= media:
        print(' ' * 40)
        for a, b in p.items():
            print(f' -{a} = {b}', end='')
        print()
print(' ' * 30)
print('\033[92m<< ENCERRADO >>\033[m')
