from time import sleep
print(''*30)
print('{:=^40}'.format('\033[1;36mCALCULADORA\033[m'))
print(''*30)
print('Para usar a calculadora é simples, ir respondendo o que for solicitado.')
print('Escolha o que você quer fazer?')
print('''
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
[ 5 ] Porcentagem
''')
opcao = int(input('Qual tipo de cálculo tipo de calculo você deseja realizar? '))
print(''*30)
if opcao == 1:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print('' * 30)
    print('\033[;31mPROCESSANDO...')
    print('' * 30)
    sleep(3)
    soma = n1 + n2
    print('\033[mO resultado de {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, soma))
elif opcao == 2:
    n2 = float(input('Digite um número: '))
    n1 = float(input('Digite outro número: '))
    print('' * 30)
    print('\033[;31mPROCESSANDO...')
    print('' * 30)
    sleep(3)
    menos = n1 - n2
    print('\033[mO resultado de {:.2f} - {:.2f} é igual a {:.2f}'.format(n1, n2, menos))
elif opcao == 3:
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print('' * 30)
    print('\033[;31mPROCESSANDO...')
    print('' * 30)
    sleep(3)
    mult = n1 * n2
    print('\033[mO resultado de {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, mult))
elif opcao == 4:
    print('''
    [ 1 ] Dividir pela ordem
    [ 2 ] Dividir o maior pelo menor 
    [ 3 ] Dividir o menor pelo maior 
    ''')
    option = int(input('Qual calculo você deseja realizar: '))
    print(''*30)
    if option == 1:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print('' * 30)
        print('\033[;31mPROCESSANDO...')
        print('' * 30)
        sleep(3)
        div = n1 % n2
        print('\033[mO resultado de {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, div))
    elif option == 2:
            n1 = float(input('Digite um número: '))
            n2 = float(input('Digite outro número: '))
            print('' * 30)
            print('\033[;31mPROCESSANDO...')
            print('' * 30)
            sleep(3)
            if n1 > n2:
                div = n1 % n2
                print('\033[mO resultado de {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, div))
            elif n2 > n1:
                div = n2 % n1
                print('\033[mO resultado de {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, div))
    else:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        print('' * 30)
        print('\033[;31mPROCESSANDO...')
        print('' * 30)
        sleep(3)
        if n2 > n1:
            div = n1 % n2
            print('\033[mO resultado de {:.2f} + {:.2f} é igual a {}'.format(n1, n2, div))
        elif n1 > n2:
            div = n2 % n1
            print('\033[mO resultado de {:.2f} + {:.2f} é igual a {:.2f}'.format(n1, n2, div))
else:
    print('Qual cálculo com porcentagem você deseja fazer?')
    print('''
    [ 1 ] Quanto é % de {}
    [ 2 ] Quanto é {} + %
    ''')
    opcao2 = int(input('Qual será o calculo? '))
    if opcao2 == 1:
        numero = int(input('Você quer saber a porcentagem de qual número: '))
        porc = int(input('Qual a porcentagem você quer descobrir: '))
        print('' * 30)
        print('\033[;31mPROCESSANDO...')
        print('' * 30)
        sleep(3)
        total = numero * porc / 100
        print('\033[m{:.2f}, é igual a {:.2f}% de {:.2f}'.format(total, porc, numero))
    elif opcao2 == 2:
        numero = int(input('Digite um número: '))
        porc = int(input('Porcentagem: '))
        print('' * 30)
        print('\033[;31mPROCESSANDO...')
        print('' * 30)
        sleep(3)
        total1 = (((numero * porc) / 100) + numero)
        print('\033[mO resultado de {:.2f}% mais {:.2f} é igual a {:.2f}'.format(porc, numero, total1))
 