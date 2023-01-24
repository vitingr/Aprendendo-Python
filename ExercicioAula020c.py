

def jogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols na competição.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols no campeonato?: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    jogador(gols=gols)
else:
    jogador(nome, gols)