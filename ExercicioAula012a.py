genero = str(input('Qual é o seu genêro, [M/F]: ')).strip().upper() [0]
while genero not in 'MmFf':
    genero = str(input("Dados inválidos, digite novamente seu genêro, [M/F]: ")).strip().upper()[0]
print('Genêro {} foi cadastrado com sucesso!'.format(genero))