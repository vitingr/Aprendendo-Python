from time import sleep


def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            print('\033[92mNúmero adicionado\033[m.')
            sleep(0.5)
            ok = True
        else:
            print('\033[91mERRO! Digite um número inteiro válido.\033[m')
            sleep(0.5)
            print(' ' * 30)
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
