print('='*30)
print('Bem-vindo ao nosso software!')
print('Esse software foi criado com a finalidade de facilitar o processo de correção de salários da nova constituição')
print('Funcionários que recebem até R$2.000,00 devem receber um aumento de 10%')
print('E funcionários que recebem menos que R$2.000,00 devem receber um aumento de 15%')
print('='*30)
nome = str(input('Insira o nome do funcionário: ').strip())
sal = float(input('Digite o salário desse funcionário: R$'))
if sal <= 2000:
    sal1 = (sal * 10 / 100) + sal
    print('O salário de {:.2f}, passará de \033[31mR${:.2f} \033[mpara \033[32mR${:.2f}.'.format(nome, sal, sal1))
else:
    sal2 = (sal * 15 / 100) + sal
    print('O salário de {:.2f}, passará de R${:.2f} para R${:.2f}.'.format(nome, sal, sal2))
