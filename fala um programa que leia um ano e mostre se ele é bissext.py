import datetime
ano=int(input('digite o ano que deseja saber: '))
if ano==0:
    ano=datetime.date.today().year
if ano % 4==0 and ano % 100 !=0 or ano % 400==0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('o ano {} não é bissexto'.format(ano))