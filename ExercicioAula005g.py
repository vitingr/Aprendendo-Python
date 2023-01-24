name = input('Qual é o seu nome: ')
salary = float(input('Seu Salário R$'))
aumento = salary * 15 / 100
salary1 = salary + aumento
print('O Governo anunciou que obrigatoriamente deverá haver um aumento de 15% sobre o salário de todos os trabalhadores')
print('Com o reajuste, o seu salário que era de R${:.2f}, passará a ser de R${:.2f}'.format(salary, salary1))
