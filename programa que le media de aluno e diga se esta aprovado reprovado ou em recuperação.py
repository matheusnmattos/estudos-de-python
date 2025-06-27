nota1=float(input('digite o valor da sua nota do primeiro semestre: '))
nota2=float(input('digite o valor da sua nota do segundo semestre: '))
media=(nota1+nota2)/2
if media<5.0:
    print('com a média {} você esta reprovado direto, pois a media é de no minimo 5 para nao reprovação direta'.format(media))
elif media >=5 or media <= 6.9:
    print('com a média {} você está de recuperação pois para aprovação direta é apenas com a média superior a 7'.format(media))
else:
    print('parabéns você foi aprovado, sua média {} é igual ou superior a media para aprovação que é 7'.format(media))