print('{:=^40}'.format('Progressão Aritmética'))
termo = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
cont = 1
decimo = termo
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantas casas decimais? -> '))
print('A Progressão Final foi realizada com {} números'.format(total))
