t1=int(input('digite o valor do primeiro termo da p.a: '))
r=int(input('digite o valor da razão da p.a: '))
for c in range(0,10):
    an=t1+(c)*r
    print('o termo {} da p.a é {}'.format(c+1,an))