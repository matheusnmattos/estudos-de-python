n=int(input('digite o valor a ser calculado na tabuada: '))
s = 1
for c in range(1,11):
    print('{} multiplicado por {}'.format(n,s))
    n *= s
    print('sera igual a {}'.format(n))
    n /= s
    s=s+1