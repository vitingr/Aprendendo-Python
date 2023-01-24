from time import sleep


c = ('\033[m',           # 0 - Sem cores
     '\033[0;30;41m',    # 1 - Vermelho
     '\033[0;30;42m',    # 2 - Verde
     '\033[0;30;43m',    # 3 - Amarelo
     '\033[0;30;44m',    # 4 - Azul
     '\033[0;30;45m',    # 5 - Roxo
     '\033[0;30m'       # 6 - Branco
     '');


def ajuda(com):
    titulo(f'Acessando manual do comando\'{com}\'', 4)
    print(c[6], end='')
    help(com)
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou Biblioteca? > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
