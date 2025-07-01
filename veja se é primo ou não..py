from operator import truediv

numero=int(input('digite o valor do número para saber se ele é primo: '))
if numero < 2:
    print('o número {} não é primo'.format(numero))
else:
    primo= True
for n in range(2,numero):
    if numero%n==0:
        primo = False
        break
if primo:
    print('o numero {} é um número primo'.format(numero))
else:
    print('o numero {} não é um número primo'.format(numero))