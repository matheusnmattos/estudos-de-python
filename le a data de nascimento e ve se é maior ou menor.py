from datetime import date
ano_atual = date.today().year
maiores=0
menores=0
for i in range(7):
    nascimento= int(input('digite o ano de nascimento da {}ª pessoa: '.format(i+1)))
    idade = ano_atual - nascimento
    if idade>=21:
        maiores+=1
    else:
        menores+=1
print('\nTotal de pessoas Maiores de idade: {}'.format(maiores))
print('\nTotal de pessoas Menores de idade:{}'.format(menores))