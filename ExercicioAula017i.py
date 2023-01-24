dados = list()
save = list()
print('\033[92mBoletim Online\033[m')
print(' ' * 40)
while True:
    nome = str(input('Nome do Aluno: '))
    n1 = float(input('Nota do 1 Bimestre: '))
    n2 = float(input('Nota do 2 Bimestre: '))
    n3 = float(input('Nota do 3 Bimestre: '))
    n4 = float(input('Nota do 4 Bimestre: '))
    media = (n1 + n2 + n3 + n4) / 4
    dados.append([nome, [n1, n2, n3, n4], media])
    c = str(input('Deseja continuar? [S/N]: '))
    if c in 'Nn':
        break
print('-='* 40)
print('{:<4}{:<10}{:>8}'.format('No', 'Nome', 'Média'))
print('-='* 40)
for a, b in enumerate(dados):
    print(f'{a:<4}{b[0]:<10}{b[2]:>8.1f}')
while True:
    print("Deseja consultar as notas detalhadas de cada aluno?")
    consulta = int(input('Digite o número do aluno que você deseja consultar: (999 interrompe): '))
    if consulta == 999:
        print('Finalizando...')
        break
    if consulta <= len(dados) - 1:
        for c in range(0, 3):
            print('-=' * 40)
            print('Informações')
            print('-=' * 40)
            print(f'Nome: {dados[consulta[0]]}')
            print(f'Nota 1 Bimestre: {dados[consulta[1][c]]}')
            print(f'Nota 2 Bimestre: {dados[consulta[1][c]]}')
            print(f'Nota 3 Bimestre: {dados[consulta[1][c]]}')
            print(f'Nota 4 Bimestre: {dados[consulta[1][c]]}')
            print(f'Média: {dados[consulta[2]]}')
            print('-=' * 40)
            print(' ' * 40)
print('Volte sempre!! :D')
