valor=float(input('digite o valor do produto que você vai comprar R$ '))
print('escolha a opção de pagamento ')
op=int(input('1 - A vista no dinheiro ou cheque.\n'
              '2 - A vista no cartão.\n'
              '3 - Em até 2x no cartão.\n'
              '4 - em até 3x ou mais no cartão.\n:'))
if op==1:
    valor= valor-(valor*0.1)
    print('o valor do produto na condição solicitada será de {} com 10% de desconto '.format(valor))
elif op==2:
    valor= valor-(valor*0.05)
    print('o valor do produto na condição solicitada será de {} com 5% de desconto'.format(valor))
elif op==3:
    valor= valor
    print('o valor do produto na condição solicitada será de {} com valor normal'.format(valor))
elif op==4:
    valor= valor+(valor*0.2)
    print('o valor do produto na condição solicitada será de {} com acréscimo de 20% no valor total'.format(valor))
else:
    print('digite uma opção valida!')