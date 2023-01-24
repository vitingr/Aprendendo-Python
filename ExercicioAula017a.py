#pessoas = [['Pedro', 25], ['Maria', 25], ['João', 32]]
dado = list()
galera1 = list()
idades = list()
totmax = 0
totmin = 0
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera1.append(dado[:])
    dado.clear()
    print(galera1)
for p in galera1:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        totmax += 1
        print(f'Temos {totmax} pessoas maior de idade')
    else:
        print(f'{p[0]} é menor de idade. ')
        totmin += 1
        print(f'Temos {totmin} pessoas maior de idade')
    break
