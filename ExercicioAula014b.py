from time import sleep
numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze',
           'Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20:'))
    if 0 <= num <= 20:
        break
    print('Tente Novamente', end='')
print(f'O número {num} por extenso se escreve dessa maneira: {numeros[num]}')
sleep(2)
print('Deseja continuar?')
