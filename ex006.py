n1=int(input('digite o primeiro numero:'))
n2=int(input('digite o segundo numero:'))
s=n1+n2
sb=n1-n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('a soma é {}, o produto é {} e a divisão é {:.3f}'.format(s,m,d), end='')
print(' divisão inteira {} e potencia {}'.format(di,e))