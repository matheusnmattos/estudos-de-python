print('A confederação Nacional de Natação precisa categorizar o atleta mediante a sua idade')
idade=int(input('por gentileza, nos informe a idade: '))
if idade<=9:
    print('pela sua idade {} você é categorizado como Nadador Mirim'.format(idade))
elif idade>=9 and idade<=14:
    print('pela sua idade {} você é categorizado como Nadador Infantil'.format(idade))
elif idade>14 and idade <=19:
    print('pela sua idade {} você é categorizado como Nadador Junior'.format(idade))
elif idade>19 and idade==20:
    print('pela sua idade {} você é categorizado como Nadador Sênior'.format(idade))
elif idade>20:
    print('pela sua idade você é categorizado como nadador Master'.format(idade))