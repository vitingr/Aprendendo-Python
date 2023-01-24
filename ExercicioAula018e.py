gols = list()
dados = dict()
total = 0
dados['Nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input('Quantas partidas '))
for c in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {c + 1}: '))
    gols.append(gol)
    total += 1
dados['Gols'] = gols
dados['Total'] = total
print('-=' * 40)
print(dados)
print('-=' * 40)
for d, e in dados.items():
    print(f'O campo {d} tem o valor {e}')
print('-=' * 40)
for a, b in enumerate(gols):
    print(f'  - Na Partida {a + 1}, fez {b} gols')
print(f'Sendo assim, um total de {total} gols')
print('-=' * 40)
