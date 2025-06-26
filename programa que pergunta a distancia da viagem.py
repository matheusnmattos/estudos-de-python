distancia=int(input('diga qual é a distancia da sua viagem: '))
if distancia <= 200:
    passagem = 0.50*distancia
    print('o valor da passagem será de R${}'.format(passagem))
else:
    passagem=0.45*distancia
    print('o valor da passagem será de R${}'.format(passagem))