nota1 = int(input('Digite a nota do 1 bimestre: '))
nota2 = int(input('Digite a nota do 2 bimestre: '))
nota3 = int(input('Digite a nota do 3 bimestre: '))
nota4 = int(input('Digite a nota do 4 bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print('O aluno teve uma média de {}, por isso o \033[32mO Aluno foi aprovado!\033[m'.format(media))
elif 7 > media >= 5:
    print('O aluno teve uma média de {}, por isso o \033[33mO Aluno ficou em recuperação!\033[m'.format(media))
elif 5 > media:
    print('O aluno teve uma média de {}, por isso o \033[31mO Aluno foi reprovado!\033[m'.format(media))
