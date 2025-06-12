import math
co=float(input('digite o valor do cateto oposto: '))
ca=float(input('digite o valor do cateto adjacente: '))
h=math.sqrt(ca**2+co**2)
print('o valor da hipotenusa é: {}'.format(h))