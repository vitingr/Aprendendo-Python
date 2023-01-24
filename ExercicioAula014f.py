produtos = ('Temaki', 10.00,
            'Niguiri',2.00,
            'Sashimi', 1.00,
            'Jow', 1.50,
            'Hossomaki', 1.50,
            'Urumaki', 2.00,
            'Salmão Grelhado', 30.00,
            'Shimeji', 20.00)
print('-'*30)
print('\033[1;36mPreços Sushis\033[m')
print('-'*30)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>6.2f}')
