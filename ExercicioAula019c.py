from time import sleep


def linha(msg):
    print('-=' * 30)
    print(msg)
    print('-=' * 30)


def maior(* num):
    print('-=' * 30)
    print('Analisando valores passados...')
    sleep(2.5)
    qtd = len(num)
    maior = max(num)
    print(f'Você digitou {qtd} números, são eles: {num}', flush=True)
    print(f'O maior valor digitado é o número \033[92m{maior}\033[m ', flush=True)


maior(1, 3, 5, 6, 7)
maior(2, 5, 4, 7)
maior(1, 2, 4)
maior(4, 6)
maior(6)
linha('     \033[94mPersonalizado\033[m')
while True:
    print('Deseja realizar o software?')
    print('''
    [ 1 ] Realizar contador personalizado
    [ 2 ] Encerrar o programa
    ''')
    resposta = int(input('Deseja continuar? [1/2]: '))
    if resposta == 1:
        a = int(input('Digite um valor: '))
        b = int(input('Digite um valor: '))
        c = int(input('Digite um valor: '))
        d = int(input('Digite um valor: '))
        e = int(input('Digite um valor: '))
        maior(a, b, c, d, e)
    if resposta == 2:
        break
    if resposta != 1 and 2:
        print('ERRO! Só aceitamos os valores 1 para sim e 2 para não')
