soma=0
for c in range(0,6):
    i=int(input(f'digite o {c} valores desejados: '))
    if i%2==0:
        soma+=i
print('A soma dos números pares é: {}'.format(soma))