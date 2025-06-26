velocidade=float(input('mostre a velocidade em km/h na qual o carro que você aferiu estava correndo: '))
if velocidade > 80:
    km_acima= velocidade - 80
    multa = km_acima * 7
    print(' a multa para velocidade indicada sera de R${}'.format(multa))

else:
    print('não há multa pois a velocidade esta dentro do limite estabelecido!')