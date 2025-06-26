import random
numero = random.randint(0,5) #faz o computador pensar em um numero
usuario=int(input('tente advinhar o numero entre 0 a 5: ')) # aqui o jogador tenta advinhar o numero#
if usuario==numero:
    print('você acertou o numero era {}'.format(numero)) #apresentação do numero caso tenha acertado
else:
    print('você errou o numero era {} e não no numero {} tente novamente'.format(numero,usuario)) #apresentação do numero caso tenha errado