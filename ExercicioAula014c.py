from time import sleep
times = ('Atlético MG', 'Flamengo','Palmeiras','Corinthians','RB Bragantino','Fortaleza','Fluminense','América MG',
         'Ceará','Internacional','Santos','São Paulo','Atlético GO','Juventude','Cuiabá','Athlético PR','Bahia',
         'Grêmio','Sport Recife','Chapecoense')
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] 5 times melhores classificados 
    [ 2 ] 5 times piores classificados
    [ 3 ] Times em ordem alfabética 
    [ 4 ] Posição da chapecoense
    [ 5 ] Sair do Programa
    ''')
    opcao = int(input('Que opção você deseja ver: '))
    print(''*30)
    if opcao == 1:
        print(f'Os 5 primeiros times do Brasileirão 2021 são: {times[0:5]}')
        sleep(2)
    elif opcao == 2:
        print(f'Os 5 piores times do Brasileirão 2021 são: {times[15:21]}')
        sleep(2)
    elif opcao == 3:
        print(f'Os times em ordem alfabética: {sorted(times)}')
        sleep(2)
    elif opcao == 4:
        chape = times.index('Chapecoense')+1
        print('Atualmente a chapecoense se encontra na posição {}'.format(chape))
        sleep(2)
    else:
        print('Encerrando...')
        sleep(2)
print('Obrigado por usar nosso programa!')