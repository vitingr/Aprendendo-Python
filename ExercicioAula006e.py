import random
print('Bem-vindo ao nosso software, aqui é possível realizar vários modelos de listas')
print('Para começar digite os nomes abaixo para a apresentação de um trabalho, por exemplo.')
n1 = str(input('Nome do Aluno: '))
n2 = str(input('Nome do Aluno: '))
n3 = str(input('Nome do Aluno: '))
n4 = str(input('Nome do Aluno: '))
n5 = str(input('Nome do Aluno: '))
seq = [n1, n2, n3, n4, n5]
random.shuffle(seq)
print('A ordem de apresentação será: ')
print(seq)
