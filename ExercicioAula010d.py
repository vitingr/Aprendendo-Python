from time import sleep
print('='*30)
print(''*30)
print('\033[1;36mBem-Vindo ao Conversor de Moedas!\033[m')
print(''*30)
print('Para utilizar o conversor é muito fácil, veja:')
print('Digite o valor que você possui em reais.')
print('E após isso escolha a moeda que você deseja converter.')
print(''*30)
print('='*30)
print(''*30)
valor = float(input('Digite o valor em reais: R$'))
print(''*30)
print('Agora escolha em que moeda você deseja converter. ')
print('''
[ 1 ] Pesos Argentinos | Argentina
[ 2 ] Bolívares Bolivianos | Bolívia
[ 3 ] Pesos Chilenos | Chile
[ 4 ] Pesos Colombianos | Colômbia
[ 5 ] Florim | Curaçao
[ 6 ] Dólar | Equador
[ 7 ] Dólar Guianense | Guiana
[ 8 ] Euro | Guiana Francesa
[ 9 ] Libras | Ilhas Falklands
[ 10 ] Guaranís | Paraguai
[ 11 ] Nuevo Sol | Peru
[ 12 ] Dólar Surinamês | Suriname
[ 13 ] Dólar trinitário | Trinidad e Tobago
[ 14 ] Peso Uruguaio | Uruguai
[ 15 ] Bolívares Venezuelanos | Venezuela
''')
bra = 1
brl = 1 * valor
option = int(input('Digite sua opção: '))
print(''*30)
print('\033[31mProcessando...\033[m')
sleep(3)
print(''*30)
if option == 1:
    arg = brl * 18.44
    print('O valor de R${:.2f} equivalem a AR${:.2f}'.format(brl, arg))
elif option == 2:
    bol = brl * 1.29
    print('O valor de R${:.2f} equivalem a Bs.{:.2f}'.format(brl, bol))
elif option == 3:
    chi = brl * 149.84
    print('O valor de R${:.2f} equivalem a CL${:.2f}'.format(brl, chi))
elif option == 4:
    col = brl * 707.46
    print('O valor de R${:.2f} equivalem a CO${:.2f}'.format(brl, col))
elif option == 5:
    cur = brl * 0.33
    print('O valor de R${:.2f} equivalem a ƒ${:.2f}'.format(brl, cur))
elif option == 6:
    ecu = brl * 0.19
    print('O valor de R${:.2f} equivalem a U${:.2f}'.format(brl, ecu))
elif option == 7:
    guy = brl * 39.04
    print('O valor de R${:.2f} equivalem a GY${:.2f}'.format(brl, guy))
elif option == 8:
    fgu = brl * 0.16
    print('O valor de R${:.2f} equivalem a €{:.2f}'.format(brl, fgu))
elif option == 9:
    fak = brl * 0.13
    print('O valor de R${:.2f} equivalem a £{:.2f}'.format(brl, fak))
elif option == 10:
    par = brl * 1289.22
    print('O valor de R${:.2f} equivalem a ₲{:.2f}'.format(brl, par))
elif option == 11:
    per = brl * 0.77
    print('O valor de R${:.2f} equivalem a S/.{:.2f}'.format(brl, per))
elif option == 12:
    sur = brl * 4.01
    print('O valor de R${:.2f} equivalem a SR${:.2f}'.format(brl, sur))
elif option == 13:
    tob = brl * 1.27
    print('O valor de R${:.2f} equivalem a TT${:.2f}'.format(brl, tob))
elif option == 14:
    uru = brl * 8.01
    print('O valor de R${:.2f} equivalem a UY${:.2f}'.format(brl, uru))
elif option == 15:
    ven = brl * 779463.10
    print('O valor de R${:.2f} equivalem a 	Bs${:.2f}'.format(brl, ven))
 