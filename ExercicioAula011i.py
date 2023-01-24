frase = (input('Digite uma palavra: ')).strip()
palavra = frase.lower()
palavras = palavra.split()
jt = ''.join(palavras)
inverso = ''
for letra in range(len(jt) - 1, -1, -1):
    inverso += jt[letra]
print('Essa frase ao contrário é {}'.format(inverso))
if inverso == palavra:
    print('\033[32mSim\033[m, Essa frase é um Palíndromo')
else:
    print('\033[31mNão\033[m, Essa frase não é um Palíndromo')
