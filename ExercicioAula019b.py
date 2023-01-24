from time import sleep


def espaco():
    print(' ' * 30)


def linha(msg):
    print('-=' * 30)
    print(msg)
    print('-=' * 30)


def contador(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b}, de {c} em {c}')
    sleep(2.5)
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont += c
        print('\033[92mFIM!\033[m')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.5)
            cont -= c
        print('\033[92mFIM!\033[m')


contador(1, 10, 1)
contador(10, 0, 2)
contador(3, 15, 1)
linha('         \033[94mContador Personalizado\033[m')
contadores = 0
while True:
    print('Deseja realizar o contador personalizado?')
    print('''
    [ 1 ] Realizar contador personalizado
    [ 2 ] Encerrar o programa
    ''')
    resposta = int(input('Deseja continuar? [1/2]: '))
    if resposta == 1:
        d = int(input('Digite o início do contador: '))
        e = int(input('Digite o final do contador: '))
        f = int(input('Digite o valor da sequência: '))
        contadores += 1
        contador(d, e, f)
    if resposta == 2:
        break
    if resposta != 1 and 2:
        print('ERRO! Só aceitamos os valores 1 para sim e 2 para não')
espaco()
print(f'Você digitou um total de {contadores} contadores')
print('Obrigado por utilizar nosso software :D')
