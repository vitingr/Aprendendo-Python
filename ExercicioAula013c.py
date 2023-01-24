from time import sleep
print('{:=^40}'.format('\033[1;33mCalculadora\033[m'))
print(''*40)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa
    ''')
    opcao = int(input('Qual sua opção: '))
    print(''*30)
    if opcao == 1:
        soma = n1 + n2
        print('O valor da soma entre os números {} e {} equivale a {}'.format(n1, n2, soma))
        print('' * 30)
        print('=' * 40)
    elif opcao == 2:
        mult = n1 * n2
        print('O valor da multiplicação entre os números {} e {} equivale a {}'.format(n1, n2, mult))
        print('' * 30)
        print('=' * 40)
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
            print('' * 30)
            print('=' * 40)
        elif n2 > n1:
            print('O maior número é {}'.format(n2))
            print('' * 30)
            print('=' * 40)
        elif n1 == n2:
            print('Os valores {} e {} possuem o mesmo valor!'.format(n1, n2))
            print('' * 30)
            print('=' * 40)
    elif opcao == 4:
        print('Informe os valores novamente.')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('' * 30)
        print('=' * 40)
    elif opcao == 5:
        print('FINALIZANDO...')
        sleep(2)
    else:
        print('Opção Inválida, por favor tente novamente')
        print('' * 30)
        print('=' * 40)
        sleep(2)
print(''*30)
print('='*40)
print(''*30)
print('Obrigado, volte sempre')
