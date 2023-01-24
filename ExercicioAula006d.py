import random
print('Bem-vindo ao sorteador')
print('Primeiro digite os nomes dos alunos participantes:')
aluno1 = str(input('Nome do Aluno: '))
aluno2 = str(input('Nome do Aluno: '))
aluno3 = str(input('Nome do Aluno: '))
aluno4 = str(input('Nome do Aluno: '))
aluno5 = str(input('Nome do Aluno: '))
alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
person = random.choice(alunos)
print('O escolhido foi o aluno {}'.format(person))
