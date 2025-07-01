texto=str(input('digite a palavra e veja se é um palíndromo: '))
invertido = texto [::-1]
invertido= invertido.replace(' ',"")
texto = texto.replace(" ","")
if invertido == texto:
    print('essa palavra é um palíndromo pois {} de trás pra frente é {}'.format(texto,invertido))
else:
    print('essa palavra não é um palíndromo, pois {} dADe trás pra frente é {}'.format(texto,invertido))