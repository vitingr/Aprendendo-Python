peso = float(input('Qual é o seu peso? -> '))
altura = float(input('Qual é a sua altura? -> '))
high = altura * altura
imc = peso / high
if imc < 18.5:
    print('Essa pessoa possui o IMC de {}, que é classificado como \033[4mMAGREZA\033[m'.format(imc))
elif imc <= 24.9:
    print('Essa pessoa possui o IMC de {}, que é classificado como \033[4mNORMAL\033[m'.format(imc))
elif imc <= 29.9:
    print('Essa pessoa possui o IMC de {}, que é classificado como \033[4mSOBREPESO\033[m'.format(imc))
elif imc <= 39.9:
    print('Essa pessoa possui o IMC de {}, que é classificado como \033[4mOBESIDADE\033[m'.format(imc))
elif imc >= 40.0:
    print('Essa pessoa possui o IMC de {}, que é classificado como \033[4mOBESIDADE GRAVE\033[m'.format(imc)) 
